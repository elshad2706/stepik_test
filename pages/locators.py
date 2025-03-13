from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    NAME_ITEM = (By.CSS_SELECTOR, "div.product_main > h1")
    PRICE_VALUE = (By.CSS_SELECTOR, "div.product_main > .price_color")
    MESSAGE_ADDED_TO_BASKET = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages > div > div > p:nth-child(1) > strong")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group")
    TOTAL_PRICE_MESSAGE = (By.XPATH,"/html/body/div[2]/div/div[1]/div[3]/div/p[1]")


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
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p > a") # (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/p")
    ITEM_ON_BASKET = (By.CSS_SELECTOR, ".col-sm-3.h3")




class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    TITLE_OF_PRODUCT = (By.CSS_SELECTOR, "div.product_main > h1")
    ADDED_TO_CART_TITLE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > .price_color") # 23,99 £
    CART_COST_MESSAGE = (By.CSS_SELECTOR, "#messages > div > div > p:nth-child(1) > strong") # 23,99 £
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

