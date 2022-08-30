import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
# open and close browser
def driver():
    #driver = webdriver.Firefox()
    #driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()
