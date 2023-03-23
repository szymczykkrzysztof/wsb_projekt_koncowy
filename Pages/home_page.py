from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Pages.page_base import PageBase


class HomePage(PageBase):
    @staticmethod
    def navigate(driver, url):
        page = HomePage(driver, url)
        page.navigate_to()
        page.click_on(
            (By.XPATH, "//div[@class='css-5f0wxg-buttonsDesktop-buttonsDesktop']//button[text()='Zaakceptuj zgody']"),
            360)
        return page

    def goto_login_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(
            self.find_element((By.XPATH, "//a[@title='Zaloguj się' and @class='dropdown-menu-button']"), 360))
        action.perform()
        self.click_on((By.XPATH, "//a[@title='Zaloguj się' and @class='dropdown-menu-button']"), 360)
        from Pages.login_page import LoginPage
        return LoginPage(self.driver, self.base_url)
