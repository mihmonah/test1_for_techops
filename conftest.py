import pytest
from selenium import webdriver
import conv


@pytest.fixture(scope="function",
                params=conv.csv_to_args('input_data.csv')[1],
                ids=conv.csv_to_args('input_data.csv')[0])
def param_test_for_insert_convertation_sum(request):
"""
Fixture: generating of parameters for test_for_insert_convertation_sum
"""
    return request.param


@pytest.fixture(scope="function",
                params=conv.csv_to_args('input_dates.csv')[1],
                ids=conv.csv_to_args('input_dates.csv')[0])
def param_test_for_from_to_filter(request):
"""
Fixture: generating of parameters for test_from_to_filter
"""
    return request.param


@pytest.fixture(scope="function")
def resource_setup(request):
"""
Base fixture: openening FireFox webdriver, connecting to site for testing
and finalizer, which close driver and browser.
"""
    print("\nconnect to converter site")
    with pytest.allure.step('open Firefox webdriver and connect to converter site'):
        driver = webdriver.Firefox()
        driver.get("http://www.sberbank.ru/ru/quotes/converter")
    driver.implicitly_wait(30)

    def resource_teardown():
        driver.quit()
    request.addfinalizer(resource_teardown)
    return driver
