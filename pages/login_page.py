from ..conftest import browser
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegisterPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Отсутствует логин в поле url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.INPUT_EMAIL), "Отсутствует инпут логина"
        assert self.is_element_present(*LoginPageLocators.INPUT_PASSWORD), "Отсутствует инпут пароля"
        assert self.is_element_present(*LoginPageLocators.BUTTON_SUBMIT), "Отсуствует кнопка войти"
        assert self.is_element_present(*LoginPageLocators.FORGET_PASSWORD), "Отсутствует кнопка забыли пароль"

    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.INPUT_EMAIL), "Отсутствует инпут логина"
        assert self.is_element_present(*RegisterPageLocators.INPUT_PASSWORD), "Отсутствует инпут пароля"
        assert self.is_element_present(*RegisterPageLocators.INPUT_REPEAT_PASSWORD), "Отсутствует инпут повторного ввода пароля"
        assert self.is_element_present(*RegisterPageLocators.BUTTON_REGISTRATION_SUBMIT), "Отсутствует кнопка войти"

    def register_new_user(self, email, password):
        WebDriverWait(self.browser, 3).until(
            EC.presence_of_element_located(RegisterPageLocators.INPUT_EMAIL)).send_keys(email)
        WebDriverWait(self.browser, 3).until(
            EC.presence_of_element_located(RegisterPageLocators.INPUT_PASSWORD)).send_keys(password)
        WebDriverWait(self.browser, 3).until(
            EC.presence_of_element_located(RegisterPageLocators.INPUT_REPEAT_PASSWORD)).send_keys(password)
        WebDriverWait(self.browser, 3).until(
            EC.presence_of_element_located(RegisterPageLocators.BUTTON_REGISTRATION_SUBMIT)).click()


