from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")

    def enter_search_query(self, query: str):
        search_box = self.find_element(*self.SEARCH_BOX)
        search_box.send_keys(query)

    def click_search_button(self):
        search_button = self.find_element(*self.SEARCH_BUTTON)
        search_button.click()

    def search(self, query: str):
        self.enter_search_query(query)
        self.click_search_button()