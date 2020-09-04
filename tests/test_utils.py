import pytest

from app.utils import (
    apply_tariff,
    count_month_days,
    end_of_month_date
)
from datetime import date


class TestUtils(object):
    """ Testing Utils. """

    @pytest.mark.parametrize(
        ('energy_source', 'units', 'amount_of_days', 'expected_total_amount'),
        (
            ('electricity', 10.0, 10, 3.65),
            ('electricity', 50.5, 15, 9.72),
            ('electricity', 100.0, 24, 17.84),
            ('electricity', 150.2, 30, 25.32),
            ('gas', 10.0, 10, 2.84),
            ('gas', 20.3, 12, 3.72),
            ('gas', 42.5, 14, 5.05),
            ('gas', 60.0, 20, 7.19),
            ('gas', 300.0, 31, 19.01),
        )
    )
    def test_apply_tariff(self, energy_source: str, units: float,
                          amount_of_days: int, expected_total_amount: float):
        """ Testing Apply Tariff method, which is used to
        calculate total bill amount in £ and adds standard_charge.

        :param str energy_source: Can be `electricity` or `gas`, parametrised.
        :param float units: Number of units in the current month, parametrised.
        :param int amount_of_days: Number of days calculated as delta
            between readings, parametrised.
        :param float expected_total_amount: Calculated and expected total
            bill amount, parametrised.
        """
        total_bill_amount = apply_tariff(
            energy_source=energy_source,
            units=units,
            amount_of_days=amount_of_days
        )
        assert total_bill_amount == expected_total_amount

    @pytest.mark.parametrize(
        ('given_date', 'expected_count'),
        (
            ('2017-08-31', 31),
        )
    )
    def test_count_month_days(self, given_date: str, expected_count: int):
        """ Testing counting days in a month and returning the amount.

        Based on a given_date, tested function should return amount of days.

        :param str given_date: Given date in a string format %Y-%m-%d,
            parametrised.
        :param int expected_count: Amount of days in a month, parametrised.
        """
        assert count_month_days(given_date=given_date) == expected_count

    @pytest.mark.parametrize(
        ('given_date', 'expected_eom_date'),
        (
            ('2017-01-10', '2017-01-31'),
            ('2017-02-11', '2017-02-28'),
            ('2017-03-25', '2017-03-31'),
            ('2017-04-13', '2017-04-30'),
            ('2017-05-31', '2017-05-31'),
        )
    )
    def test_end_of_month_date(self, given_date: str, expected_eom_date: str):
        """ Testing end of the month date.

        :param str given_date: Given date in a string format %Y-%m-%d,
            parametrised.
        :param str expected_eom_date: Expected date %Y-%m-%d, parametrised.
        """
        assert end_of_month_date(given_date=given_date) == \
               date.fromisoformat(expected_eom_date)
