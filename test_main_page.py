import time

from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from selenium import webdriver
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    page = MainPage(browser,link) #инициализируем Page Object, передаем в конструктор экземпляр драйвера и link адрес
    page.open()
    login_page = page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    page = BasketPage(browser, link)
    page.open()
    page.quest_click_button_view_basket()
    page.product_is_not_exist_in_basket()
    page.text_about_basket_empty()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    browser.get(link)
    page = BasketPage(browser, link)
    page.open()
    page.quest_click_button_view_basket()
    page.product_is_not_exist_in_basket()
    page.text_about_basket_empty()



