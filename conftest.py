import pytest
from Browser import Browser
from browser_config import BrowserConfig

# parser работает, но его значения никуда не передаются и нигде не сохраняются
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser():
    # было нужно для получения флага с помощью parser-а выше, но BROWSER_NAME был прописан в browser_config
    #browser_name = request.config.getoption("browser_name")

    # было нужно для получения флага с помощью parser-а выше и изменения значения BROWSER_NAME в browser_config
    #if browser_name:
     #   BrowserConfig().change_browser_name(browser_name)

    base_url = "http://testfire.net/"
    Browser().go_to_site(base_url)
    yield
    Browser.quit()