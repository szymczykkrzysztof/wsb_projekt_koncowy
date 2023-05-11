from time import sleep

from TestData.testdata import TestData
from Pages.page_base import PageBase
from Pages.selectors import Selectors


class CartPage(PageBase):
    def validate_products_price_in_cart(self):
        sleep(2)
        prices = self.find_elements(Selectors.CartPage.prices, 360)
        purchase_price = self.find_element(Selectors.CartPage.purchase_price, 360).text
        purchase_price = purchase_price.replace(" zł", "").replace(",", ".")
        purchase_price = float(purchase_price)
        total_price = 0.0
        for item in prices:
            price = item.text
            price = price.replace(" zł", "").replace(",", ".")
            total_price += float(price)
        assert total_price == purchase_price
        return self

    def remove_item_from_cart(self):
        self.click_on(Selectors.CartPage.remove_item_from_cart, 360)
        sleep(5)
        return self

    def validate_empty_cart(self):
        sleep(5)
        purchase_price = self.find_element(Selectors.CartPage.purchase_price).text
        purchase_price = purchase_price.replace(" zł", "").replace(",", ".")
        purchase_price = float(purchase_price)
        assert purchase_price == 0.0
        message = self.find_element(Selectors.CartPage.empty_cart_message).text
        assert message == TestData.empty_cart_message
        return self

    def go_to_home_page(self):
        self.click_on(Selectors.CartPage.back_to_home_page, 360)
        from Pages.home_page import HomePage
        home_page = HomePage(self.driver, self.base_url)
        return home_page
