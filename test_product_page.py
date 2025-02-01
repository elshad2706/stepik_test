import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{link}/?promo=offer{no}" for no in range(10)]

@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    browser.get(link)
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.get_item_before()
    product_page.get_price_before()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.compare_item_and_price_after()