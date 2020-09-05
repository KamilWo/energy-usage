import pytest

from app.models import (
    Account,
    BillDatabase,
    ElectricityBill,
    GasBill,
    Member,
)

# TODO: write more tests


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
