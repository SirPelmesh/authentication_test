from Browser import Browser
from selenium.webdriver.common.by import By
from BaseElement import BaseElement
from BasePage import BasePage

# functions for interacting with locators
class LoginPage(BasePage):
    # До этого BaseElement унаследовал функционал BasePage, поэтому теперь пишем здесь только BaseElement.
    # Правильно ли это, если интуитивно это не понятно?

    USERNAME_LOCATOR = (By.NAME, "uid")  # locator for the username field
    PASSWORD_LOCATOR = (By.NAME, "passw")  # locator for the password field
    BUTTON_LOCATOR = (By.NAME, "btnSubmit")  # locator for submit button
    URL = "http://testfire.net/login.jsp"

    LoginPage=BasePage(USERNAME_LOCATOR)

    # function to input username
    def enter_username(self, username):
        username_field = BaseElement(self.USERNAME_LOCATOR).find_element()  # search for the username field
        username_field.enter_data(username)

    # function to input password
    def enter_password(self, password):
        passw_field = BaseElement(self.PASSWORD_LOCATOR).find_element()  # search for the password field
        passw_field.enter_data(password)

    # button click to send data
    def click_on_the_submit_button(self):
        BaseElement(self.BUTTON_LOCATOR).click_the_button()

    def log_in(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_on_the_submit_button()


    def return_locator(self):
        pass






