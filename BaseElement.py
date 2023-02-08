from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BasePage import BasePage

class BaseElement(BasePage):

    def enter_data(self, element, data):
        element.click()
        element.send_keys(data)

    def find_element(self, locator,time=1):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=1):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def element_is_present(self,locator):
        return len(self.find_elements(locator)) > 0

    def element_is_not_present(self,locator):
        return len(self.find_elements(locator)) < 1

    def submit_alert(self):
        self.driver.switch_to.alert.accept()

    def click_the_button(self,locator):
        self.find_element(locator).click()

