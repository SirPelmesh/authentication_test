from selenium.common import NoAlertPresentException

from FeedbackPage import FeedbackPage
from HomePage import HomePage
from Browser import Browser
from Framework.Button import Button
from SendFeedbackPage import SendFeedbackPage
from Logger import Logg

logger=Logg()

def test_feedback_XSS_vuln():
    logger.makeLog('__Test feedback XSS vuln__')
    Browser.go_to_site(HomePage.URL)
    logger.makeLog(text='Home page opened')
    Button(HomePage.FEEDBACK_BUTTON_LOCATOR).click_the_element()
    if FeedbackPage(FeedbackPage.YOUR_NAME_LOCATOR).is_opened():
        logger.makeLog(text='Feedback page opened')
    FeedbackPage(FeedbackPage.YOUR_NAME_LOCATOR).enter_name("<script>alert('attack')</script>")
    logger.makeLog(text='JavaScript command entered in the name field')
    Button(FeedbackPage.BUTTON_LOCATOR).click_the_element()
    logger.makeLog(text='Button pressed, data sent')
    assert Browser.catch_alert(), logger.makeLog(text='Notification was not accepted')