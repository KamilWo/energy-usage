import datetime
import pytest

from app.models import (
    Account,
    BillDatabase,
    Member,
    ElectricityBill,
    GasBill
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
    def test_member_accounts(
        self,
        member_id,
        name,
        accounts
    ):
        member = Member(
            member_id=member_id,
            name=name,
            accounts=set()
        )
        assert member is not None
        assert member.member_id == member_id
        assert member.name == name

        db = BillDatabase(
            members={member},
            accounts=dict(),
            electricity_bills={},
            gas_bills={}
        )
        for account in accounts:
            db.add_account_for_member(
                member_id=member_id,
                account=account
            )

        print(db.get_member_accounts(
            member_id=member_id
        ))
        if accounts:
            assert len(db.get_member_accounts(
                member_id=member_id
            )) == len(accounts)
