from BasePage import BasePage
from selenium.webdriver.common.by import By
from BaseElement import BaseElement

# functions for interacting with locators
class LoginPage(BaseElement):
    # До этого BaseElement унаследовал функционал BasePage, поэтому теперь пишем здесь только BaseElement.
    # Правильно ли это, если интуитивно это не понятно?

    USERNAME_LOCATOR = (By.NAME, "uid")  # locator for the username field
    PASSWORD_LOCATOR = (By.NAME, "passw")  # locator for the password field
    BUTTON_LOCATOR = (By.NAME, "btnSubmit")  # locator for submit button
    LOGIN_URL = "http://testfire.net/login.jsp"

    # function to input username
    def enter_username(self, username):
        username_field = self.find_element(self.USERNAME_LOCATOR)  # search for the username field
        self.enter_data(username_field,username)

    # function to input password
    def enter_password(self, password):
        passw_field = self.find_element(self.PASSWORD_LOCATOR)  # search for the password field
        self.enter_data(passw_field,password)

    # button click to send data
    def click_on_the_submit_button(self):
        self.click_the_button(self.BUTTON_LOCATOR)

    def log_in_with_filled_fields(self, username, password):
        # это точно должно быть здесь?
        # я дублирую функции выше, есть ли в этом смысл?
        self.go_to_site()
        self.enter_username(username)
        self.enter_password(password)
        self.click_on_the_submit_button()

    def log_in_without_filled_fields(self, username, password):
        self.go_to_site()
        self.enter_username(username)
        self.enter_password(password)
        self.click_on_the_submit_button()
        self.submit_alert()

    def this_is_LoginPage(self):
        if self.element_is_present(self.USERNAME_LOCATOR) and self.return_current_url()==self.LOGIN_URL: return True




