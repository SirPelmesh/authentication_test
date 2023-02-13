import pytest
from Browser import Browser
from Logger import Logg

logger=Logg()


@pytest.fixture(scope="function")
def browser():

    base_url = "http://testfire.net/"
    # Browser()
    Browser.go_to_site(base_url)
    yield
    Browser.quit()
    Browser.clear()
    logger.makeLog(str(Browser.get_driver()))