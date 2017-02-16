import pytest
import time
import allure


@allure.feature('Test: "insert convertation sum"')
def test_insert_convertation_sum(resource_setup, param_test_for_insert_convertation_sum):
    with pytest.allure.step('find window for inserting conversation sum and clear its content'):
        time.sleep(2)
        filter = resource_setup.find_element_by_class_name('filter-block-line-right input')
        filter.clear()
        time.sleep(2)
    with pytest.allure.step('getting parameters for test and insert it to conversation window'):
        (input, expected_output) = param_test_for_insert_convertation_sum
        filter.send_keys(input)
        resource_setup.find_element_by_xpath("//div[@class='filter-block']//button").click()
    time.sleep(3)
    with pytest.allure.step('getting result from "Вы получите" window'):
        resource_setup.find_element_by_class_name('converter-result')
        res = resource_setup.find_element_by_class_name('converter-result')
        a = res.text
        b = a.split('\n')[1]
        result = b[:b.find('R')]
    with pytest.allure.step('comparison input and output data'):
        assert result == expected_output
