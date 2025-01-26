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
    def get_item_and_price_before(self):
        name_item = WebDriverWait(self.browser,10).until(
            EC.visibility_of_element_located(*MainPageLocators.NAME_ITEM)).text()
        price_value = WebDriverWait(self.browser,10).until(
            EC.visibility_of_element_located(*MainPageLocators.PRICE_VALUE)).text()
        return name_item,price_value
    def compare_item_and_price_after(self):
        assert "has been added to your basket" in self.is_element_present(*MainPageLocators.MESSAGE_ADDED_TO_BASKET),"Отсутствует сообщение о добавление товара в корзину"
        assert ProductPage.get_item_and_price_before(self) in self.is_element_present(*MainPageLocators.MESSAGE_ADDED_TO_BASKET),"Отсутствует название товара в сообщении о добавлении в корзину"
        assert ProductPage.get_item_and_price_before(self) in self.is_element_present(*MainPageLocators.MESSAGE_PRICE_IN_BASKET),"Стоимость корзины не совпадает с ценой товара"