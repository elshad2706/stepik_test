import time
import pytest
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from selenium import webdriver
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_quest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        login_page = page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = BasketPage(browser, link)
        page.open()
        page.quest_click_button_view_basket()
        page.product_is_not_exist_in_basket()
        page.text_about_basket_empty()
