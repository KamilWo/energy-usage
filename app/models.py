from calendar import monthrange
from .consts import DATE_FORMAT
from datetime import date
from dataclasses import dataclass, field
from typing import Optional
from .utils import apply_tariff


# TODO: in v2.0 I would like to use database framework (e.g. SQLAlchemy)
#  to handle the models and serialise them in a relational database


@dataclass
class Member:
    """ Represents Bulb Customer's (member). """

    member_id: str
    accounts: set
    name: str = ""

    def __hash__(self):
        return hash(self.member_id)


@dataclass
class Account:
    """ Represents Bulb Customer's (member) account. """

    account_id: str
    member_id: str

    def __hash__(self):
        return hash(f'{self.account_id}_{self.member_id}')


@dataclass
class BaseBill:
    """ Represents Bulb Customer's bill for the given date. """

    member: Member
    account: Account
    bill_date: str
    units: int
    total: float

    def __hash__(self):
        return hash(f'{self.member.member_id}_{self.account.account_id}_'
                    f'{self.bill_date}')


@dataclass
class ElectricityBill(BaseBill):
    """ Represents Bulb Customer's electricity bill for
        the given date.
    """

    billing_type: str = "electricity"

    def __hash__(self):
        return BaseBill.__hash__(self)


@dataclass
class GasBill(BaseBill):
    """ Represents Bulb Customer's gas bill for the given date. """

    billing_type: str = "gas"

    def __hash__(self):
        return BaseBill.__hash__(self)


@dataclass
class BillDatabase:
    """ Bulb bills database. """

    members: set = field(default_factory=set)
    accounts: list = field(default_factory=list)
    electricity_bills: dict = field(default_factory=dict)
    gas_bills: dict = field(default_factory=dict)

    def add_member(self, member: Member) -> None:
        """ Stores Member in the database.

        :param Member member: Provided Member object.

        :returns: None
        """

        self.members.add(member)

    def is_member(self, member_id: str) -> bool:
        """ Checks if Member exists in the database.

        :param str member_id: Provided member_id string.

        :returns: True if Member is in the database, False if doesn't exist.
        :rtype: bool
        """

        return member_id in [member.member_id for member in self.members]

    def add_account(self, account: Account) -> None:
        """ Stores Account in the database.

        :param Account account: Provided Account object.

        :returns: None
        """

        self.accounts += [account]

    def is_account(self, account_id: str) -> bool:
        """ Checking if Account exists for specific Member.

        :param str account_id: Provided account_id string.

        :returns: True if Account is in the database, False if doesn't exist.
        :rtype: bool
        """

        return account_id in [acc.account_id for acc in self.accounts]

    def get_member_accounts(self, member_id: str) -> list:
        """ Gets Accounts list for specific Member.

        :param str member_id: Provided member_id string.

        :returns: Accounts for specific Member.
        :rtype: list
        """

        return [acc.account_id for acc in self.accounts
                if acc.member_id == member_id]

    def add_electricity_bill(self, el_bill: ElectricityBill) -> None:
        """ Stores Electricity Bill.

        :param ElectricityBill el_bill: ElectricityBill object.

        :returns: None
        """

        self.electricity_bills[
            f'{el_bill.member.member_id}_{el_bill.account.account_id}_'
            f'{el_bill.bill_date}'
        ] = el_bill

    def add_gas_bill(self, gas_bill: GasBill) -> None:
        """ Stores Gas Bill.

        :param GasBill gas_bill: GasBill object.

        :returns: None
        """

        self.gas_bills[
            f'{gas_bill.member.member_id}_{gas_bill.account.account_id}_'
            f'{gas_bill.bill_date}'
        ] = gas_bill

    def process_energy_sources(self, energy_source: str, sources: dict,
                               member: Member, account: Account) -> None:
        """ Processes energy sources and adds them to the database.

        It's necessary to find first month's units and follow them linearly

        :param str energy_source: Energy source type: `electricity` or `gas`.
        :param dict sources: Bill readings dict.
        :param Member member: Provided Member.
        :param Account account: Provided Account.

        :returns: None
        """

        if member and account:
            if energy_source == 'electricity' and energy_source in sources:
                electricity_readings = sources[energy_source]
                previous_reading = None
                for er in electricity_readings:
                    # It's necessary to find first month's units
                    # and follow them linearly
                    if previous_reading:
                        eom_date, units_delta, days_delta = \
                            self.calculate_units(
                                previous_reading=previous_reading,
                                current_reading=er
                            )
                        self.add_electricity_bill(
                            ElectricityBill(
                                member=member,
                                account=account,
                                bill_date=eom_date.strftime(DATE_FORMAT),
                                units=units_delta,
                                total=apply_tariff(
                                    energy_source='electricity',
                                    units=units_delta,
                                    amount_of_days=days_delta
                                )
                            )
                        )
                    previous_reading = er
            elif energy_source == 'gas' and energy_source in sources:
                gas_readings = sources[energy_source]
                previous_reading = None
                for gr in gas_readings:
                    # It's necessary to find first month's units
                    # and follow them linearly
                    if previous_reading:
                        eom_date, units_delta, days_delta = \
                            self.calculate_units(
                                previous_reading=previous_reading,
                                current_reading=gr
                            )
                        self.add_gas_bill(
                            GasBill(
                                member=member,
                                account=account,
                                bill_date=eom_date.strftime(DATE_FORMAT),
                                units=units_delta,
                                total=apply_tariff(
                                    energy_source='gas',
                                    units=units_delta,
                                    amount_of_days=days_delta
                                )
                            )
                        )
                    previous_reading = gr

    @classmethod
    def calculate_units(cls, previous_reading: dict,
                        current_reading: dict) -> tuple:
        """ Calculates estimated decimal number of units in current month

        designated by `current_date`. It requires data from previous month.

        :param int previous_reading: Number of units from the previous month.
        :param str current_reading: Previous month's readingDate date.

        :returns: End of the month date and units for the end of the month.
        :rtype: tuple
        """

        prev_date = date.fromisoformat(previous_reading['readingDate'][:10])
        curr_date = date.fromisoformat(current_reading['readingDate'][:10])
        days_delta = (curr_date - prev_date).days
        eom_date = date(
            year=prev_date.year,
            month=prev_date.month,
            day=monthrange(prev_date.year,
                           prev_date.month)[1]
        )
        units_delta = current_reading['cumulative'] - \
            previous_reading['cumulative']
        return eom_date, units_delta, days_delta

    def get_bills_amount(self, energy_source: str, member_id: str,
                         account_id: str, given_date: str,
                         all_accounts: Optional[str] = None) -> tuple:
        """ Retrieve electricity bills for member and account.

        :param str energy_source: Type of source of energy for which bill
            is being calculated.
        :param str member_id: Member identifier.
        :param str account_id: Account identifier.
        :param str given_date: Specified date of the bill.
        :param Optional[str] all_accounts: If specified, all accounts
            for the member will be calculated.

        :returns: Total bill value and total number of units
        :rtype: tuple
        """

        total = 0.0
        units = 0
        if energy_source == 'electricity':
            if all_accounts == 'ALL':
                for account_id in self.get_member_accounts(member_id):
                    eb = self.electricity_bills[
                        f'{member_id}_{account_id}_{given_date}']
                    total += eb.total
                    units += eb.units
                return total, units
            else:
                eb = self.electricity_bills[
                    f'{member_id}_{account_id}_{given_date}']
                return eb.total, eb.units
        elif energy_source == 'gas':
            if all_accounts == 'ALL':
                for account_id in self.get_member_accounts(member_id):
                    gb = self.gas_bills[
                        f'{member_id}_{account_id}_{given_date}']
                    total += gb.total
                    units += gb.units
                return total, units
            else:
                gb = self.gas_bills[
                    f'{member_id}_{account_id}_{given_date}']
                return gb.total, gb.units
