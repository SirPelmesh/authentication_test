from page import BasePage
from selenium.webdriver.common.by import By

# definition of locators to be used in the test
class LoginLocators:
    username_locator = (By.NAME, "uid") # locator for the username field
    password_locator = (By.NAME, "passw")  # locator for the password field
    button_locator = (By.NAME, "btnSubmit")  # locator for submit button

# functions for interacting with locators
class AuthForm(BasePage):
    # function to input username
    def enter_username(self, username):
        username_field = self.find_element(LoginLocators.username_locator)  # search for the username field
        username_field.send_keys(username)  # input username

    # function to input password
    def enter_password(self, password):
        passw_field = self.find_element(LoginLocators.password_locator)  # search for the password field
        passw_field.send_keys(password)  # input password

    # button click to send data
    def click_on_the_submit_button(self):
        self.find_element(LoginLocators.button_locator,time=0.5).click()  # search for a button and click

