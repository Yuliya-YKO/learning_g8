from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver



class PageTextBox:
    URL = 'https://docs.google.com/forms/d/1DdsfDRJGn9Zhuc66gtEl2KBn4M8m6VV6ShNls57Ul6I/viewform?edit_requested=true'

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__email_field_loc = (By.XPATH, '/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
        self.__name_parents = (By.XPATH, '/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        self.__name_children = (By.XPATH, '/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        self.__yes_radio_button_xpath = (By.XPATH, '/html/body/div/div[3]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[7]/label/div/div[2]/div/span')
        self.__yes_radio_button2 = (By.XPATH, '/html/body/div/div[3]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
        self.__submit_button_loc = (By.XPATH, '/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        # self.__button_loc = (By.XPATH,
        #                      '//button[.="{}"]')  # any button with name taken as argument from corresponded method (instead of curves brackets)#
        # # locators for result getters
        # self.__result_name_loc = (By.XPATH, '//p[@id="name"]')
        # self.__result_email_loc = (By.XPATH, '//p[@id="email"]')
        # self.__result_curr_addr_loc = (By.XPATH, '//p[@id="currentAddress"]')
        # self.__result_perm_addr_loc = (By.XPATH, '//p[@id="permanentAddress"]')

    def open(self):
        self.__driver.get(self.URL)

    def set_email(self, email: str) -> None:
        element = self.__driver.find_element(*self.__email_field_loc)
        element.send_keys(email)

    def set_full_name(self, fullname: str) -> None:
        element = self.__driver.find_element(*self.__name_parents)
        element.send_keys(fullname)



    def set_current_address(self, address: str) -> None:
        element = self.__driver.find_element(*self.__name_children)
        element.clear()
        element.send_keys(address)


    def select_button_by_locator(self):
        element = self.__driver.find_element(*self.__yes_radio_button_xpath)
        element.click()

    def select_button_by_locator2(self):
        element = self.__driver.find_element(*self.__yes_radio_button2)
        element.click()
    # def set_permanent_address(self, perm_address: str) -> None:
    #     element = self.__driver.find_element(*self.__perm_addr_text_area_loc)
    #     element.clear()
    #     element.send_keys(perm_address)

    def submit(self) -> None:
        element = self.__driver.find_element(*self.__submit_button_loc)
        element.click()
    #
    # def click_button_by_name(self, button_name) -> None:
    #     by = self.__button_loc[0]
    #     loc = self.__button_loc[1].format(button_name)
    #     element = self.__driver.find_element(by, loc)
    #     # index [1] used, because locator 'self.__button_loc' is a tuple, and we need to work only with text part of locator#
    #     element.click()
    #
    # def get_result_name(self):
    #     full_text = get_element_text_by_xpath(self.__driver, self.__result_name_loc)
    #     return full_text.split(':')[1]
    #
    # def get_result_email(self):
    #     full_text = get_element_text_by_xpath(self.__driver, self.__result_email_loc)
    #     return full_text.split(':')[1]
    #
    # def get_result_current_address(self):
    #     full_text = get_element_text_by_xpath(self.__driver, self.__result_curr_addr_loc)
    #     return full_text.split(':')[1]
    #
    # def get_result_permanent_address(self):
    #     full_text = get_element_text_by_xpath(self.__driver, self.__result_perm_addr_loc)
    #     return full_text.split(':')[1]
