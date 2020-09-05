# flake8: noqa

from app.models import (
    Account,
    ElectricityBill,
    GasBill,
    Member,
)

TEST_PREPARE_DATABASE_DB_ELECTRICITY_BILLS = {
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

TEST_PREPARE_DATABASE_DB_GAS_BILLS = {
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

TEST_LOAD_READINGS_DB_GET_READINGS_ORIGINAL = {
    "member-123": [
        {
            "account-abc": [
                {
                    "electricity": [
                        {
                            "cumulative": 17580,
                            "readingDate": "2017-03-28T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 17759,
                            "readingDate": "2017-04-15T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18002,
                            "readingDate": "2017-05-08T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18270,
                            "readingDate": "2017-06-18T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18453,
                            "readingDate": "2017-07-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18620,
                            "readingDate": "2017-08-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18682,
                            "readingDate": "2017-09-10T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18905,
                            "readingDate": "2017-10-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 19150,
                            "readingDate": "2017-11-04T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 19517,
                            "readingDate": "2017-12-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 19757,
                            "readingDate": "2018-01-23T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 20090,
                            "readingDate": "2018-02-19T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 20276,
                            "readingDate": "2018-03-14T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 20600,
                            "readingDate": "2018-04-29T00:00:00.000Z",
                            "unit": "kWh"
                        }
                    ]
                }
            ]
        }
    ]
}

TEST_LOAD_READINGS_DB_GET_READINGS_CUSTOM = {
    "member-123": [
        {
            "account-abc": [
                {
                    "electricity": [
                        {
                            "cumulative": 17580,
                            "readingDate": "2017-03-28T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 17759,
                            "readingDate": "2017-04-15T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18002,
                            "readingDate": "2017-05-08T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18270,
                            "readingDate": "2017-06-18T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18453,
                            "readingDate": "2017-07-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18620,
                            "readingDate": "2017-08-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18682,
                            "readingDate": "2017-09-10T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18905,
                            "readingDate": "2017-10-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 19150,
                            "readingDate": "2017-11-04T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 19517,
                            "readingDate": "2017-12-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 19757,
                            "readingDate": "2018-01-23T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 20090,
                            "readingDate": "2018-02-19T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 20276,
                            "readingDate": "2018-03-14T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 20600,
                            "readingDate": "2018-04-29T00:00:00.000Z",
                            "unit": "kWh"
                        }
                    ]
                },
                {
                    "gas": [
                        {
                            "cumulative": 37580,
                            "readingDate": "2017-03-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 37759,
                            "readingDate": "2017-04-15T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38002,
                            "readingDate": "2017-05-18T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38270,
                            "readingDate": "2017-06-18T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38453,
                            "readingDate": "2017-07-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38620,
                            "readingDate": "2017-08-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38682,
                            "readingDate": "2017-09-16T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38905,
                            "readingDate": "2017-10-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 39150,
                            "readingDate": "2017-11-22T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 39517,
                            "readingDate": "2017-12-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 39757,
                            "readingDate": "2018-01-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 40090,
                            "readingDate": "2018-02-22T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 40276,
                            "readingDate": "2018-03-16T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 40600,
                            "readingDate": "2018-04-25T00:00:00.000Z",
                            "unit": "kWh"
                        }
                    ]
                }
            ],
            "account-abd": [
                {
                    "electricity": [
                        {
                            "cumulative": 17580,
                            "readingDate": "2017-03-28T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 17759,
                            "readingDate": "2017-04-15T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18002,
                            "readingDate": "2017-05-08T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18270,
                            "readingDate": "2017-06-18T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18453,
                            "readingDate": "2017-07-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18620,
                            "readingDate": "2017-08-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18682,
                            "readingDate": "2017-09-10T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18905,
                            "readingDate": "2017-10-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 19150,
                            "readingDate": "2017-11-04T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 19517,
                            "readingDate": "2017-12-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 19757,
                            "readingDate": "2018-01-23T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 20090,
                            "readingDate": "2018-02-19T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 20276,
                            "readingDate": "2018-03-14T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 20600,
                            "readingDate": "2018-04-29T00:00:00.000Z",
                            "unit": "kWh"
                        }
                    ]
                },
                {
                    "gas": [
                        {
                            "cumulative": 37580,
                            "readingDate": "2017-03-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 37759,
                            "readingDate": "2017-04-15T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38002,
                            "readingDate": "2017-05-18T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38270,
                            "readingDate": "2017-06-18T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38453,
                            "readingDate": "2017-07-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38620,
                            "readingDate": "2017-08-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38682,
                            "readingDate": "2017-09-16T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38905,
                            "readingDate": "2017-10-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 39150,
                            "readingDate": "2017-11-22T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 39517,
                            "readingDate": "2017-12-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 39757,
                            "readingDate": "2018-01-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 40090,
                            "readingDate": "2018-02-22T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 40276,
                            "readingDate": "2018-03-16T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 40600,
                            "readingDate": "2018-04-25T00:00:00.000Z",
                            "unit": "kWh"
                        }
                    ]
                }
            ]
        }
    ],
    "member-124": [
        {
            "account-bcd": [
                {
                    "electricity": [
                        {
                            "cumulative": 17580,
                            "readingDate": "2017-03-28T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 17759,
                            "readingDate": "2017-04-15T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18002,
                            "readingDate": "2017-05-08T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18270,
                            "readingDate": "2017-06-18T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18453,
                            "readingDate": "2017-07-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18620,
                            "readingDate": "2017-08-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18682,
                            "readingDate": "2017-09-10T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18905,
                            "readingDate": "2017-10-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 19150,
                            "readingDate": "2017-11-04T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 19517,
                            "readingDate": "2017-12-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 19757,
                            "readingDate": "2018-01-23T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 20090,
                            "readingDate": "2018-02-19T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 20276,
                            "readingDate": "2018-03-14T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 20600,
                            "readingDate": "2018-04-29T00:00:00.000Z",
                            "unit": "kWh"
                        }
                    ]
                },
                {
                    "gas": [
                        {
                            "cumulative": 37580,
                            "readingDate": "2017-03-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 37759,
                            "readingDate": "2017-04-15T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38002,
                            "readingDate": "2017-05-18T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38270,
                            "readingDate": "2017-06-18T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38453,
                            "readingDate": "2017-07-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38620,
                            "readingDate": "2017-08-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38682,
                            "readingDate": "2017-09-16T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38905,
                            "readingDate": "2017-10-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 39150,
                            "readingDate": "2017-11-22T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 39517,
                            "readingDate": "2017-12-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 39757,
                            "readingDate": "2018-01-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 40090,
                            "readingDate": "2018-02-22T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 40276,
                            "readingDate": "2018-03-16T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 40600,
                            "readingDate": "2018-04-25T00:00:00.000Z",
                            "unit": "kWh"
                        }
                    ]
                }
            ],
            "account-bce": [
                {
                    "electricity": [
                        {
                            "cumulative": 17580,
                            "readingDate": "2017-03-28T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 17759,
                            "readingDate": "2017-04-15T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18002,
                            "readingDate": "2017-05-08T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18270,
                            "readingDate": "2017-06-18T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18453,
                            "readingDate": "2017-07-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18620,
                            "readingDate": "2017-08-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18682,
                            "readingDate": "2017-09-10T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 18905,
                            "readingDate": "2017-10-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 19150,
                            "readingDate": "2017-11-04T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 19517,
                            "readingDate": "2017-12-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 19757,
                            "readingDate": "2018-01-23T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 20090,
                            "readingDate": "2018-02-19T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 20276,
                            "readingDate": "2018-03-14T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 20600,
                            "readingDate": "2018-04-29T00:00:00.000Z",
                            "unit": "kWh"
                        }
                    ]
                },
                {
                    "gas": [
                        {
                            "cumulative": 37580,
                            "readingDate": "2017-03-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 37759,
                            "readingDate": "2017-04-15T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38002,
                            "readingDate": "2017-05-18T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38270,
                            "readingDate": "2017-06-18T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38453,
                            "readingDate": "2017-07-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38620,
                            "readingDate": "2017-08-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38682,
                            "readingDate": "2017-09-16T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 38905,
                            "readingDate": "2017-10-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 39150,
                            "readingDate": "2017-11-22T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 39517,
                            "readingDate": "2017-12-31T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 39757,
                            "readingDate": "2018-01-27T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 40090,
                            "readingDate": "2018-02-22T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 40276,
                            "readingDate": "2018-03-16T00:00:00.000Z",
                            "unit": "kWh"
                        },
                        {
                            "cumulative": 40600,
                            "readingDate": "2018-04-25T00:00:00.000Z",
                            "unit": "kWh"
                        }
                    ]
                }
            ]
        }
    ]
}
