from selenium import webdriver
import pytest

@pytest.fixture()
# def setup():
#     driver=webdriver.Chrome(executable_path="C:\\browser\\chromedriver.exe")
#     return driver

def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome(executable_path="C:\\browser\\chromedriver.exe")

    elif browser=='firefox':
        driver=webdriver.Firefox(executable_path="C:\\browser\\geckodriver.exe")

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



