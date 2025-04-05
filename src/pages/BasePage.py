from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def wait_for_element(self, by: By, value: str, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def find_element(self, by: By, value: str):
        return self.driver.find_element(by, value)

    def find_elements(self, by: By, value: str):
        return self.driver.find_elements(by, value)

    def go_to(self, url: str):
        self.driver.get(url)