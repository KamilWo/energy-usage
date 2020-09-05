import pytest

from app.bill_member import prepare_database
from app.models import (
    Account,
    BillDatabase,
    ElectricityBill,
    GasBill,
    Member
)
from typing import Optional


class TestModels(object):
    """ Testing Models. """

    @pytest.mark.parametrize(
        ('member_id', 'name', 'accounts'),
        (
            ('member-123', 'member-123', []),
            ('member-123', '', [Account(
                account_id='account-abc',
                member_id='member-123'
            )]),
        )
    )
    def test_models(
        self,
        member_id: str,
        name: str,
        accounts: [Account]
    ):
        """ Testing models and their functions.

        :param str member_id: Member identifier, parametrised.
        :param str name: Member name, parametrised.
        :param [Account] accounts: Account model instances, parametrised.
        """

        test_member = Member(
            member_id=member_id,
            name=name,
            accounts=set()
        )
        assert test_member is not None
        assert test_member.member_id == member_id
        assert test_member.name == name

        db = BillDatabase(
            members={test_member},
            accounts=list(),
            electricity_bills={},
            gas_bills={}
        )
        for account in accounts:
            db.add_account(
                account=account
            )

        if accounts:
            assert len(db.get_member_accounts(
                member_id=member_id
            )) == len(accounts)

        test_account = Account(
            account_id='account-abc',
            member_id='member-123'
        )

        assert test_account.__hash__() == hash('account-abc_member-123')

        test_electricity_bill = ElectricityBill(
            member=test_member,
            account=test_account,
            bill_date='2017-08-31',
            units=0,
            total=0.0
        )

        assert test_electricity_bill.__hash__() == \
               hash('member-123_account-abc_2017-08-31')

        test_gas_bill = GasBill(
            member=test_member,
            account=test_account,
            bill_date='2017-08-31',
            units=0,
            total=0.0
        )

        assert test_gas_bill.__hash__() == \
               hash('member-123_account-abc_2017-08-31')

    @pytest.mark.parametrize(
        ('energy_source', 'member_id', 'account_id', 'given_date',
         'expected_total_amount', 'expected_units', 'all_accounts'),
        (
            ('electricity', 'member-123', 'account-abc', '2017-08-31',
             19.72, 124, 'ALL'),
            ('electricity', 'member-123', 'account-abc', '2017-08-31',
             9.86, 62, False),
            ('gas', 'member-123', 'account-abc', '2017-08-31', 12.58,
             124, 'ALL'),
            ('gas', 'member-123', 'account-abc', '2017-08-31', 6.29,
             62, False),
        )
    )
    def test_get_bills_amount(self, energy_source: str, member_id: str,
                              account_id: str, given_date: str,
                              expected_total_amount: float,
                              expected_units: int,
                              all_accounts: Optional[str]):
        """ Testing BilLDatabase.get_bills_amount method.
        :param str energy_source: Type of source of energy for which bill
            is being calculated, parametrised.
        :param str member_id: Member identifier, parametrised.
        :param str account_id: Account identifier, parametrised.
        :param str given_date: Specified date of the bill, parametrised.
        :param float expected_total_amount: Calculated total bill amount,
            parametrised.
        :param int expected_units: Calculated total units amount,
            parametrised.
        :param Optional[str] all_accounts: Provided flag for billing
            all accounts, parametrised.
        """

        db = prepare_database(data_source='test_readings.json')

        assert (expected_total_amount, expected_units) == db.get_bills_amount(
            energy_source=energy_source,
            member_id=member_id,
            account_id=account_id,
            given_date=given_date,
            all_accounts=all_accounts
        )
