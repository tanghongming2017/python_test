# coding=utf-8
import time
from selenium import webdriver
from base.find_element import FindElement


class ActionMethod:

    def open_browser(self, browser):
        if browser == 'chrome':
            self.webdriver = webdriver.Chrome()
        elif browser == 'firefox':
            self.webdriver = webdriver.Firefox()
        else:
            self.webdriver = webdriver.Edge()

    def get_url(self, url):
        self.webdriver.get(url)

    def get_element(self, node_element, element):
        find_element = FindElement(self.webdriver)
        return find_element.get_element(node_element, element)

    def send_element_value(self, node_element, element, value):
        self.get_element(node_element, element).send_keys(value)

    def click_element(self, node_element, element):
        self.get_element(node_element, element).click()

    def wait_time(self, n):
        time.sleep(int(n))

    def close_browser(self):
        self.webdriver.close()

    def get_title(self):
        return self.webdriver.title

    def get_alert_text(self):
        result = ''
        try:
            alert_element = self.webdriver.switch_to.alert
            result = alert_element.text
            alert_element.accept()
        except:
            pass
        finally:
            return result
