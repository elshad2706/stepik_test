from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.locators import MainPageLocators
import pytest


@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.skip(reason="fixing this bug later")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.is_disappeared(*MainPageLocators.MESSAGE_ADDED_TO_BASKET)
