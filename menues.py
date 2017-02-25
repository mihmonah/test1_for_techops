import pytest
import time
from selenium.webdriver.common.keys import Keys
import allure
from selenium.webdriver.common.by import By
from locators import *


class LeftMenu(object):
    """
    Testing area divided into 2 areas. This class contains 2 implementations of test cases
    for testing LeftMenu (white window with word "Конвертация").
    """
    def check_insert_convertation_sum(resource, input_sum, correct_sum):
        """
        This function inputs convertation sum to "Сумма" field
	    and clicks "Показать" button. After that we try to find "Вы получите"
        field and get sum value from it. Result of function is 1 if
        sum value is same as expected value corresponding to input data.
        """
        result = '---'
        with pytest.allure.step('find window for inserting conversation sum and clear its content'):
            time.sleep(2)
            filter = resource.find_element(*LeftMenuLocators.INSERT_FIELD)
            filter.clear()
            time.sleep(2)
        with pytest.allure.step('getting parameters for test and insert it to conversation window'):
            input = input_sum
            expected_output = correct_sum
            filter.send_keys(input)
            resource.find_element(*LeftMenuLocators.BUTTON).click()
            time.sleep(3)
        with pytest.allure.step('getting result from "Вы получите" window'):
            try:
                b = resource.find_element(
                    *LeftMenuLocators.RESULT).text.split('\n')[1]
                result = b[:b.find('R')]
            except Exception as e:
                print("Input data is incorrect", format(e))
        with pytest.allure.step('comparison input and output data'):
            return result == expected_output

    def check_find_currency(resource, input_cur, input_cur_name):
        """
        This function clicks on "Из" currency, and selects one from list of currancy.
        After that it clicks on button "Расширенная таблица курсов" and button
        "Динамика изменения курсов" and checks value of "Из" currency.
        Result of function is 1 if selected currency doesn't change after clicks.
        """
        with pytest.allure.step('getting parameters for test'):
            cur = input_cur
            cur_name = input_cur_name
        with pytest.allure.step('open first select currency element and change it to currancy from parameters'):
            resource.find_element(*RightMenuLocators.FIST_CUR).click()
            resource.find_element(*RightMenuLocators.CUR[cur]).click()
        with pytest.allure.step('click to "Расширенная таблица курсов" button'):
            resource.find_element(*RightMenuLocators.RIGHT_TABLE).click()
            resource.implicitly_wait(30)
        with pytest.allure.step('click to "Динамика изменения курсов" button'):
            resource.find_element(*RightMenuLocators.LEFT_TABLE).click()
            resource.implicitly_wait(30)
        with pytest.allure.step('comparison input currancy and currancy after clicking buttons'):
            return resource.find_element(*RightMenuLocators.FIST_CUR).text == cur_name


class RightMenu(object):
    """
    Testing area divided into 2 areas. This class contains implementation of test cases
    for testing RightMenu (everything to the right of the LeftMenu).
    """
    def check_from_to_filters(resource, from_filt, to_filt):
        """
        This function inputs from/to dates to "С" and "По" filters
	    and clicks "Показать" button. After that we try to find x-axis
        currency plot. Result of function is 1 if first caption is same
        as from date, or if last caption is same as to date.
        """
        xaxis = [0, 0]
        with pytest.allure.step('getting parameters for test'):
            data_from = from_filt
            data_to = to_filt
        time.sleep(4)
        with pytest.allure.step('input data from'):
            filter_from = resource.find_element(*RightMenuLocators.FROM_FILTER)
            filter_from.clear()
            filter_from.send_keys(data_from)
            filter_from.send_keys(Keys.RETURN)
        with pytest.allure.step('input data to'):
            filter_to = resource.find_element(*RightMenuLocators.TO_FILTER)
            filter_to.clear()
            filter_to.send_keys(data_to)
            filter_to.send_keys(Keys.RETURN)
        with pytest.allure.step('click "Показать" button'):
            resource.find_element(*RightMenuLocators.BUTTON).click()
        time.sleep(4)
        try:
            xaxis = resource.find_element(
                *RightMenuLocators.X_DATA_FIELD).text.split('\n')
        except Exception as e:
            print("Input data is incorrect", format(e))
        return data_from == xaxis[0] or data_to == xaxis[-1]
