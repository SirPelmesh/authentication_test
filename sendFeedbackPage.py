from selenium.webdriver.common.by import By
from Framework.BasePage import BasePage
from Framework.TextBox import TextBox
from Framework.Button import Button

class sendFeedbackPage(BasePage):
    UNIQUE_LOCATOR = (By.XPATH, '//h1')
    URL = "http://testfire.net/sendFeedback.jsp"
    sendFeedbackPage = BasePage(UNIQUE_LOCATOR)
