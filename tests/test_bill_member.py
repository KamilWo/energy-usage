import pytest

from app.bill_member import calculate_bill


class TestBillMember(object):

    @pytest.mark.parametrize(
        ('member_id', 'account_id', 'bill_date'),
        (
            ('member-123', 'ALL', '2017-08-31'),
            ('member-123', 'account-abc', '2017-09-30'),
            ('member-123', 'ALL', 'None'),
            ('member-123', 'account-abc', 'null'),
        )
    )
    def test_calculate_bill_for_august_2017(
        self,
        member_id,
        account_id,
        bill_date
    ):
        amount, kwh = calculate_bill(
            member_id=member_id,
            account_id=account_id,
            bill_date=bill_date
        )
        if bill_date == '2017-08-31':
            assert amount == 27.57
            assert kwh == 167
        if bill_date == '2017-09-31':
            assert amount == 0
            assert kwh == 0
        if bill_date == '2017-10-31':
            assert amount == 27.57
            assert kwh == 167
