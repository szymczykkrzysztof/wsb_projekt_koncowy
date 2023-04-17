from Pages.home_page import HomePage
from Pages.page_base import PageBase
from Pages.selectors import Selectors
from TestData.testdata import TestData


class AccountDetailsPage(PageBase):
    def goto_account_data(self):
        self.click_on(Selectors.AccountDetailsPage.account_data, 360)
        header = self.find_element(Selectors.AccountDetailsPage.account_data_header).text
        assert header == 'Dane konta'
        return self

    def verify_user_details(self):
        login = self.find_element(Selectors.AccountDetailsPage.login_email).text
        assert login == TestData.full_valid_user_name
        nick = self.find_element(Selectors.AccountDetailsPage.nick).text
        assert nick == TestData.full_valid_user_nick
        name = self.find_element(Selectors.AccountDetailsPage.name).text
        assert name == TestData.full_valid_user_first_name
        surname = self.find_element(Selectors.AccountDetailsPage.surname).text
        assert surname == TestData.full_valid_user_surname
        mobile = self.find_element(Selectors.AccountDetailsPage.phone_number).text
        assert mobile == TestData.full_valid_user_phone
        date_of_birth = self.find_element(Selectors.AccountDetailsPage.date_of_birth).text
        assert date_of_birth == TestData.full_valid_date_of_birth
        return self

    def goto_home_page(self):
        return HomePage(self.driver, self.base_url)
