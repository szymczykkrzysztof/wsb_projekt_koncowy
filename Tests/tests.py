import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.home_page import HomePage
from Pages.selectors import Selectors
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
        .check_title(TestData.home_page_title) \
        .logout() \
        .check_title(TestData.home_page_title)


def test_login_with_given_user_and_verify_details(browser):
    HomePage.navigate(browser, TestData.empik_url) \
        .goto_login_page() \
        .login_with_user(TestData.full_valid_user_name, TestData.valid_user_name_password) \
        .check_title(TestData.home_page_title) \
        .goto_user_details() \
        .goto_account_data() \
        .verify_user_details() \
        .goto_home_page() \
        .logout() \
        .check_title(TestData.home_page_title)


# This test is passing until captcha will require additional authorization
def test_validate_incorrect_login_password_message(browser):
    HomePage.navigate(browser, TestData.empik_url) \
        .goto_login_page() \
        .validate_improper_login_message(TestData.invalid_user_name) \
        .login_with_user(TestData.full_valid_user_name, TestData.invalid_user_name_password) \
        .switch_to_login_page() \
        .validate_improper_password_message()


def test_validate_adding_and_removing_products_to_cart(browser):
    HomePage.navigate(browser, TestData.empik_url) \
        .goto_login_page() \
        .login_with_user(TestData.full_valid_user_name, TestData.valid_user_name_password) \
        .add_product_to_cart(Selectors.HomePage.category_menu_item_music, TestData.top_gun_maverick,
                             Selectors.HomePage.maverick_top_gun_sound_track_add_to_cart, "1") \
        .click_on_logo() \
        .add_product_to_cart(Selectors.HomePage.category_menu_item_electronics, TestData.kindle_paperwhite,
                             Selectors.HomePage.kindle_add_to_cart, "2") \
        .click_on_logo() \
        .add_product_to_cart(Selectors.HomePage.category_menu_item_books, TestData.festung_breslau,
                             Selectors.HomePage.festung_breslau_add_to_cart, "3") \
        .click_on_cart() \
        .validate_products_price_in_cart() \
        .remove_item_from_cart() \
        .validate_products_price_in_cart() \
        .remove_item_from_cart() \
        .validate_products_price_in_cart() \
        .remove_item_from_cart() \
        .validate_empty_cart() \
        .go_to_home_page() \
        .validate_empty_cart() \
        .logout() \
        .check_title(TestData.home_page_title)
