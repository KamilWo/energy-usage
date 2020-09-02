import logging

from collections import defaultdict
from datetime import datetime, date
from .exceptions import (
    UnknownAccount,
    UnknownBillingType,
    UnknownMember
)
from .load_readings import get_readings
from .models import (
    Account,
    BillDatabase,
    Member
)
from typing import Optional
from .utils import apply_tariff, count_month_days


def prepare_database() -> BillDatabase:
    """ Prepares database from readings.

    :returns: Database of the bills
    :rtype: BillDatabase
    """
    # Retrieve readings
    readings = get_readings()

    # Initialise database
    db = BillDatabase(
        members=set(),
        accounts=dict(),
        electricity_bills=dict(),
        gas_bills=dict()
    )

    # Loop through the readings and add all the objects to the database
    for member_id in readings:
        member = readings[member_id]
        new_member = Member(
            member_id=member_id,
            name=member_id,
            accounts=set()
        )
        for accounts in member:
            for account_id in accounts.keys():
                new_account = Account(
                        account_id=account_id,
                        member_id=member_id
                    )
                db.add_account_for_member(
                    member_id=member_id,
                    account=new_account
                )
                for sources in accounts[account_id]:
                    for source in sources.keys():
                        db.process_energy_sources(
                            energy_source=source,
                            sources=sources,
                            member=new_member,
                            account=new_account
                        )
    return db


def calculate_bill(member_id: Optional[str] = None,
                   account_id: Optional[str] = None,
                   bill_date: Optional[str] = None,
                   energy_type='electricity') -> (float, float):
    """ Computes the customer bill.

    :param str member_id: Given Customer (member) identifier.
    :param str account_id: Given Account identifier.
    :param str bill_date: Date of the bill (end of the month).
    :param str energy_type: Type of the billing, can be `electricity`
        or `gas`.

    :returns: Amount and kwh values.
    :rtype: tuple

    :raises UnknownMember: When user provides unknown member_id.
    :raises UnknownAccount: When user provides unknown account.
    :raises IncorrectDateType: When user provides date in incorrect format.
    """

    db = prepare_database()

    # Handling unknown members
    if not db.is_member(member_id):
        logging.error(f'UnknownMember error occurred for member_id '
                      f'{member_id}')
        raise UnknownMember(f'Member {member_id} is unknown.')

    # Handling unknown accounts
    if account_id != 'ALL' and not db.is_member_account(
        member_id=member_id,
        account_id=account_id
    ):
        logging.error(f'UnknownAccount error occurred for member '
                      f'{member_id}: account {account_id} doesn\'t exist')
        raise UnknownAccount(f'Account {account_id} is unknown '
                             f'or not allowed.')

    bill_date = datetime.strptime(bill_date, '%Y-%m-%d')

    units = 0
    amount_of_days = 0
    db.get_bills_amount(
        energy_type=energy_type,
        member_id=member_id,
        account_id=account_id,
        given_date=bill_date,
        all_accounts=account_id
    )

    # Rounding bill result to full £
    return round(apply_tariff(
        billing_type='electricity',
        units=units,
        amount_of_days=amount_of_days)
    ), units


def calculate_and_print_bill(member_id: str, account: str, bill_date: str,
                             billing_type: str) -> None:
    """ Computes the customer bill and then prints the result to screen.

    Account is an optional argument - I could bill for one account or many.
    There's no need to refactor this function.

    :param str member_id: Customer
    :param str account: Account
    :param str bill_date: Date of the bill
    :param str billing_type: Type of the billing, can be `electricity`
        or `gas`.

    :returns: none
    """
    if billing_type not in ('electricity', 'gas'):
        logging.error(f'WrongBillingType error occurred for billing '
                      f'type: {billing_type}')
        raise UnknownBillingType('Acceptable billing type is only '
                                 '`electricity` or `gas`.')

    member_id = member_id or 'member-123'
    bill_date = bill_date or '2017-08-31'
    account = account or 'ALL'
    amount, kwh = calculate_bill(member_id, account, bill_date)
    print(f'Hello {member_id}!')
    print(f'Your bill for {account} on {bill_date} is £{amount}')
    print(f'based on {kwh}kWh of usage in the last month.')
