import os

import allure

from pages.feedback_form_page import FeedbackFormPage


class TestFeedbackForm:
    @allure.epic("Тест формы обратной связи")
    class TestFeedbackFormPage:

        @allure.description("Тест отправки полностью заполненной формы")
        def test_send_fully_filled_form(self, driver):
            feedback_form_page = FeedbackFormPage(driver, f'file://{os.getcwd()}/data/test_for_QA/QA.html')
            feedback_form_page.open()
            feedback_form_page.fill_full_fields()
            with allure.step('Результат отправки формы'):
                assert feedback_form_page.check_send() == True, 'Форма не была отправлена'

        @allure.description("Тест кнопки 'Очистить'")
        def test_clear_form(self, driver):
            feedback_form_page = FeedbackFormPage(driver, f'file://{os.getcwd()}/data/test_for_QA/QA.html')
            feedback_form_page.open()
            feedback_form_page.fill_full_fields()
            feedback_form_page.clear_fields()
            result = feedback_form_page.check_clear()
            with allure.step('поле "ФИО"'):
                assert result[0] == '', 'В поле "ФИО" есть символы'
            with allure.step('поле "Компания"'):
                assert result[1] == '', 'В поле "Компания" есть символы'
            with allure.step('поле "E-mail"'):
                assert result[2] == '', 'В поле "E-mail" есть символы'
            with allure.step('поле "Файлы"'):
                assert result[3] == '', 'В поле "Файлы" есть символы'
            with allure.step('поле "Текст обращения"'):
                assert result[4] == '', 'В поле "Текст обращения" есть символы'

        @allure.description("Тест отправки только обязательных полей")
        def test_send_required_filled_form(self, driver):
            feedback_form_page = FeedbackFormPage(driver, f'file://{os.getcwd()}/data/test_for_QA/QA.html')
            feedback_form_page.open()
            feedback_form_page.fill_required_fields()
            with allure.step('Результат отправки формы'):
                assert feedback_form_page.check_send() == True, 'Форма не была отправлена'
