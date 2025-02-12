from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    NAME_ITEM = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/h1")
    PRICE_VALUE = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]")
    MESSAGE_ADDED_TO_BASKET = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div")
    MESSAGE_PRICE_IN_BASKET = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group")


class LoginPageLocators:
    INPUT_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    BUTTON_SUBMIT = (By.NAME, "login_submit")
    FORGET_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")


class RegisterPageLocators:
    INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION_SUBMIT = (By.NAME, "registration_submit")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators:
    TEXT_EMPTY_BASKET = (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/p/text()")


