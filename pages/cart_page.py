from playwright.sync_api import Page
from data.test_data import get_locators
from pages.base_page import BasePage

class CartPage(BasePage):
    """Checkout semantic locators"""
    def __init__(self,page : Page) :
        super().__init__(page)
        self.loc = get_locators(page,"cart")

    def get_cart_page_title(self):
        return self.get_text(self.loc.cart_page_title)

    def get_cart_items_count(self) -> int:
        count = self.loc.cart_product_card.count()
        print(f"Cart has {count} items")
        return count

    def get_added_product_title(self):
        return self.get_text(self.loc.cart_product_title)

    def get_added_product_price(self):
        return self.get_text(self.loc.cart_product_price)

    def get_grand_total_price(self):
        return self.get_text(self.loc.cart_grand_total)

    def click_checkout_btn(self):
        self.click_element(self.loc.checkout_btn)
