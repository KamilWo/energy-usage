import logging

from calendar import monthrange
from datetime import date
from .exceptions import IncorrectDateType
from .tariff import BULB_TARIFF


def apply_tariff(energy_source: str, units: float,
                 amount_of_days: int) -> float:
    """ Applies tariff to the units.

    :param str energy_source: Can be `electricity` or `gas`
    :param float units: number of units in the current month
    :param int amount_of_days: number of days in a month.

    :returns: Total bill in £
    :rtype: float
    """

    unit_rate = BULB_TARIFF[energy_source]['unit_rate']
    standard_charge = BULB_TARIFF[energy_source]['standing_charge']

    # Bill calculations: units and standard charge
    total_bill = units * unit_rate
    total_bill += amount_of_days * standard_charge

    # Expressing value in £ and with 2 decimal places
    return float(f'{total_bill/100:.2f}')


def count_month_days(given_date: str):
    """ Counts days in a month and returns the amount.

    Especially useful to calculate standing charge per month,
    because readings are taken only once per month, but bill
    date is at the end of the month.

    :param str given_date: UTC date in string format.
    :returns: number of days in month
    :rtype: int

    :raises IncorrectDateType when bill_date string can't be parsed.
    """
    try:
        given_date = date.fromisoformat(given_date[:10])
    except ValueError:
        logging.error(f'IncorrectDateType error occurred '
                      f'for bill_date: {given_date}.')
        raise IncorrectDateType("Incorrect date format, should be YYYY-MM-DD.")
    _, amount_of_days = monthrange(given_date.year, given_date.month)
    return amount_of_days


def end_of_month_date(given_date: str) -> date:
    """ Returns date object representing date at the end
    of the current month.

    :param str given_date: Provided date string.

    :returns:
    """
    try:
        curr_date = date.fromisoformat(given_date)
    except ValueError:
        logging.error(f'Provided date has incorrect format: {given_date}.')
        raise IncorrectDateType(f"Provided date has incorrect "
                                f"format: {given_date}")
    return curr_date.replace(
        day=monthrange(curr_date.year, curr_date.month)[1]
    )
