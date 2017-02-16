import pytest
import csv
from selenium import webdriver


def csv_to_args(scv_file_name):
    csvfile = open(scv_file_name, newline='')
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    ids = []
    inputs = []
    outputs = []
    next(spamreader)
    for row in spamreader:
        id = row[0]
        input = row[1]
        output = row[2]
        ids.append(id)
        inputs.append(input)
        outputs.append(output)
    n_inp = ''
    for i in inputs:
        n_inp = n_inp + '+' + i[1:-1]
    inputs = n_inp.split('+')
    inputs = inputs[1:]
    n_out = ''
    for o in outputs:
        n_out = n_out + '+' + o[1:-1]
    outputs = n_out.split('+')
    outputs = outputs[1:]
    param = []
    x = 0
    while (x < len(inputs)):
        param.append((inputs[x], outputs[x]))
        x = x + 1
    return ([ids, param])


@pytest.fixture(scope="function", params=csv_to_args('input_data.csv')[1], ids=csv_to_args('input_data.csv')[0])
def param_test_for_insert_convertation_sum(request):
    return request.param


@pytest.fixture(scope="function", params=csv_to_args('input_dates.csv')[1], ids=csv_to_args('input_dates.csv')[0])
def param_test_for_from_to_filter(request):
    return request.param


@pytest.fixture(scope="function")
def resource_setup(request):
    print("\nconnect to converter site")
    with pytest.allure.step('open Firefox webdriver and connect to converter site'):
        driver = webdriver.Firefox()
        driver.get("http://www.sberbank.ru/ru/quotes/converter")
    driver.implicitly_wait(30)

    def resource_teardown():
        driver.quit()

    request.addfinalizer(resource_teardown)
    return driver
