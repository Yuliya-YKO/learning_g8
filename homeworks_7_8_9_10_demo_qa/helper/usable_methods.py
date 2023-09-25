from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def get_element_text_by_xpath(driver: WebDriver, locator: By.XPATH) -> str:
    return driver.find_element(*locator).text