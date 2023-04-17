from selenium.webdriver.common.by import By


class Selectors:
    class HomePage:
        btn_continue = (By.XPATH, "//button[text()='DALEJ']")
        btn_accept = (
            By.XPATH, "//div[@class='css-5f0wxg-buttonsDesktop-buttonsDesktop']//button[text()='Zaakceptuj zgody']")
        menu_item_login = (By.XPATH, "//a[@title='Zaloguj się' and @class='dropdown-menu-button']")
        logged_user_menu = (By.XPATH, "//span[@class='empikNav__userText ta-login-link']")
        menu_item_logout = (By.XPATH, "//a[@title='Wyloguj']")
        menu_item_my_profile = (By.XPATH, "//a[text()='Mój profil']")

    class LoginPage:
        email = (By.ID, "user-email")
        given_email = (By.XPATH, "//div[@class='truncate']")
        password = (By.ID, "user-password")
        btn_login = (By.XPATH, "//button[text()='ZALOGUJ SIĘ']")

    class AccountDetailsPage:
        account_data = (By.XPATH, "//a[@href='/twoje-konto/twoje-dane' and @class='active']")
        account_data_header = (By.XPATH, "//header/h2")
        login_email = (By.XPATH, "//div[@class='user-data']//label[@for='email']/parent::*//span[@class='control-display']")
        nick = (By.XPATH, "//div[@class='user-data']//label[@for='nick']/parent::*//span[@class='control-display']")
        password = (By.XPATH, "//div[@class='user-data']//label[@for='password']/parent::*//span[@class='control-display']")
        name = (By.XPATH, "//div[@class='user-data']//label[@for='name']/parent::*//span[@class='control-display']")
        surname = (By.XPATH, "//div[@class='user-data']//label[@for='surname']/parent::*//span[@class='control-display']")
        phone_number = (By.XPATH, "//div[@class='user-data']//label[@for='phone-number']/parent::*//span[@class='control-display']")
        address = (By.XPATH, "//div[@class='user-data']//label[@for='address']/parent::*//span[@class='control-display']")
        date_of_birth = (By.XPATH, "//div[@class='user-data']//label[@for='b-date']/parent::*//span[@class='control-display']")
