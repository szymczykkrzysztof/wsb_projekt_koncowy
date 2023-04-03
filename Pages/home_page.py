from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

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
        action = ActionChains(self.driver)
        action.move_to_element(
            self.find_element(Selectors.HomePage.menu_item_login, 360))
        action.perform()
        self.click_on(Selectors.HomePage.menu_item_login, 360)
        from Pages.login_page import LoginPage
        return LoginPage(self.driver, self.base_url)
