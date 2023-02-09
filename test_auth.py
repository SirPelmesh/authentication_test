
import pytest
from LoginPage import LoginPage
from WelcomePage import WelcomePage
from HomePage import HomePage

@pytest.mark.parametrize('login, password',
                        [
                            ('admin', 'admin'),
                        ]
                        )
def test_altoro_matual_valid_auth(login, password, browser):
    LoginPage(browser).log_in_with_filled_fields(login,password)
    assert WelcomePage.this_is_WelcomPage()

@pytest.mark.parametrize('login, password',
                        [
                            ('naruto','uzumaki'),
                            ('SOMETHING', 'STRANGE')
                        ]
                        )
def test_altoro_matual_invalid_auth(login, password, browser):
    page = LoginPage(browser)
    page.log_in_with_filled_fields(login,password)
    assert page.this_is_LoginPage()

'''# invalid input
def test_altoro_matual_NONvalid_auth(browser,main_page=Factory()):
    assert main_page.authpage(browser,'naruto','uzumaki')==True

# input of only one field
def test_altoro_matual_onefield(browser,main_page=Factory()):
    assert main_page.authpage(browser,'hi')==True'''

