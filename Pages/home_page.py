from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages.cart_page import CartPage
from Pages.page_base import PageBase
from Pages.selectors import Selectors
from TestData.testdata import TestData


class HomePage(PageBase):
    @staticmethod
    def navigate(driver, url):
        page = HomePage(driver, url)
        page.navigate_to()
        page.click_on(Selectors.HomePage.btn_accept, 360)
        return page

    def goto_login_page(self):
        self.hover_over_main_menu(Selectors.HomePage.menu_item_login)
        self.click_on(Selectors.HomePage.menu_item_login, 360)
        from Pages.login_page import LoginPage
        return LoginPage(self.driver, self.base_url)

    def switch_to_login_page(self):
        from Pages.login_page import LoginPage
        return LoginPage(self.driver, self.base_url)

    def logout(self):
        self.hover_over_main_menu(Selectors.HomePage.logged_user_menu)
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(Selectors.HomePage.menu_item_logout))
        self.click_on(Selectors.HomePage.menu_item_logout, 360)
        return self

    def goto_user_details(self):
        self.hover_over_main_menu(Selectors.HomePage.logged_user_menu)
        self.click_on(Selectors.HomePage.menu_item_my_profile, 360)
        from Pages.account_details_page import AccountDetailsPage
        return AccountDetailsPage(self.driver, self.base_url)

    def select_category(self, category):
        self.click_on(Selectors.HomePage.category_menu, 360)
        self.click_on(category, 360)

        return self

    def add_product_to_cart(self, category, value, add_to_cart_selector, items_in_cart):
        # sleep(3)
        self.select_category(category)
        self.enter_txt(Selectors.HomePage.search_box, value)
        self.click_on(Selectors.HomePage.search_icon, 360)
        self.hover_over_main_menu(Selectors.HomePage.first_found_item)
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(add_to_cart_selector))
        self.click_on(add_to_cart_selector, 360)
        sleep(2)
        current_item_in_cart = self.find_element(Selectors.HomePage.cart_items).text
        assert current_item_in_cart == items_in_cart
        # sleep(2)
        return self

    def click_on_logo(self):
        self.click_on(Selectors.HomePage.logo, 360)
        return self

    def click_on_cart(self):
        self.click_on(Selectors.HomePage.cart, 360)
        cart = CartPage(self.driver, self.base_url)
        return cart

    def validate_empty_cart(self):
        message = self.find_element(Selectors.HomePage.empty_cart_message).text
        assert message == TestData.empty_cart
        return self
