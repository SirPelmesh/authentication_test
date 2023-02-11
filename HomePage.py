from selenium.webdriver.common.by import By
from Framework.BasePage import BasePage


class HomePage(BasePage):
    UNIQUE_LOCATOR='// a[contains( @ href, "_savi")]'
    URL='http://testfire.net/index.jsp'
    LOGIN_BUTTON_LOCATOR = (By.ID, "LoginLink")
    FEEDBACK_BUTTON_LOCATOR = (By.XPATH, "//a[contains(@href,'eedb')]")

    def return_locator(self):
        pass
