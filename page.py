from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://testfire.net/login.jsp"

    # function to find element
    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    # function to go to the specified url
    def go_to_site(self):
        return self.driver.get(self.base_url) 
    
    # function to return the current url
    def return_current_url(self,driver):
        return driver.current_url

    def submit_alert(self,driver):
        driver.switch_to.alert.accept()
