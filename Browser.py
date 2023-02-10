from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Singleton import Singleton
from Driver import Driver

from browser_config import BrowserConfig
#Browser должен иметь подклассы разных браузеров - это значит, что Browser Тоже абстрактный класс?

class Browser(metaclass=Singleton):
    # может быть это classmethod?
    #def __init__(self, browser_name):
    driver = Driver.chooseDriver(BrowserConfig.BROWSER_NAME)

    @classmethod
    def get_driver(self):
        return self.driver
    @classmethod
    def quit(self):
        self.get_driver().quit()

    # function to go to the specified url
    @classmethod
    def go_to_site(self):
        return self.driver.get(self.base_url) 
    
    # function to return the current url

    @classmethod
    def current_url(self):
        return self.driver.current_url

    @classmethod
    def refresh(self,driver):
        driver.switch_to.alert.accept()

#browser должен проходить тонкой линией везде, но как его инициализировать один раз и передавать везде,
# когда нужно, не используя наследование?
