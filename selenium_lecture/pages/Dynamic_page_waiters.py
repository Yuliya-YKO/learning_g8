from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class DynamicProperties:
    __URL = 'https://demoqa.com/dynamic-properties'

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__enable_after_button_loc = (By.XPATH, '//button[@id="enableAfter"]')
        self.__color_change_button_loc = (By.ID, 'colorChange')
        self.visible_after_button_loc = (By.CSS_SELECTOR, '#visibleAfter')

    def open(self):
        self.__driver.get(self.__URL)

    def get_enable_after_button_attribute(self, attribute):
        element = self.__driver.find_element(*self.__enable_after_button_loc)
        return element.get_attribute(attribute)

    def get_enable_after_button_element(self):
        element = self.__driver.find_element(*self.__enable_after_button_loc)
        return element
