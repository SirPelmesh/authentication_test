import pytest
from Browser import Browser
from browser_config import BrowserConfig
from Logger import Logg

logger=Logg()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action = 'store', default = "chrome" )

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name:
        BrowserConfig.BROWSER_NAME = browser_name
        logger.makeLog(str(BrowserConfig.BROWSER_NAME))
    base_url = "http://testfire.net/"
    # Browser()
    Browser().driver_init(browser_name=browser_name)
    Browser.go_to_site(base_url)
    yield
    Browser.quit()
    Browser.clear()
    logger.makeLog(str(Browser.get_driver()))