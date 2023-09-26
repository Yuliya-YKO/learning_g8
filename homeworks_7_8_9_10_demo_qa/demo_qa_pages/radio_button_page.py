from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageRadioButton:
    __URL = 'https://demoqa.com/radio-button'

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__yes_radio_button_xpath = '//label[@for="yesRadio"]//ancestor::div[contains(@class, "radio")]'
        self.__impressive_radio_button_xpath = ('//label[@for="impressiveRadio"]//ancestor::div[contains(@class, '
                                                '"radio")]')
        self.__no_radio_button_xpath = '//label[@for="noRadio"]//ancestor::div[contains(@class, "radio")]'

    def open(self):
        self.__driver.get(self.__URL)

    def __select_button_by_locator(self, xpath):
        self.__driver.find_element(*xpath).click()

    def select_yes_button(self):
        locator = (By.XPATH, self.__yes_radio_button_xpath + '/label')
        self.__select_button_by_locator(locator)

    def select_impressive_button(self):
        locator = (By.XPATH, self.__impressive_radio_button_xpath + '/label')
        self.__select_button_by_locator(locator)

    # def select_no_radio_button(self):
    #     no_label = driver.find_element_by_xpath("//label[@for='noRadio']")
    #     driver.execute_script("arguments[0].classList.remove('disabled')", no_label)
    #     self.__driver.find_element(*no_label).click()

    def enable_no_button(self):
        script = "document.querySelector('#noRadio').removeAttribute('disabled');"
        self.__driver.execute_script(script)

    def select_no_button(self):
        locator = (By.XPATH, self.__no_radio_button_xpath + '/label')
        self.__select_button_by_locator(locator)

    def is_yes_button_selected(self) -> bool:
        locator = (By.XPATH, self.__yes_radio_button_xpath + '/input')
        return self.__driver.find_element(*locator).is_selected()

    def is_impressive_button_selected(self) -> bool:
        locator = (By.XPATH, self.__impressive_radio_button_xpath + '/input')
        return self.__driver.find_element(*locator).is_selected()

    def is_no_button_selected(self) -> bool:
        locator = (By.XPATH, self.__no_radio_button_xpath + '/input')
        return self.__driver.find_element(*locator).is_selected()

    def is_yes_button_enabled(self) -> bool:
        locator = self.__yes_radio_button_xpath + '/input'
        return self.__driver.find_element(By.XPATH, locator).get_attribute('disabled') is None

    def is_impressive_button_enabled(self) -> bool:
        locator = self.__impressive_radio_button_xpath + '/input'
        return self.__driver.find_element(By.XPATH, locator).get_attribute('disabled') is None

    def is_no_button_enabled(self) -> bool:
        locator = self.__no_radio_button_xpath + '/input'
        return self.__driver.find_element(By.XPATH, locator).get_attribute('disabled') is None
