from calendar import monthrange
from collections import defaultdict
from datetime import date, datetime
from dataclasses import dataclass, field
from typing import Dict, Optional
from .utils import count_month_days


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


@dataclass
class BaseBill:
    """ Represents Bulb Customer's bill for the given date. """

    member: Member
    account: Account
    bill_date: date
    units: int
    total: float

    def __hash__(self):
        return hash((
            self.member.member_id,
            self.account.account_id,
            self.bill_date
        ))


@dataclass
class ElectricityBill(BaseBill):
    """ Represents Bulb Customer's electricity bill for
        the given date.
    """

    billing_type: str = "electricity"


@dataclass
class GasBill(BaseBill):
    """ Represents Bulb Customer's gas bill for the given date. """

    billing_type: str = "gas"


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
            hash((el_bill.member.member_id, el_bill.account.account_id,
                  el_bill.bill_date))
        ] = el_bill

    def add_gas_bill(self, gas_bill: GasBill) -> None:
        """ Stores Gas Bill.

        :param GasBill gas_bill: GasBill object.

        :returns: None
        """
        self.gas_bills[
            hash((gas_bill.member.member_id, gas_bill.account.account_id,
                  gas_bill.bill_date))
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
                prev_reading = None
                prev_month_date = ""
                prev_month_units = 0
                for er in electricity_readings:
                    # It's necessary to find first month's units
                    # and follow them linearly
                    if prev_reading:
                        prev_month_date, prev_month_units = \
                            self.calculate_units(
                                prev_eom_cumulative=prev_month_units,
                                prev_eom_date=prev_month_date,
                                prev_cumulative=prev_reading['cumulative'],
                                prev_date=prev_reading['readingDate'][:10],
                                current_cumulative=er['cumulative'],
                                current_date=er['readingDate'][:10],
                                days_in_month=count_month_days(
                                    given_date=er['readingDate'][:10]
                                )
                            )
                        self.add_electricity_bill(
                            ElectricityBill(
                                member=member,
                                account=account,
                                bill_date=date.fromisoformat(
                                    er['readingDate'][:10]),
                                units=0,
                                total=0.0
                            )
                        )
                    prev_reading = er
            elif energy_source == 'gas' and energy_source in sources:
                gas_readings = sources[energy_source]
                prev_reading = None
                prev_month_date = ""
                prev_month_units = 0
                for gr in gas_readings:
                    # It's necessary to find first month's units
                    # and follow them linearly
                    if prev_reading:
                        prev_month_date, prev_month_units = \
                            self.calculate_units(
                                prev_eom_cumulative=prev_month_units,
                                prev_eom_date=prev_month_date,
                                prev_cumulative=prev_reading['cumulative'],
                                prev_date=prev_reading['readingDate'],
                                current_cumulative=gr['cumulative'],
                                current_date=gr['readingDate'][:10],
                                days_in_month=count_month_days(
                                    given_date=gr['readingDate'][:10]
                                )
                            )
                    self.add_gas_bill(
                        GasBill(
                            member=member,
                            account=account,
                            bill_date=date.fromisoformat(
                                gr['readingDate']),
                            units=0,
                            total=0.0
                        )
                    )
                    prev_reading = gr

    @classmethod
    def calculate_units(cls, prev_eom_cumulative: int, prev_eom_date: str,
                        prev_cumulative: int, prev_date: str,
                        current_cumulative: int, current_date: str,
                        days_in_month) -> tuple:
        """ Calculates estimated decimal number of units.

        :param int prev_eom_cumulative: Number of units from the end
            of previous month.
        :param str prev_eom_date: Previous month's end date.
        :param int prev_cumulative: Number of units from the previous month.
        :param str prev_date: Previous month's readingDate date.
        :param str prev_date: Previous month's readingDate date.
        :param int current_cumulative: Number of units from the current month.
        :param str current_date: Current month's readingDate date.
        :param int days_in_month: Number of days in the current month.

        :returns: End of the month date and units for the end of the month.
        :rtype: tuple
        """
        if prev_eom_cumulative and prev_eom_date:
            units_delta = current_cumulative - prev_cumulative
        else:
            units_delta = current_cumulative - prev_cumulative

        curr_date = datetime.combine(
            date.fromisoformat(current_date[:10]), datetime.min.time()
        )
        delta = curr_date - datetime.combine(
            date.fromisoformat(prev_date[:10]),
            datetime.min.time()
        )
        # End of the month date
        eom_date = curr_date.replace(
            day=monthrange(curr_date.year, curr_date.month)[1]
        )
        units = units_delta / delta.days * days_in_month
        return eom_date, units

    def get_bills_amount(self, energy_source: str, member_id: str,
                         account_id: str, given_date: date,
                         all_accounts=None) -> float:
        """ Retrieve electricity bills for member and account.

        :param energy_source: Type of source of energy for which bill
            is being calculated.
        :param member_id: Member identifier.
        :param account_id: Account identifier.
        :param given_date: Specified date of the bill.
        :param all_accounts: If specified, all accounts for the member
            will be calculated.

        :returns: List of bills
        """

        total = 0.0
        if energy_source == 'electricity':
            if all_accounts:
                for account_id in self.get_member_accounts(member_id):
                    total += self.electricity_bills[
                        hash((member_id, account_id, given_date))].total
            else:
                return self.electricity_bills[
                    hash((member_id, account_id, given_date))].total
        elif energy_source == 'gas':
            if all_accounts:
                for account_id in self.get_member_accounts(member_id):
                    total += self.gas_bills[
                        hash((member_id, account_id, given_date))].total
            else:
                return self.electricity_bills[
                    hash((member_id, account_id, given_date))].total
