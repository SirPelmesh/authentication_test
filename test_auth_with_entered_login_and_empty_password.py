import pytest
from LoginPage import LoginPage
from HomePage import HomePage
from Browser import Browser
from Framework.Button import Button
from Logger import Logg

logger=Logg()

@pytest.mark.parametrize('login',
                        [
                            ('Sssnake!')
                        ]
                        )

def test_auth_with_entered_login_and_empty_password(login):
    logger.makeLog('__Test with entered login and empty password__')
    Browser.go_to_site(HomePage.URL)
    logger.makeLog(text='Home page opened')
    Button(HomePage.LOGIN_BUTTON_LOCATOR).click_the_element()
    if LoginPage(LoginPage.USERNAME_LOCATOR).is_opened():
        logger.makeLog(text='Authorization page opened')
    LoginPage(LoginPage.USERNAME_LOCATOR).enter_username(login)
    logger.makeLog(text='Only login entered')
    Button(LoginPage.BUTTON_LOCATOR).click_the_element()
    logger.makeLog(text='Button pressed, data sent')
    Browser.get_driver().switch_to.alert.accept()
    logger.makeLog(text='Notification of blank password accepted')
    assert LoginPage(LoginPage.USERNAME_LOCATOR).is_opened(), logger.makeLog(text='Test failed')