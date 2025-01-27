from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    browser.get(link)
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.get_item_before()
    product_page.get_price_before()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.compare_item_and_price_after()