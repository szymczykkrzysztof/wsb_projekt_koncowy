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
