from Pages.page_base import PageBase


class LoginPage(PageBase):
    def login(self):
        self.check_title('Logowanie - EMPIK')
