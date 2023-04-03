from selenium.webdriver.common.by import By


class Selectors:
    class HomePage:
        btn_continue = (By.XPATH, "//button[text()='DALEJ']")
        btn_accept = (By.XPATH, "//div[@class='css-5f0wxg-buttonsDesktop-buttonsDesktop']//button[text()='Zaakceptuj zgody']")
        menu_item_login = (By.XPATH, "//a[@title='Zaloguj się' and @class='dropdown-menu-button']")

    class LoginPage:
        email = (By.ID, "user-email")
        given_email = (By.XPATH, "//div[@class='truncate']")
        password = (By.ID, "user-password")
        btn_login = (By.XPATH, "//button[text()='ZALOGUJ SIĘ']")
