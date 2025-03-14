import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from .locators import *


class BasePage:
    def __init__(self, browser, link, timeout=10):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.link)
        self.browser.maximize_window()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what,
                               timeout=4):  # упадет,как только увидит отысковаемый элемент.Если не появился:пройден
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def quest_click_button_view_basket(self):
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(MainPageLocators.VIEW_BASKET)).click()

    def is_disappeared(self, how, what, timeout=4):  # будет ждать до тех пор, пока элемент не исчезнет.
        try:
            WebDriverWait(self.browser, timeout).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def get_element_text(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            return element.text
        except NoSuchElementException:
            return None

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     "probably unauthorised user"
