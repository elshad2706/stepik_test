from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegistrPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Отсутствует логин в поле url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.INPUT_EMAIL),"Отсутствует инпут логина"
        assert self.is_element_present(*LoginPageLocators.INPUT_PASSWORD),"Отсутствует инпут пароля"
        assert self.is_element_present(*LoginPageLocators.BUTTON_SUBMIT),"Отсуствует кнопка войти"
        assert self.is_element_present(*LoginPageLocators.FORGET_PASSWORD),"Отсутствует кнопка забыли пароль"
    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*RegistrPageLocators.INPUT_EMAIL), "Отсутствует инпут логина"
        assert self.is_element_present(*RegistrPageLocators.INPUT_PASSWORD), "Отсутствует инпут пароля"
        assert self.is_element_present(*RegistrPageLocators.INPUT_REPEAT_PASSWORD),"Отсутствует инпут повторного ввода пароля"
        assert self.is_element_present(*RegistrPageLocators.BUTTON_REGISTRATION_SUBMIT), "Отсуствует кнопка войти"
