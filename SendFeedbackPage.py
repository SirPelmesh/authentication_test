from selenium.webdriver.common.by import By
from Framework.BasePage import BasePage

class SendFeedbackPage(BasePage):

    UNIQUE_LOCATOR = (By.XPATH, '//h1')
    URL = "http://testfire.net/sendFeedback.jsp"

    def __init__(self):
        super().__init__(locator=self.UNIQUE_LOCATOR)