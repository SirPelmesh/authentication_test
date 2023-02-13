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

def test_auth_with_entered_login_and_empty_password(browser,login):
    logger.makeLog('__Test with entered login and empty password__')
    Browser.go_to_site(HomePage.URL)
    logger.makeLog(text='Home page opened')
    HomePage().click_on_the_log_in_link_button()
    login_page=LoginPage()
    if login_page.is_opened():
        logger.makeLog(text='Authorization page opened')
    login_page.enter_username(login)
    logger.makeLog(text='Only login entered')
    login_page.click_on_the_submit_button()
    logger.makeLog(text='Button pressed, data sent')
    if Browser.catch_alert():
        logger.makeLog(text='Notification of blank password accepted')
    assert login_page.is_opened()