from PageObject import AuthForm

class Factory(object):

    def authpage(self,browser,user=None,passw=None):  # client function
                self.main_page = AuthForm(browser)  # class initialization
                self.main_page.go_to_site()  # go to authentication page
                self.old_url=self.main_page.return_current_url(browser) # get the current url and save it as old_url
                return self.choose_path(browser, user, passw)

    def check_url(self,browser):  # url comparison function
        self.main_page.click_on_the_submit_button()  # click the submit button
        self.new_url = self.main_page.return_current_url(browser)  # get the current url and save it as new_url
        return self.new_url==self.old_url

    def catch_alert(self, browser):  # function for the alert acceptation
        self.main_page.click_on_the_submit_button()  # click the submit button
        self.main_page.submit_alert(browser)
        return True

    def username_exists(self, user):
        if user:
            self.main_page.enter_username(user)  # input username
            return True
        else:
            return False

    def password_exists(self,passw):
        if passw:
            self.main_page.enter_password(passw)  # input password
            return True
        else:
            return False

    def choose_path(self,browser,user,passw):
        if self.username_exists(user)*self.password_exists(passw)==True:  # if both username and password are not None
            return self.check_url(browser)
        else:
            return self.catch_alert(browser)



