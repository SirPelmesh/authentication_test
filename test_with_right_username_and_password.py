import pytest
from LoginPage import LoginPage
from WelcomePage import WelcomePage
from HomePage import HomePage
from Browser import Browser
from Framework.Button import Button
from Logger import Logg

logger=Logg()

@pytest.mark.parametrize('login, password',
                        [
                            ('admin', 'admin'),
                        ]
                        )
def test_with_right_username_and_password(login, password, browser):
    logger.makeLog('__Test with right username and password__')
    Browser.go_to_site(HomePage.URL)
    logger.makeLog(text='Home page opened')
    Button(HomePage.LOGIN_BUTTON_LOCATOR).click_the_element()
    if LoginPage(LoginPage.USERNAME_LOCATOR).is_opened():
        logger.makeLog(text='Authorization page opened')
    LoginPage(LoginPage.USERNAME_LOCATOR).log_in(login, password)
    logger.makeLog(text='Data entered')
    if WelcomePage(WelcomePage.UNIQUE_LOCATOR).is_opened():
        logger.makeLog(text='Welcome page opened')
    assert WelcomePage(WelcomePage.UNIQUE_LOCATOR).is_opened(), logger.makeLog(text='Test failed')