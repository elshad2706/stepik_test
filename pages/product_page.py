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

    def get_name_product(self):
        name_item = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.NAME_ITEM))
        return name_item.text

    def get_price_product(self):
        price_value = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.PRICE_VALUE))
        return price_value.text

    def compare_item_and_price_after_add_basket(self):
        assert self.is_element_present(*MainPageLocators.TOTAL_PRICE_MESSAGE), "Отсутствует cообщение со стоимостью корзины"

        price_in_basket = self.get_element_text(*MainPageLocators.PRICE_IN_BASKET)
        assert ProductPage.get_price_product(self) == price_in_basket, "Стоимость корзины,после добаления товара, не совпадает с ценой товара"

        assert self.is_element_present(*MainPageLocators.MESSAGE_ADDED_TO_BASKET), "Отсутствует сообщение о добавление товара в корзину"

        message_full_text = self.get_element_text(*MainPageLocators.MESSAGE_ADDED_TO_BASKET)
        assert f"{ProductPage.get_name_product(self)}" in message_full_text, "Название товара в сообщении не совпадает с тем товаром, который мы добавили."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*MainPageLocators.MESSAGE_ADDED_TO_BASKET), "Успешное сообщение присутствует,но не должен был быть"
