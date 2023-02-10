import pytest
from Driver import Driver
from Browser import Browser
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    # browser=Browser(browser_name).get_driver()
    base_url = "http://testfire.net/"
    Browser().go_to_site(base_url)
    yield
    # browser.quit()
    Browser.quit()