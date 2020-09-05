import pytest

from app.bill_member import (
    calculate_bill,
    prepare_database,
    calculate_and_print_bill
)
from app.exceptions import (
    UnknownAccount,
    UnknownBillingType,
    UnknownMember
)
from app.models import (
    Account,
    Member,
)
from tests.consts import (
    TEST_PREPARE_DATABASE_DB_ELECTRICITY_BILLS,
    TEST_PREPARE_DATABASE_DB_GAS_BILLS
)


class TestBillMember(object):

    @pytest.mark.parametrize(
        ('member_id', 'account_id', 'bill_date', 'energy_source',
         'expected_amount', 'expected_kwh'),
        (
            ('member-123', 'account-abc', '2017-07-31', 'electricity', 27.57,
             167),
            ('member-123', 'ALL', '2017-07-31', 'electricity', 27.57, 167),
            ('member-123', 'ALL', '2017-08-31', 'electricity', 9.86, 62),
            ('member-123', 'account-abc', '2017-09-30', 'electricity', 38.19,
             223),
            ('member-123', 'account-abc', '2017-10-31', 'electricity', 31.24,
             245),
            ('member-123', 'ALL', '2017-10-31', 'electricity', 31.24, 245),
            ('member-123', 'account-abc', '2018-01-31', 'electricity', 46.42,
             333),
            ('member-123', 'ALL', '2018-01-31', 'electricity', 46.42, 333),
        )
    )
    def test_calculate_bill(
        self,
        member_id: str,
        account_id: str,
        bill_date: str,
        energy_source: str,
        expected_amount: float,
        expected_kwh: int
    ):
        """ Testing calculate_bill.
        :param str member_id: Given Customer (member) identifier,
            parametrised.
        :param str account_id: Given Account identifier, parametrised.
        :param str bill_date: Date of the bill (end of the month),
            parametrised.
        :param str energy_source: Type of the billing, can be `electricity`
            or `gas`, parametrised.
        :param float expected_amount: Calculated and expected amount of
            bill, parametrised.
        :param int expected_kwh: Calculated and expected amount of kwh
            units (usage), parametrised.
        """

        assert calculate_bill(
            member_id=member_id,
            account_id=account_id,
            bill_date=bill_date,
            energy_source=energy_source
        ) == (expected_amount, expected_kwh)

        with pytest.raises(UnknownMember):
            calculate_bill(
                member_id='aa',
                account_id=account_id,
                bill_date=bill_date,
                energy_source=energy_source
            )

        with pytest.raises(UnknownAccount):
            calculate_bill(
                member_id=member_id,
                account_id='bb',
                bill_date=bill_date,
                energy_source=energy_source
            )

        with pytest.raises(UnknownBillingType):
            calculate_bill(
                member_id=member_id,
                account_id=account_id,
                bill_date=bill_date,
                energy_source='foo'
            )

    @pytest.mark.parametrize(
        'json_file_name',
        (
            'test_readings.json',
        )
    )
    def test_prepare_database(self, json_file_name: str):
        """ Testing preparation of the database and important functions.

        :param str json_file_name: Path to the test JSON file, parametrised.
        """

        db = prepare_database(data_source=json_file_name)

        assert db.members == {
            Member(member_id='member-123', accounts=set(), name='member-123'),
            Member(member_id='member-124', accounts=set(), name='member-124')
        }
        assert db.accounts == [
            Account(account_id='account-abc', member_id='member-123'),
            Account(account_id='account-abd', member_id='member-123'),
            Account(account_id='account-bcd', member_id='member-124'),
            Account(account_id='account-bce', member_id='member-124')
        ]

        assert db.electricity_bills == \
               TEST_PREPARE_DATABASE_DB_ELECTRICITY_BILLS

        assert db.gas_bills == TEST_PREPARE_DATABASE_DB_GAS_BILLS

    @pytest.mark.parametrize(
        ('member_id', 'account', 'bill_date', 'energy_source',
         'testing', 'expected_amount', 'expected_kwh'),
        (
            ('member-123', 'account-abc', '2017-03-31', 'electricity', True,
             25.81, 179),
            ('member-123', 'account-abc', '2017-04-30', 'electricity', True,
             34.68, 243),
            ('member-123', 'account-abc', '2017-05-31', 'electricity', True,
             42.09, 268),
            ('member-123', 'account-abc', '2017-06-30', 'electricity', True,
             32.43, 183),
            ('member-123', 'account-abc', '2017-07-31', 'electricity', True,
             27.57, 167),
            ('member-123', 'account-abc', '2017-08-31', 'electricity', True,
             9.86, 62),
            ('member-123', 'account-abc', '2017-09-30', 'electricity', True,
             38.19, 223),
            ('member-123', 'account-abc', '2017-10-31', 'electricity', True,
             31.24, 245),
            ('member-123', 'account-abc', '2017-11-30', 'electricity', True,
             57.85, 367),
            ('member-123', 'account-abc', '2017-12-31', 'electricity', True,
             34.33, 240),
            ('member-123', 'account-abc', '2018-01-31', 'electricity', True,
             46.42, 333),
            ('member-123', 'account-abc', '2018-02-28', 'electricity', True,
             27.87, 186),
            ('member-123', 'account-abc', '2018-03-31', 'electricity', True,
             50.01, 324),
        )
    )
    def test_calculate_and_print_bill(self, member_id: str, account: str,
                                      bill_date: str, energy_source: str,
                                      testing: bool, expected_amount: float,
                                      expected_kwh: int):
        """ Testing calculations and printing bill.

        :param str member_id: Customer provided as a parameter (optional),
            parametrised.
        :param str account: Account provided as a parameter  (optional),
            parametrised.
        :param str bill_date: Date of the bill provided as a parameter
            (optional), parametrised.
        :param str energy_source: Type of the billing, can be `electricity`
            or `gas`, parametrised.
        :param bool testing: Flag for testing, parametrised.
        :param float expected_amount: Calculated expected bill amount,
            parametrised.
        :param int expected_kwh: Calculated amount of kwh units, parametrised.
        """

        assert (expected_amount, expected_kwh) == calculate_and_print_bill(
            member_id=member_id,
            account=account,
            bill_date=bill_date,
            energy_source=energy_source,
            testing=testing
        )
