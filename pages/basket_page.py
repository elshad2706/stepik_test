from .base_page import BasePage
import time
from selenium import webdriver
from .base_page import BasePage
from .locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def text_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET), "Корзина не пуста,а должна быть"

