import logging
import os.path

from app.bill_member import calculate_and_print_bill
from typing import Optional

# Sphinx was causing an error and the path to the log file has to be absolute.
logging.basicConfig(
    filename=os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'logs', 'bulb.log'),
    level=logging.DEBUG
)
logger = logging.getLogger('Bulb')


def parse_arguments():
    """ Parses arguments for command line application. """

    import argparse
    parser = argparse.ArgumentParser(
        description="""Main entry point for command line app to compute \n
            your energy bill based on a given `readings.json` file, \n
            which is assumed to be in the data/ directory.""")
    parser.add_argument('--member_id', type=str,
                        help='The identifier we use to select the member '
                             'profile.')
    parser.add_argument('--account_id', type=str,
                        help='The identifier we use to select the member '
                             'account. You can choose to bill for all '
                             'accounts, or an individual account.')
    parser.add_argument('--bill_date', type=str,
                        help='ISO standard formatted date for UTC timezone.')
    parser.add_argument('--energy_source', type=str,
                        help='Type of the energy source, can be: '
                             '`electricity` or `gas`. If none provided, '
                             '`electricity` will be assumed.')
    return parser.parse_args()


def main(
    member_id: Optional[str] = None,
    account_id: Optional[str] = None,
    bill_date: Optional[str] = None,
    energy_source: Optional[str] = None
):
    """ Main entry point for bill calculation command line app.

    Expects a date format as a string: %Y-%m-%d, e.g. '2017-11-01'
    Timezone is assumed to be UTC.

    :param str member_id: the member identifier in our dataset.
    :param str account_id: the account identifier in our dataset.
        If left unset, we return a total bill for all accounts.
    :param str bill_date: The billing date is the last day of the month.
    :param str energy_source: Type of the energy source, can be:
        `electricity` or `gas`.
    """

    calculate_and_print_bill(member_id, account_id, bill_date, energy_source)


if __name__ == '__main__':
    args = parse_arguments()
    main(
        member_id=args.member_id,
        account_id=args.account_id,
        bill_date=args.bill_date,
        energy_source=args.energy_source,
    )
