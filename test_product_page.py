import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{link}/?promo=offer{no}" for no in range(10)]
bugged_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
okey_link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
okey_link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8"

# @pytest.mark.parametrize('link', urls)
@pytest.mark.parametrize('link', [okey_link1, pytest.param(bugged_link, marks=pytest.mark.xfail), okey_link2])
def test_guest_can_add_product_to_basket(link,browser):
    browser.get(link)
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.get_item_before()
    product_page.get_price_before()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.compare_item_and_price_after()