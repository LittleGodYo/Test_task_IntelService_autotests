import os

from selenium.common.exceptions import NoAlertPresentException

from generator.generator import generated_person
from locators.feedback_forms_page_locators import FeedbackFormPageLocators
from pages.base_page import BasePage


class FeedbackFormPage(BasePage):
    locators = FeedbackFormPageLocators()

    def fill_full_fields(self):
        person = next(generated_person())
        path = rf'{os.getcwd()}\data\test_for_QA\QA.html'
        self.is_visible('css', self.locators.FULL_NAME).send_keys(person.full_name)
        self.is_visible('css', self.locators.COMPANY).send_keys(person.company)
        self.is_visible('css', self.locators.EMAIL).send_keys(person.email)
        self.is_present('css', self.locators.FILE_INPUT).send_keys(path)
        self.is_visible('css', self.locators.TEXT_OF_APPEAL).send_keys(person.text_of_appeal)
        return person

    def fill_required_fields(self):
        person = next(generated_person())
        self.is_visible('css', self.locators.FULL_NAME).send_keys(person.full_name)
        self.is_visible('css', self.locators.COMPANY).send_keys(person.company)
        self.is_visible('css', self.locators.EMAIL).send_keys(person.email)
        self.is_visible('css', self.locators.BUTTON_SUBMIT).click()
        return person

    def clear_fields(self):
        self.is_visible('css', self.locators.BUTTON_CLEAR).click()

    def check_send(self):
        self.is_visible('css', self.locators.BUTTON_SUBMIT).click()
        try:
            if self.text_alert() == 'Форма отправлена!':
                return True
        except NoAlertPresentException:
            return False

    def check_clear(self):
        full_name = self.is_visible('css', self.locators.FULL_NAME).get_attribute(name="value")
        company = self.is_visible('css', self.locators.COMPANY).get_attribute(name="value")
        email = self.is_visible('css', self.locators.EMAIL).get_attribute(name="value")
        file = self.is_present('css', self.locators.FILE_INPUT).get_attribute(name="value")
        text = self.is_visible('css', self.locators.TEXT_OF_APPEAL).get_attribute(name="value")
        return [full_name, company, email, file, text]
