import pytest
from Browser import Browser
from browser_config import BrowserConfig


'''def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="",
                     help="Choose browser: chrome or firefox")'''

@pytest.fixture(scope="function")
def browser(request):
    '''browser_name = request.config.getoption("browser_name")
    print(browser_name)
    if browser_name:
        BrowserConfig().change_browser_name(browser_name)'''
    base_url = "http://testfire.net/"
    Browser().go_to_site(base_url)
    yield
    # browser.quit()
    Browser.quit()
