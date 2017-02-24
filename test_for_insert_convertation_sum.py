import pytest
import allure
from menues import LeftMenu


@allure.feature('Test: "insert convertation sum"')
def test_insert_convertation_sum(resource_setup, param_test_for_insert_convertation_sum):
"""
In this test case we check that insert to "Сумма" field sum
is the same as sum if fileld "Вы получите" after clicking "Показать" button.
"""
    (sum_in, sum_out) = param_test_for_insert_convertation_sum
    assert LeftMenu.check_insert_convertation_sum(
        resource_setup, sum_in, sum_out)
