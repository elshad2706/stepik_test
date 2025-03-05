import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import pytest

link_product_1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{link_product_1}/?promo=offer{no}" for no in range(10)]
bugged_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
okay_link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
okay_link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8"
link_product_2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.need_review
# @pytest.mark.parametrize('link', urls)
@pytest.mark.parametrize('links', [okay_link1, pytest.param(bugged_link, marks=pytest.mark.xfail), okay_link2])
def test_guest_can_add_product_to_basket(links, browser):
    product_page = ProductPage(browser, links)
    product_page.open()
    product_page.get_name_product()
    product_page.get_price_product()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.compare_item_and_price_after_add_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_product_2)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_product_2)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link_product_3 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = BasketPage(browser, link_product_3)
    page.open()
    page.quest_click_button_view_basket()
    page.product_is_not_exist_in_basket()
    page.text_about_basket_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link_auth = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link_auth)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, "Qawsrf123124@")
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, link_product_1)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, link_product_1)
        product_page.open()
        product_page.get_name_product()
        product_page.get_price_product()
        product_page.add_to_basket()
        product_page.compare_item_and_price_after_add_basket()
