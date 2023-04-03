import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.home_page import HomePage
from TestData.testdata import TestData


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.close()
    driver.quit()


def test_login_with_given_user(browser):
    HomePage.navigate(browser, TestData.empik_url) \
        .goto_login_page() \
        .login_with_user(TestData.valid_user_name, TestData.valid_user_name_password) \
        .check_title(TestData.home_page_title)
