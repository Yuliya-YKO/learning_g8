from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from homeworks_7_8_9_10_demo_qa.helper.usable_methods import get_element_text_by_xpath


class PageObjectTextBox:
    URL = 'https://demoqa.com/text-box'
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__full_name_field = (By.XPATH, '//input[@id = "userName"]' )
        self.__email_field = (By.XPATH, '//input[@id = "userEmail"]')
        self.__current_adr_field = (By.XPATH, '//textarea[@id = "currentAddress"]')
        self.__permanent_adr_field = (By.XPATH, '//textarea[@id = "permanentAddress"]')
        self.__submit_button = (By.XPATH, '//button[@id = "submit"]')

# get result
        self.__get_name = (By.XPATH, '//p[@id = "name"]')
        self.__get_email = (By.XPATH, '//p[@id = "name"]')
        self.__get_current_adr = (By.XPATH, '//p[@id = "currentAddress"]')
        self.__get_permanent_adr = (By.XPATH, '//p[@id = "permanentAddress"]')

    def open (self):
        self.__driver.get(self.URL)

    def set_full_name(self, fullname: str)-> None:
        element = self.__driver.find_element(*self.__full_name_field)
        element.clear()
        element.send_keys(fullname)

    def set_email(self, email: str)-> None:
        element = self.__driver.find_element(*self.__email_field)
        element.clear()
        element.send_keys(email)

    def set_curr_addr(self, cur_adr: str)->None:
        element = self.__driver.find_element(*self.__current_adr_field)
        element.clear()
        element.send_keys(cur_adr)

    def set_perm_addr(self, perm_adr: str)-> None:
        element = self.__driver.find_element(*self.__current_adr_field)
        element.clear()
        element.send_keys(perm_adr)

    def submit_button(self)-> None:
        element = self.__driver.find_element(*self.__submit_button)
        element.click()

    def get_result_name(self):
        full_text = get_element_text_by_xpath(self.__driver, self.__get_name)
        return full_text.split(':')[1]


    def get_result_email(self):
        full_text = get_element_text_by_xpath(self.__driver, self.__get_email)
        return full_text.split(':')[1]

    def get_result_curr_adr(self):
        full_text = get_element_text_by_xpath(self.__driver, self.__current_adr_field)
        return full_text.split(':')[1]


    def get_result_perm_adr(self):
        full_text = get_element_text_by_xpath(self.__driver, self.__get_permanent_adr)
        return full_text.split(':')[1]
