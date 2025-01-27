import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import math
from selenium.common.exceptions import NoAlertPresentException

class BasePage:
    def __init__(self,browser,link,timeout=10):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.link)

    def is_element_present(self,how,what):
        try:
            self.browser.find_element(how,what)
        except NoSuchElementException:
            return False
        return True

    def get_element_text(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            print("элемент 2 -------------",element.text)
            return element.text
        except NoSuchElementException:
            return None  # Если элемент не найден, вернуть None

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








