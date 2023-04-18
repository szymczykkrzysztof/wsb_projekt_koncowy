from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.page_base import PageBase
from Pages.selectors import Selectors


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
