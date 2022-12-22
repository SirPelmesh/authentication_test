import selenium

from actions import Factory

# valid input
def test_altoro_matual_valid_auth(browser,main_page=Factory()):
    assert main_page.authpage(browser,'admin','admin')==False

# invalid input
def test_altoro_matual_NONvalid_auth(browser,main_page=Factory()):
    assert main_page.authpage(browser,'naruto','uzumaki')==True

# input of only one field
def test_altoro_matual_onefield(browser,main_page=Factory()):
    assert main_page.authpage(browser,'hi')==True

