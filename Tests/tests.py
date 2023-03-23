import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Pages.home_page import HomePage


@pytest.fixture()
def browser():
    path = os.path.expanduser("~/Desktop/Driver/chromedriver")
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.close()


def test_login(browser):
    HomePage.navigate(browser, 'https://www.empik.com/')
