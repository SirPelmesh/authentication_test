from selenium.webdriver.common.by import By
from Framework.BasePage import BasePage


class HomePage(BasePage):

    # a unique locator
    # that can be used to verify that this is the right page
    UNIQUE_LOCATOR=r'//a[contains(@href,"personal_savi")]'

    # page address
    URL='http://testfire.net/index.jsp'

    # locators of the links to other pages
    LOGIN_BUTTON_LOCATOR = (By.ID, "LoginLink")
    FEEDBACK_BUTTON_LOCATOR = (By.XPATH, "//a[contains(@href,'eedb')]")

    #для каждой кнопки отдельная функция

