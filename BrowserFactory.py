import pytest
from selenium import webdriver
from Singleton import Singleton

class Driver(metaclass=Singleton):
    @staticmethod
    def chooseDriver(browser_name):
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            print("\nstart chrome browser for test..")
            return webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            print("\nstart firefox browser for test..")
            browser = webdriver.Firefox(options=options)
            return browser
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
