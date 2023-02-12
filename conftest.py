import pytest
from Browser import Browser


@pytest.fixture(scope="function")
def browser():

    base_url = "http://testfire.net/"
    Browser().go_to_site(base_url)
    yield
    Browser.quit()