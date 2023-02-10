
import pytest
from LoginPage import LoginPage
from WelcomePage import WelcomePage
from HomePage import HomePage
from Browser import Browser
from Driver import Driver
from Browser import Browser
from BaseElement import BaseElement
from Button import Button
from TextBox import TextBox

@pytest.mark.parametrize('login, password',
                        [
                            ('admin', 'admin'),
                        ]
                        )
def test_altoro_matual_valid_auth(login, password, browser):
    Browser.go_to_site(HomePage.URL)
    Button(HomePage.LOGIN_BUTTON_LOCATOR).click_the_button()
    if LoginPage(LoginPage.USERNAME_LOCATOR).is_opened():
        print('Перешли на страницу аутентификации')
    LoginPage(LoginPage.USERNAME_LOCATOR).log_in(login, password)
    if WelcomePage(WelcomePage.UNIQUE_LOCATOR).is_opened():
        print('Перешли на страницу приветствия')
    assert WelcomePage(WelcomePage.UNIQUE_LOCATOR).is_opened()

'''@pytest.mark.parametrize('login, password',
                        [
                            ('naruto','uzumaki'),
                            ('SOMETHING', 'STRANGE')
                        ]
                        )
def test_altoro_matual_invalid_auth(login, password, browser):
    page = LoginPage(browser)
    page.log_in_with_filled_fields(login,password)
    assert page.this_is_LoginPage()'''

'''# invalid input
def test_altoro_matual_NONvalid_auth(browser,main_page=Factory()):
    assert main_page.authpage(browser,'naruto','uzumaki')==True

# input of only one field
def test_altoro_matual_onefield(browser,main_page=Factory()):
    assert main_page.authpage(browser,'hi')==True'''

