import time

from selenium import webdriver
from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        button_basket = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET)
        button_basket.click()
    def get_item_before(self):
        name_item = WebDriverWait(self.browser,10).until(
            EC.visibility_of_element_located(MainPageLocators.NAME_ITEM))
        return name_item.text

    def get_price_before(self):
        price_value = WebDriverWait(self.browser,10).until(
            EC.visibility_of_element_located(MainPageLocators.PRICE_VALUE))
        return price_value.text
    def compare_item_and_price_after(self):
        message_text = self.get_element_text(*MainPageLocators.MESSAGE_ADDED_TO_BASKET)
        assert "has been added to your basket" in message_text,"Отсутствует сообщение о добавление товара в корзину"

        name_item = self.get_element_text(*MainPageLocators.MESSAGE_ADDED_TO_BASKET)
        assert ProductPage.get_item_before(self) in name_item,"Название товара в сообщении, о добавлении в корзину, не совпадает с товаром, который мы добавили"

        price_of_basket = self.get_element_text(*MainPageLocators.MESSAGE_PRICE_IN_BASKET)
        assert ProductPage.get_price_before(self) in price_of_basket,"Стоимость корзины не совпадает с ценой товара"


