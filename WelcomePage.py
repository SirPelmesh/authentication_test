from BaseElement import BaseElement
from selenium.webdriver.common.by import By

class WelcomePage(BaseElement):
    USERNAME_LOCATOR = (By.NAME, "uid")  # locator for the username field
    PASSWORD_LOCATOR = (By.NAME, "passw")  # locator for the password field
    BUTTON_LOCATOR = (By.NAME, "btnSubmit")  # locator for submit button
    LOGIN_URL = "http://testfire.net/login.jsp"