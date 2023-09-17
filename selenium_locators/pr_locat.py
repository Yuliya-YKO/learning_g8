import pytest
import logging
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.fixture()
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
def test_2(chrome):
    chrome.get('https://demoqa.com/text-box')
    full_name_field = chrome.find_element(By.ID, 'userName')
    full_name_field.send_keys('Vasya')
    email_field = chrome.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]')
    email_field.send_keys('pupkin@mail.com')
    curr_addr_text_area = chrome.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
    curr_addr_text_area.send_keys('My curr addr in Ukraine')
    perm_addr_text_area = chrome.find_element(By.XPATH, '//textarea[contains(@id, "permanentA")]')
    perm_addr_text_area.send_keys('My perm addr also in Ukraine')
    submit_button = chrome.find_element(By.XPATH, '//button[.="Submit"]')
    # submit_button = chrome.find_element(By.XPATH, '//button[contains(text(), "Sub")]')
    submit_button.click()


    pass
