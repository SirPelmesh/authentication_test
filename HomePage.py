from Browser import Browser
from selenium.webdriver.common.by import By
from BaseElement import BaseElement


class HomePage(BaseElement):
    UNIQUE_LOCATOR='// a[contains( @ href, "_savi")]'
    HOME_URL='http://testfire.net/index.jsp'
    BUTTON_LOCATOR = (By.ID, "LoginLink")

    def change_page(self):
        self.click_the_button(self.BUTTON_LOCATOR)

    def this_is_HomePage(self):
        if self.element_is_present(self.UNIQUE_LOCATOR) or self.return_current_url()==self.HOME_URL: return True
