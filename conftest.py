import pytest
from Browser import Browser
from Logger import Logg

logger=Logg(f'Browser-{str(Browser)}')


@pytest.fixture(scope="function")
def browser():

    base_url = "http://testfire.net/"
    Browser.go_to_site(base_url)
    logger.make_log(text='Home page opened')
    yield
    Browser.quit()
    Browser.clear()
    logger.make_log(str(Browser.get_driver()))