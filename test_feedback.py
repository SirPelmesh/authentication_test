import pytest
from FeedbackPage import FeedbackPage
from sendFeedbackPage import sendFeedbackPage
from HomePage import HomePage
from Browser import Browser
from Framework.Button import Button


def test_filling_name_only():
    Browser.go_to_site(HomePage.URL)
    Button(HomePage.FEEDBACK_BUTTON_LOCATOR).click_the_button()
    FeedbackPage(FeedbackPage.YOUR_NAME_LOCATOR).enter_name('Sergey')
    Button(FeedbackPage.BUTTON_LOCATOR).click_the_button()
    assert sendFeedbackPage(sendFeedbackPage.UNIQUE_LOCATOR).is_opened()
