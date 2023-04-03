from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages.home_page import HomePage
from Pages.page_base import PageBase
from Pages.selectors import Selectors
from TestData.testdata import TestData


class LoginPage(PageBase):

    def login_with_user(self, login, password):
        self.check_title(TestData.login_page_title)
        self.enter_txt(Selectors.LoginPage.email, login)
        self.click_on(Selectors.HomePage.btn_continue, 60)
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element(Selectors.LoginPage.given_email,
                                             f"E-mail: {login}"))
        email = self.find_element(Selectors.LoginPage.given_email).text
        assert email == f"E-mail: {login}"
        self.enter_txt(Selectors.LoginPage.password, password)
        self.click_on(Selectors.LoginPage.btn_login, 60)
        return HomePage(self.driver, self.base_url)
