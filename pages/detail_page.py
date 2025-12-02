from playwright.sync_api import Page
from data.test_data import get_locators
from pages.base_page import BasePage

class DetailPage(BasePage):
    """Detail page class"""
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = get_locators(page,"product")

    def get_product_title(self):
        return self.get_text(self.loc.product_title)

    def get_product_price(self):
        return self.get_text(self.loc.product_price)

    def click_addToCart(self):
        self.click_element(self.loc.add_to_cart_btn)
        try:
            self.wait_for_element_visible(self.loc.quick_sell_popup)
            if self.is_element_visible(self.loc.quick_sell_popup):
                self.click_element(self.loc.quick_sell_popup)
            else:
                self.loc.go_to_cart_btn.click()
                print("✅ Product Added to Cart")
        except:
            print("✅ Product Added to Cart")