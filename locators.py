from selenium.webdriver.common.by import By


class LeftMenuLocators(object):
    INSERT_FIELD    = (By.CLASS_NAME, 'filter-block-line-right input')                            # convertation sum input field
    BUTTON          = (By.XPATH, "//div[@class='filter-block']//button")                          # button "Показать" from left menu
    RESULT          = (By.CLASS_NAME, 'converter-result')                                         # "Вы получите" field

class RightMenuLocators(object):
    FIST_CUR        = (By.XPATH, "//div[@class='select']//strong")                                # first currency change menu
    CUR             = [(By.XPATH, "//div[@class='visible']//span[1]"),                            # visible list of currency
                       (By.XPATH, "//div[@class='visible']//span[2]"),
					   (By.XPATH, "//div[@class='visible']//span[3]"),
					   (By.XPATH, "//div[@class='visible']//span[4]"),
					   (By.XPATH, "//div[@class='visible']//span[5]"),
					   (By.XPATH, "//div[@class='visible']//span[6]")]
    LEFT_TABLE      = (By.XPATH, "//ul[@class='rates-tabs rates-right']//li[1]//span")            # "Динамика изменения курсов"
    RIGHT_TABLE     = (By.XPATH, "//ul[@class='rates-tabs rates-right']//li[2]//span")            # "Расширенная таблица курсов"
    FROM_FILTER     = (By.NAME, 'filter-datepicker-details-from')                                 # date filter from
    TO_FILTER       = (By.NAME, 'filter-datepicker-details-to')                                   # date filter to
    BUTTON          = (By.XPATH, "//div[@class='rates-details-period-datepicker-line']//button")  # button "Показать" from right menu
    X_DATA_FIELD    = (By.CLASS_NAME, 'jqplot-axis.jqplot-xaxis')                                 # captions to the x-axis 