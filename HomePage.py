from Browser import Browser
from selenium.webdriver.common.by import By
from BaseElement import BaseElement
from BasePage import BasePage


class HomePage(BasePage):
    UNIQUE_LOCATOR='// a[contains( @ href, "_savi")]'
    URL='http://testfire.net/index.jsp'
    LOGIN_BUTTON_LOCATOR = (By.ID, "LoginLink")

    def return_locator(self):
        pass
