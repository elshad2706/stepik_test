from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from selenium import webdriver


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    page = MainPage(browser,link)# инициализируем Page Object, передаем в конструктор экземпляр драйвера и link адрес
    page.open()
    page.go_to_login_page()


