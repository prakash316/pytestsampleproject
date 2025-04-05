# tests/test_login.py

import pytest
from pages.home_page import HomePage
from utils.browser_factory import get_driver
from utils.logger import logger

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_google_search(driver):
    try:
        # Initialize HomePage
        home_page = HomePage(driver)

        # Open Google
        home_page.open_url("https://www.google.com")

        # Perform search
        home_page.enter_search_query("Selenium with Python")
        home_page.click_search_button()

        # Assertion
        assert "Selenium with Python" in driver.title
        logger.info("Test passed successfully!")
    except Exception as e:
        logger.error(f"Test failed: {e}")
        raise
