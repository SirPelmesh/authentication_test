from BaseElement import BaseElement
from selenium.webdriver.common.by import By
from BasePage import BasePage

#добавить в Гитхабе KarasyovVS в репозитории
class WelcomePage(BasePage):
    UNIQUE_LOCATOR = (By.ID, "listAccounts")  # locator for the password field KarasyovVS
    URL = "http://testfire.net/bank/main.jsp"
    WelcomePage = BasePage(UNIQUE_LOCATOR)

    def return_locator(self):
        pass