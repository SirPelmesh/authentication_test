from FeedbackPage import FeedbackPage
from HomePage import HomePage
from Browser import Browser
from Framework.Button import Button
from SendFeedbackPage import SendFeedbackPage
from Logger import Logg

logger=Logg()

def test_feedback_sending_only_with_name():
    logger.makeLog('__Test sending feedback only with a name__')
    Browser.go_to_site(HomePage.URL)
    logger.makeLog(text='Home page opened')
    Button(HomePage.FEEDBACK_BUTTON_LOCATOR).click_the_element()
    if FeedbackPage(FeedbackPage.YOUR_NAME_LOCATOR).is_opened():
        logger.makeLog(text='Feedback page opened')
    FeedbackPage(FeedbackPage.YOUR_NAME_LOCATOR).enter_name('Sergey')
    logger.makeLog(text='Only name entered')
    Button(FeedbackPage.BUTTON_LOCATOR).click_the_element()
    logger.makeLog(text='Button pressed, data sent')
    assert SendFeedbackPage(SendFeedbackPage.UNIQUE_LOCATOR).is_opened(), logger.makeLog(text='Test failed')