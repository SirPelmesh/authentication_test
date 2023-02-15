from FeedbackPage import FeedbackPage
from HomePage import HomePage
from Browser import Browser
from Framework.Button import Button
from SendFeedbackPage import SendFeedbackPage
from Logger import Logg

logger=Logg('test_feedback_sending_only_with_name')


def test_feedback_sending_only_with_name(browser):

    logger.make_log('__Test sending feedback only with a name__')
    #Browser.go_to_site(HomePage.URL)
    #logger.makeLog(text='Home page opened')
    HomePage().click_on_the_feedback_link_button()
    assert FeedbackPage().is_opened()
    logger.make_log(text='Feedback page opened')
    FeedbackPage().enter_name('Sergey')
    logger.make_log(text='Only name entered')
    FeedbackPage().click_on_the_submit_button()
    logger.make_log(text='Button pressed, data sent')
    assert SendFeedbackPage().is_opened()