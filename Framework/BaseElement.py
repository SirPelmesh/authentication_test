from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Browser import Browser
from abc import ABC, abstractmethod

class BaseElement(ABC):
    driver=Browser.get_driver()

    def __init__(self,locator):
        self.locator=locator

    def enter_data(self,data):
        element = self.find_element()
        element.click()
        element.send_keys(data)

    def find_element(self,time=1):
        print(type(self.driver))
        print(type(self.locator))
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(self.locator))

    def find_elements(self,time=1):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(self.locator))

    def element_is_present(self):
        return len(self.find_elements()) > 0

    def element_is_not_present(self):
        return len(self.find_elements()) < 1

    def submit_alert(self):
        self.driver.switch_to.alert.accept()

    def click_the_button(self):
        element=self.find_element()
        element.click()

''' @abstractmethod
    def get_element(self):
        pass'''

