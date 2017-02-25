import pytest
import allure
from menues import LeftMenu


@pytest.mark.parametrize("input_currency",
                         [(0, "RUR"), (1, "CHF"), (2, "EUR"),
                          (3, "GBP"), (4, "JPY"), (5, "USD")],
                         ids=["RUR", "CHF", "EUR", "GBP", "JPY", "USD"])
@allure.feature('Test: "find currency"')
def test_find_currency(resource_setup, input_currency):
    """
    In this test case we check that chosen currency doesn't change
    after clicking between tables "Динамика изменения курсов"
    and "Расширенная таблица курсов".
    """
    (i_c, i_c_n) = input_currency
    assert LeftMenu.check_find_currency(resource_setup, i_c, i_c_n)
