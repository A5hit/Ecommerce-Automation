from playwright.sync_api import Page
from data.test_data import get_locators
from pages.base_page import BasePage

class ListingPage(BasePage):

    def __init__(self, page : Page):
        super().__init__(page)
        self.loc = get_locators(page,"listing")

    def get_listing_title(self):
        return self.get_text(self.loc.product_listing_title)

    def click_product_from_listing(self):
        self.click_element(self.loc.listing_product_card)