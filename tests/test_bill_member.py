import pytest

from app.bill_member import (
    calculate_bill,
    prepare_database,
    calculate_and_print_bill
)
from app.models import (
    Account,
    ElectricityBill,
    GasBill,
    Member,
)


class TestBillMember(object):

    @pytest.mark.parametrize(
        ('member_id', 'account_id', 'bill_date', 'energy_source',
         'expected_amount', 'expected_kwh'),
        (
            ('member-123', 'account-abc', '2017-07-31', 'electricity', 27.57, 167),
            ('member-123', 'ALL', '2017-07-31', 'electricity', 27.57, 167),
            ('member-123', 'ALL', '2017-08-31', 'electricity', 9.86, 62),
            ('member-123', 'account-abc', '2017-09-30', 'electricity', 38.19, 223),
            ('member-123', 'account-abc', '2017-10-31', 'electricity', 31.24, 245),
            ('member-123', 'ALL', '2017-10-31', 'electricity', 31.24, 245),
            ('member-123', 'account-abc', '2018-01-31', 'electricity', 46.42, 333),
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

        assert db.electricity_bills == {
            'member-123_account-abc_2017-03-31': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-03-31', units=179,
                total=25.81, billing_type='electricity'),
            'member-123_account-abc_2017-04-30': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-04-30', units=243,
                total=34.68, billing_type='electricity'),
            'member-123_account-abc_2017-05-31': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-05-31', units=268,
                total=42.09, billing_type='electricity'),
            'member-123_account-abc_2017-06-30': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-06-30', units=183,
                total=32.43, billing_type='electricity'),
            'member-123_account-abc_2017-07-31': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-07-31', units=167,
                total=27.57, billing_type='electricity'),
            'member-123_account-abc_2017-08-31': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-08-31', units=62,
                total=9.86, billing_type='electricity'),
            'member-123_account-abc_2017-09-30': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-09-30', units=223,
                total=38.19, billing_type='electricity'),
            'member-123_account-abc_2017-10-31': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-10-31', units=245,
                total=31.24, billing_type='electricity'),
            'member-123_account-abc_2017-11-30': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-11-30', units=367,
                total=57.85, billing_type='electricity'),
            'member-123_account-abc_2017-12-31': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-12-31', units=240,
                total=34.33, billing_type='electricity'),
            'member-123_account-abc_2018-01-31': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2018-01-31', units=333,
                total=46.42, billing_type='electricity'),
            'member-123_account-abc_2018-02-28': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2018-02-28', units=186,
                total=27.87, billing_type='electricity'),
            'member-123_account-abc_2018-03-31': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2018-03-31', units=324,
                total=50.01, billing_type='electricity'),
            'member-123_account-abd_2017-03-31': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-03-31', units=179,
                total=25.81, billing_type='electricity'),
            'member-123_account-abd_2017-04-30': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-04-30', units=243,
                total=34.68, billing_type='electricity'),
            'member-123_account-abd_2017-05-31': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-05-31', units=268,
                total=42.09, billing_type='electricity'),
            'member-123_account-abd_2017-06-30': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-06-30', units=183,
                total=32.43, billing_type='electricity'),
            'member-123_account-abd_2017-07-31': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-07-31', units=167,
                total=27.57, billing_type='electricity'),
            'member-123_account-abd_2017-08-31': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-08-31', units=62,
                total=9.86, billing_type='electricity'),
            'member-123_account-abd_2017-09-30': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-09-30', units=223,
                total=38.19, billing_type='electricity'),
            'member-123_account-abd_2017-10-31': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-10-31', units=245,
                total=31.24, billing_type='electricity'),
            'member-123_account-abd_2017-11-30': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-11-30', units=367,
                total=57.85, billing_type='electricity'),
            'member-123_account-abd_2017-12-31': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-12-31', units=240,
                total=34.33, billing_type='electricity'),
            'member-123_account-abd_2018-01-31': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2018-01-31', units=333,
                total=46.42, billing_type='electricity'),
            'member-123_account-abd_2018-02-28': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2018-02-28', units=186,
                total=27.87, billing_type='electricity'),
            'member-123_account-abd_2018-03-31': ElectricityBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2018-03-31', units=324,
                total=50.01, billing_type='electricity'),
            'member-124_account-bcd_2017-03-31': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-03-31', units=179,
                total=25.81, billing_type='electricity'),
            'member-124_account-bcd_2017-04-30': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-04-30', units=243,
                total=34.68, billing_type='electricity'),
            'member-124_account-bcd_2017-05-31': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-05-31', units=268,
                total=42.09, billing_type='electricity'),
            'member-124_account-bcd_2017-06-30': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-06-30', units=183,
                total=32.43, billing_type='electricity'),
            'member-124_account-bcd_2017-07-31': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-07-31', units=167,
                total=27.57, billing_type='electricity'),
            'member-124_account-bcd_2017-08-31': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-08-31', units=62,
                total=9.86, billing_type='electricity'),
            'member-124_account-bcd_2017-09-30': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-09-30', units=223,
                total=38.19, billing_type='electricity'),
            'member-124_account-bcd_2017-10-31': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-10-31', units=245,
                total=31.24, billing_type='electricity'),
            'member-124_account-bcd_2017-11-30': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-11-30', units=367,
                total=57.85, billing_type='electricity'),
            'member-124_account-bcd_2017-12-31': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-12-31', units=240,
                total=34.33, billing_type='electricity'),
            'member-124_account-bcd_2018-01-31': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2018-01-31', units=333,
                total=46.42, billing_type='electricity'),
            'member-124_account-bcd_2018-02-28': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2018-02-28', units=186,
                total=27.87, billing_type='electricity'),
            'member-124_account-bcd_2018-03-31': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2018-03-31', units=324,
                total=50.01, billing_type='electricity'),
            'member-124_account-bce_2017-03-31': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-03-31', units=179,
                total=25.81, billing_type='electricity'),
            'member-124_account-bce_2017-04-30': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-04-30', units=243,
                total=34.68, billing_type='electricity'),
            'member-124_account-bce_2017-05-31': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-05-31', units=268,
                total=42.09, billing_type='electricity'),
            'member-124_account-bce_2017-06-30': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-06-30', units=183,
                total=32.43, billing_type='electricity'),
            'member-124_account-bce_2017-07-31': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-07-31', units=167,
                total=27.57, billing_type='electricity'),
            'member-124_account-bce_2017-08-31': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-08-31', units=62,
                total=9.86, billing_type='electricity'),
            'member-124_account-bce_2017-09-30': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-09-30', units=223,
                total=38.19, billing_type='electricity'),
            'member-124_account-bce_2017-10-31': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-10-31', units=245,
                total=31.24, billing_type='electricity'),
            'member-124_account-bce_2017-11-30': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-11-30', units=367,
                total=57.85, billing_type='electricity'),
            'member-124_account-bce_2017-12-31': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-12-31', units=240,
                total=34.33, billing_type='electricity'),
            'member-124_account-bce_2018-01-31': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2018-01-31', units=333,
                total=46.42, billing_type='electricity'),
            'member-124_account-bce_2018-02-28': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2018-02-28', units=186,
                total=27.87, billing_type='electricity'),
            'member-124_account-bce_2018-03-31': ElectricityBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2018-03-31', units=324,
                total=50.01, billing_type='electricity')}

        assert db.gas_bills == {
            'member-123_account-abc_2017-03-31': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-03-31', units=179,
                total=11.47, billing_type='gas'),
            'member-123_account-abc_2017-04-30': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-04-30', units=243,
                total=17.34, billing_type='gas'),
            'member-123_account-abc_2017-05-31': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-05-31', units=268,
                total=17.8, billing_type='gas'),
            'member-123_account-abc_2017-06-30': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-06-30', units=183,
                total=17.51, billing_type='gas'),
            'member-123_account-abc_2017-07-31': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-07-31', units=167,
                total=13.96, billing_type='gas'),
            'member-123_account-abc_2017-08-31': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-08-31', units=62,
                total=6.29, billing_type='gas'),
            'member-123_account-abc_2017-09-30': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-09-30', units=223,
                total=18.54, billing_type='gas'),
            'member-123_account-abc_2017-10-31': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-10-31', units=245,
                total=15.7, billing_type='gas'),
            'member-123_account-abc_2017-11-30': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-11-30', units=367,
                total=23.52, billing_type='gas'),
            'member-123_account-abc_2017-12-31': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2017-12-31', units=240,
                total=15.75, billing_type='gas'),
            'member-123_account-abc_2018-01-31': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2018-01-31', units=333,
                total=19.04, billing_type='gas'),
            'member-123_account-abc_2018-02-28': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2018-02-28', units=186,
                total=12.47, billing_type='gas'),
            'member-123_account-abc_2018-03-31': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abc', member_id='member-123'), bill_date='2018-03-31', units=324,
                total=22.14, billing_type='gas'),
            'member-123_account-abd_2017-03-31': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-03-31', units=179,
                total=11.47, billing_type='gas'),
            'member-123_account-abd_2017-04-30': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-04-30', units=243,
                total=17.34, billing_type='gas'),
            'member-123_account-abd_2017-05-31': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-05-31', units=268,
                total=17.8, billing_type='gas'),
            'member-123_account-abd_2017-06-30': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-06-30', units=183,
                total=17.51, billing_type='gas'),
            'member-123_account-abd_2017-07-31': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-07-31', units=167,
                total=13.96, billing_type='gas'),
            'member-123_account-abd_2017-08-31': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-08-31', units=62,
                total=6.29, billing_type='gas'),
            'member-123_account-abd_2017-09-30': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-09-30', units=223,
                total=18.54, billing_type='gas'),
            'member-123_account-abd_2017-10-31': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-10-31', units=245,
                total=15.7, billing_type='gas'),
            'member-123_account-abd_2017-11-30': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-11-30', units=367,
                total=23.52, billing_type='gas'),
            'member-123_account-abd_2017-12-31': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2017-12-31', units=240,
                total=15.75, billing_type='gas'),
            'member-123_account-abd_2018-01-31': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2018-01-31', units=333,
                total=19.04, billing_type='gas'),
            'member-123_account-abd_2018-02-28': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2018-02-28', units=186,
                total=12.47, billing_type='gas'),
            'member-123_account-abd_2018-03-31': GasBill(
                member=Member(member_id='member-123', accounts=set(), name='member-123'),
                account=Account(account_id='account-abd', member_id='member-123'), bill_date='2018-03-31', units=324,
                total=22.14, billing_type='gas'),
            'member-124_account-bcd_2017-03-31': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-03-31', units=179,
                total=11.47, billing_type='gas'),
            'member-124_account-bcd_2017-04-30': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-04-30', units=243,
                total=17.34, billing_type='gas'),
            'member-124_account-bcd_2017-05-31': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-05-31', units=268,
                total=17.8, billing_type='gas'),
            'member-124_account-bcd_2017-06-30': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-06-30', units=183,
                total=17.51, billing_type='gas'),
            'member-124_account-bcd_2017-07-31': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-07-31', units=167,
                total=13.96, billing_type='gas'),
            'member-124_account-bcd_2017-08-31': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-08-31', units=62,
                total=6.29, billing_type='gas'),
            'member-124_account-bcd_2017-09-30': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-09-30', units=223,
                total=18.54, billing_type='gas'),
            'member-124_account-bcd_2017-10-31': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-10-31', units=245,
                total=15.7, billing_type='gas'),
            'member-124_account-bcd_2017-11-30': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-11-30', units=367,
                total=23.52, billing_type='gas'),
            'member-124_account-bcd_2017-12-31': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2017-12-31', units=240,
                total=15.75, billing_type='gas'),
            'member-124_account-bcd_2018-01-31': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2018-01-31', units=333,
                total=19.04, billing_type='gas'),
            'member-124_account-bcd_2018-02-28': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2018-02-28', units=186,
                total=12.47, billing_type='gas'),
            'member-124_account-bcd_2018-03-31': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bcd', member_id='member-124'), bill_date='2018-03-31', units=324,
                total=22.14, billing_type='gas'),
            'member-124_account-bce_2017-03-31': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-03-31', units=179,
                total=11.47, billing_type='gas'),
            'member-124_account-bce_2017-04-30': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-04-30', units=243,
                total=17.34, billing_type='gas'),
            'member-124_account-bce_2017-05-31': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-05-31', units=268,
                total=17.8, billing_type='gas'),
            'member-124_account-bce_2017-06-30': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-06-30', units=183,
                total=17.51, billing_type='gas'),
            'member-124_account-bce_2017-07-31': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-07-31', units=167,
                total=13.96, billing_type='gas'),
            'member-124_account-bce_2017-08-31': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-08-31', units=62,
                total=6.29, billing_type='gas'),
            'member-124_account-bce_2017-09-30': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-09-30', units=223,
                total=18.54, billing_type='gas'),
            'member-124_account-bce_2017-10-31': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-10-31', units=245,
                total=15.7, billing_type='gas'),
            'member-124_account-bce_2017-11-30': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-11-30', units=367,
                total=23.52, billing_type='gas'),
            'member-124_account-bce_2017-12-31': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2017-12-31', units=240,
                total=15.75, billing_type='gas'),
            'member-124_account-bce_2018-01-31': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2018-01-31', units=333,
                total=19.04, billing_type='gas'),
            'member-124_account-bce_2018-02-28': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2018-02-28', units=186,
                total=12.47, billing_type='gas'),
            'member-124_account-bce_2018-03-31': GasBill(
                member=Member(member_id='member-124', accounts=set(), name='member-124'),
                account=Account(account_id='account-bce', member_id='member-124'), bill_date='2018-03-31', units=324,
                total=22.14, billing_type='gas')}

    @pytest.mark.parametrize(
        ('member_id', 'account', 'bill_date', 'energy_source',
         'testing', 'expected_amount', 'expected_kwh'),
        (
            ('member-123', 'account-abc', '2017-03-31', 'electricity', True, 25.81, 179),
            ('member-123', 'account-abc', '2017-04-30', 'electricity', True, 34.68, 243),
            ('member-123', 'account-abc', '2017-05-31', 'electricity', True, 42.09, 268),
            ('member-123', 'account-abc', '2017-06-30', 'electricity', True, 32.43, 183),
            ('member-123', 'account-abc', '2017-07-31', 'electricity', True, 27.57, 167),
            ('member-123', 'account-abc', '2017-08-31', 'electricity', True, 9.86, 62),
            ('member-123', 'account-abc', '2017-09-30', 'electricity', True, 38.19, 223),
            ('member-123', 'account-abc', '2017-10-31', 'electricity', True, 31.24, 245),
            ('member-123', 'account-abc', '2017-11-30', 'electricity', True, 57.85, 367),
            ('member-123', 'account-abc', '2017-12-31', 'electricity', True, 34.33, 240),
            ('member-123', 'account-abc', '2018-01-31', 'electricity', True, 46.42, 333),
            ('member-123', 'account-abc', '2018-02-28', 'electricity', True, 27.87, 186),
            ('member-123', 'account-abc', '2018-03-31', 'electricity', True, 50.01, 324),
        )
    )
    def test_calculate_and_print_bill(self, member_id: str, account: str,
                                      bill_date: str, energy_source: str,
                                      testing: bool, expected_amount: float,
                                      expected_kwh: int):
        """ """

        assert (expected_amount, expected_kwh) == calculate_and_print_bill(
            member_id=member_id,
            account=account,
            bill_date=bill_date,
            energy_source=energy_source,
            testing=testing
        )
