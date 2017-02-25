from selenium.webdriver.common.by import By


class LeftMenuLocators(object):
    # convertation sum input field
    INSERT_FIELD = (By.CLASS_NAME, 'filter-block-line-right input')
    # button "Показать" from left menu
    BUTTON = (By.XPATH, "//div[@class='filter-block']//button")
    # "Вы получите" field
    RESULT = (By.CLASS_NAME, 'converter-result')


class RightMenuLocators(object):
    # first currency change menu
    FIST_CUR = (By.XPATH, "//div[@class='select']//strong")
    # visible list of currency
    CUR = [(By.XPATH, "//div[@class='visible']//span[1]"),
           (By.XPATH, "//div[@class='visible']//span[2]"),
           (By.XPATH, "//div[@class='visible']//span[3]"),
           (By.XPATH, "//div[@class='visible']//span[4]"),
           (By.XPATH, "//div[@class='visible']//span[5]"),
           (By.XPATH, "//div[@class='visible']//span[6]")]
    # button "Динамика изменения курсов"
    LEFT_TABLE = (
        By.XPATH, "//ul[@class='rates-tabs rates-right']//li[1]//span")
    # button "Расширенная таблица курсов"
    RIGHT_TABLE = (
        By.XPATH, "//ul[@class='rates-tabs rates-right']//li[2]//span")
    # date filter from
    FROM_FILTER = (By.NAME, 'filter-datepicker-details-from')
    # date filter to
    TO_FILTER = (By.NAME, 'filter-datepicker-details-to')
    # button "Показать" from right menu
    BUTTON = (
        By.XPATH,
        "//div[@class='rates-details-period-datepicker-line']//button")
    # captions to the x-axis
    X_DATA_FIELD = (By.CLASS_NAME, 'jqplot-axis.jqplot-xaxis')
