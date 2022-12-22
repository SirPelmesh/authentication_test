import pytest
from selenium import webdriver


#creating a fixture to open/close the browser
@pytest.fixture(scope="session")
def browser():
    # create webdriver object
    driver = webdriver.Firefox()
    yield driver
    driver.quit()