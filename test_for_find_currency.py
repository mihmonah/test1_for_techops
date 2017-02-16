import pytest
import allure


@pytest.mark.parametrize("input_currency", [(1, "RUR"), (2, "CHF"), (3, "EUR"), (4, "GBP"), (5, "JPY"), (6, "USD")],
                         ids=["RUR", "CHF", "EUR", "GBP", "JPY", "USD"])
@allure.feature('Test: "find currency"')
def test_find_currency(resource_setup, input_currency):
    with pytest.allure.step('getting parameters for test'):
        (cur, cur_name) = input_currency
    with pytest.allure.step('open first select currency element and change it to currancy from parameters'):
        resource_setup.find_element_by_xpath("//div[@class='select']//strong").click()
        resource_setup.find_element_by_xpath("//div[@class='visible']//span[%d]" % cur).click()
    with pytest.allure.step('click to "Расширенная таблица курсов" button'):
        table = resource_setup.find_element_by_xpath("//ul[@class='rates-tabs rates-right']//li[2]//span")
        table.click()
    resource_setup.implicitly_wait(30)
    with pytest.allure.step('click to "Динамика изменения курсов" button'):
        resource_setup.find_element_by_xpath("//ul[@class='rates-tabs rates-right']//li[1]//span").click()
    resource_setup.implicitly_wait(30)
    with pytest.allure.step('comparison input currancy and currancy after clicking buttons'):
        assert resource_setup.find_element_by_xpath("//div[@class='select']//strong").text == cur_name
