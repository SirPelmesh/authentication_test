from BaseElement import BaseElement
from selenium.webdriver.common.by import By

class WelcomePage(BaseElement):
    UNIQUE_LOCATOR = (By.ID, "ListAccounts")  # locator for the password field
    WELCOME_URL = "http://testfire.net/bank/main.jsp"

    def this_is_WelcomePage(self):
        if self.element_is_present(self.UNIQUE_LOCATOR) or self.return_current_url()==self.WELCOME_URL: return True