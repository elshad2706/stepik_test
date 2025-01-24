from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,"#login_link")
class LoginPageLocators():
    INPUT_EMAIL = (By.CSS_SELECTOR,"#id_login-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR,"#id_login-password")
    BUTTON_SUBMIT = (By.NAME,"login_submit")
    FORGET_PASSWORD = (By.CSS_SELECTOR,"#id_registration-password2")
class RegistrPageLocators():
    INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION_SUBMIT = (By.NAME, "registration_submit")