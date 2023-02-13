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

def test_auth_with_wrong_username_and_password(browser,login,password):
    logger.makeLog('__Test with wrong username and password__')
    Browser.go_to_site(HomePage.URL)
    logger.makeLog(text='Home page opened')
    HomePage().click_on_the_log_in_link_button()
    if LoginPage().is_opened():
        logger.makeLog(text='Authorization page opened')
    LoginPage().log_in(login, password)
    logger.makeLog(text='Data entered')
    assert WelcomePage().is_closed()