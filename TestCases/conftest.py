import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utilities.readProperties import ReadConfig

################### Get the value from Command Line ###########################
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="type in browser_name")

##################### Return the value to init_driver method #####################
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")

@pytest.fixture(scope="function")
def init_driver(request):
    from selenium import webdriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser= request.config.getoption("--browser")
################################## Chrome Browser #############################
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(ReadConfig.getApplicationURL())
        driver.find_element_by_id("details-button").click()
        driver.find_element_by_id("proceed-link").click()
################################## Firefox ####################################
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(ReadConfig.getApplicationURL())

################################ Default Browser ###############################
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(ReadConfig.getApplicationURL())
        driver.find_element_by_id("details-button").click()
        driver.find_element_by_id("proceed-link").click()



    driver.implicitly_wait(3)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
    driver.quit()


####################### PyTest HTML Report #####################

def pytest_configure(config):
    config._metadata['Project Name'] = "EOTS"
    config._metadata['Module Name'] =  ""
    config._metadata['Release Version'] = "21.1"

@pytest.mark.optionhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)


