import pytest
import allure
from menues import RightMenu


@allure.feature('Test: "input data to filters"')
def test_input_data_to_filters(resource_setup, param_test_for_from_to_filter):
    """
    In this test case we check that at least one input date
    is the same as date on captions to the x-axis.
    """
    (data_from, data_to) = param_test_for_from_to_filter
    assert RightMenu.check_from_to_filters(resource_setup, data_from, data_to)
