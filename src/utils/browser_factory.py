# utils/browser_factory.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import json

def load_config():
    with open("config/config.json", "r") as file:
        config = json.load(file)
    return config

def get_driver():
    config = load_config()
    browser = config["browser"]

    if browser == "chrome":
        options = Options()
        options.headless = config["headless"]
        driver = webdriver.Chrome(service=ChromeService(executable_path="drivers/chromedriver.exe"), options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.headless = config["headless"]
        driver = webdriver.Firefox(service=FirefoxService(executable_path="drivers/geckodriver.exe"), options=options)
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    return driver
