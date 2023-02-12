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
                            ('naruto','uzumaki')
                        ]
                        )

def test_auth_with_wrong_username_and_password(login,password):
    logger.makeLog('__Test with wrong username and password__')
    Browser.go_to_site(HomePage.URL)
    logger.makeLog(text='Home page opened')
    Button(HomePage.LOGIN_BUTTON_LOCATOR).click_the_element()
    if LoginPage(LoginPage.USERNAME_LOCATOR).is_opened():
        logger.makeLog(text='Authorization page opened')
    LoginPage(LoginPage.USERNAME_LOCATOR).log_in(login, password)
    logger.makeLog(text='Data entered')
    assert WelcomePage(WelcomePage.UNIQUE_LOCATOR).is_closed(), logger.makeLog(text='Test failed')