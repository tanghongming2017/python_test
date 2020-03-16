
from base.find_element import FindElement


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.find_element = FindElement(driver)

    def get_element(self, node_element, element):
        return self.find_element.get_element(node_element, element)

    def get_alert_element(self):
        return self.driver.switch_to.alert
