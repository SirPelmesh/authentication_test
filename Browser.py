from selenium.common import NoAlertPresentException

from Singleton import Singleton
from Driver import Driver
from browser_config import BrowserConfig

class Browser(metaclass=Singleton):

    def __init__(self):
        self.driver = Driver.chooseDriver(BrowserConfig.BROWSER_NAME)

    @classmethod
    def get_driver(cls):
        return cls().driver

    @classmethod
    def quit(self):
        self.get_driver().quit()
        # self.driver = None

    # function to go to the specified url
    @classmethod
    def go_to_site(cls,base_url):
        cls.get_driver().get(base_url)
    
    # function to return the current url
    @classmethod
    def current_url(self):
        return self.driver.current_url

    @classmethod
    def refresh(self):
        self.driver.refresh()

    @classmethod
    def catch_alert(self):
        try:
            Browser.get_driver().switch_to.alert.accept()
            return True
        except NoAlertPresentException:
            return False
