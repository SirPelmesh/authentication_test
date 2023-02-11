from Singleton import Singleton
class BrowserConfig(object):
    BROWSER_NAME = 'chrome'

    @classmethod
    def change_browser_name(self,browser_name):
        self.BROWSER_NAME = str(browser_name)
        return self.BROWSER_NAME

    print(BROWSER_NAME)