import os
import time

from pages.feedback_form_page import FeedbackFormPage


class TestFeedbackForm:
    class TestFeedbackFormPage:
        def test_text_box(self, driver):
            text_box_page = FeedbackFormPage(driver, 'file://' + os.getcwd().replace('tests', '') + 'data/test_for_QA/QA.html')
            text_box_page.open()
            time.sleep(5)