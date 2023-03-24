from selenium.webdriver.common.by import By

from Pages.page_base import PageBase


class LoginPage(PageBase):
    def login(self):
        self.check_title('Logowanie - EMPIK')
        self.enter_txt((By.ID, "user-email"), "krzysztof.szymczyk@yahoo.com")
        self.click_on((By.XPATH, "//button[text()='DALEJ']"), 60)
        self.enter_txt((By.ID, "user-password"), "")
        self.click_on((By.XPATH, "//button[text()='ZALOGUJ SIĘ']"), 60)
