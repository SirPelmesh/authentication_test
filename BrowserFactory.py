import pytest
from selenium import webdriver
from Singleton import Singleton

class Driver(metaclass=Singleton):
    @staticmethod
    def chooseDriver(browser_name):
        if browser_name == "edge":
            print("\nstart chrome browser for test..")
            return webdriver.Edge()
        elif browser_name == "firefox":
            print("\nstart firefox browser for test..")
            browser = webdriver.Firefox()
            return browser
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")