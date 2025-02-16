from .base_page import BasePage
import time
from selenium import webdriver
from .base_page import BasePage
from .locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def product_is_not_exist_in_basket(self):
        try:
            WebDriverWait(self.browser,3).until(
                EC.presence_of_element_located(BasketPageLocators.ITEM_ON_BASKET))
        except TimeoutException:
            return True
        return False

    def text_about_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET), "Корзина не пуста,а должна быть пустой"

