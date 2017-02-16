import pytest
import time
from selenium.webdriver.common.keys import Keys
import allure


@allure.feature('Test: "input data to filters"')
def test_input_data_to_filters(resource_setup, param_test_for_from_to_filter):
    with pytest.allure.step('getting parameters for test'):
        (data_from, data_to) = param_test_for_from_to_filter
    with pytest.allure.step('input data from'):
        filter_from = resource_setup.find_element_by_name('filter-datepicker-details-from')
        filter_from.clear()
        filter_from.send_keys(data_from)
        filter_from.send_keys(Keys.RETURN)
    with pytest.allure.step('input data to'):
        filter_to = resource_setup.find_element_by_name('filter-datepicker-details-to')
        filter_to.clear()
        filter_to.send_keys(data_to)
        filter_to.send_keys(Keys.RETURN)
    with pytest.allure.step('click "Показать" button'):
        resource_setup.find_element_by_xpath("//div[@class='rates-details-period-datepicker-line']//button").click()
    time.sleep(4)
    with pytest.allure.step('checking results of click "Показать" button'):
        try:
            resource_setup.find_element_by_xpath("//div[@class='jqplot-axis jqplot-xaxis']//div")
        except Exception as e:
            print("Input data is incorrect", format(e))
            assert 0
        finally:
            assert 1
