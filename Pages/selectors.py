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
        category_menu = (By.XPATH, "//button[@class='ta-cs-trigger css-p6fcqm-trigger']")
        category_menu_item_movie = (By.XPATH, "//label[text()='Filmy']")
        category_menu_item_music = (By.XPATH, "//label[text()='Muzyka']")
        category_menu_item_electronics = (By.XPATH, "//label[text()='Elektronika']")
        category_menu_item_books = (By.XPATH, "//label[text()='Książki']")
        search_box = (By.XPATH, "//input[@type='search']")
        search_icon = (By.XPATH, "//button[@title='Szukaj']")
        add_to_cart = (By.XPATH, "//*[contains(text(),'DODAJ DO KOSZYKA')]")
        maverick_top_gun_add_to_cart = (By.XPATH, "//button[@data-id='p1332653186']")
        maverick_top_gun_sound_track_add_to_cart = (By.XPATH, "//button[@data-id='p1308719380']")
        kindle_add_to_cart = (By.XPATH, "//button[@data-id='p1290861733']")
        festung_breslau_add_to_cart = (By.XPATH, "//button[@data-id='p1366592507']")
        cart_items = (By.XPATH, "//span[@class='empikNav__userIcon']//span[@class='infoCircle ta-counter']")
        first_found_item = (By.XPATH, "//strong[@class='ta-product-title']")
        logo = (By.XPATH, "//div[@class='empikHeader__logo']")
        cart = (By.ID, "simple-dropdown4")
        empty_cart_message = (By.XPATH, "//a[@class='minicart-empty']//span[@class='empikNav__userText']//span")

    class LoginPage:
        email = (By.ID, "user-email")
        given_email = (By.XPATH, "//div[@class='truncate']")
        password = (By.ID, "user-password")
        btn_login = (By.XPATH, "//button[text()='ZALOGUJ SIĘ']")
        incorrect_email_message = (By.XPATH, "//form[@id='user-login-form']/span[@class='error show']")
        incorrect_password_message = (
            By.XPATH, "//form[@id='user-login-form']//div[@class='infoBox type-error top-space']/div")

    class AccountDetailsPage:
        account_data = (By.XPATH, "//a[@href='/twoje-konto/twoje-dane' and @class='active']")
        account_data_header = (By.XPATH, "//header/h2")
        login_email = (
            By.XPATH, "//div[@class='user-data']//label[@for='email']/parent::*//span[@class='control-display']")
        nick = (By.XPATH, "//div[@class='user-data']//label[@for='nick']/parent::*//span[@class='control-display']")
        password = (
            By.XPATH, "//div[@class='user-data']//label[@for='password']/parent::*//span[@class='control-display']")
        name = (By.XPATH, "//div[@class='user-data']//label[@for='name']/parent::*//span[@class='control-display']")
        surname = (
            By.XPATH, "//div[@class='user-data']//label[@for='surname']/parent::*//span[@class='control-display']")
        phone_number = (
            By.XPATH, "//div[@class='user-data']//label[@for='phone-number']/parent::*//span[@class='control-display']")
        address = (
            By.XPATH, "//div[@class='user-data']//label[@for='address']/parent::*//span[@class='control-display']")
        date_of_birth = (
            By.XPATH, "//div[@class='user-data']//label[@for='b-date']/parent::*//span[@class='control-display']")

    class CartPage:
        prices = (By.XPATH, "//span[@data-ta='product-main-price']")
        purchase_price = (By.XPATH, "//span[@data-ta='purchase-price']")
        remove_item_from_cart = (By.XPATH, "//a[@data-ta='quantity-remove']")
        empty_cart_message = (By.XPATH, "//p[@class='css-z8hido-emptyCartTitle']")
        back_to_home_page = (By.XPATH, "//a[@class='css-w52lk0-emptyCartLink']")
