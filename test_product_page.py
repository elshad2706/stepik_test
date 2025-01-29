import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(link,browser):
    link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    browser.get(link)
    product_page = ProductPage(browser, link)
    product_page.open()
    time.sleep(5)
    product_page.get_item_before()
    time.sleep(5)
    product_page.get_price_before()
    time.sleep(5)
    product_page.add_to_basket()
    time.sleep(5)
    product_page.solve_quiz_and_get_code()
    time.sleep(5)
    product_page.compare_item_and_price_after()