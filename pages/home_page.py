from playwright.sync_api import Page
from pages.base_page import BasePage
from data.test_data import get_locators, BASE_URL

class HomePage(BasePage):

    def __init__(self, page : Page):
        super().__init__(page)
        self.loc = get_locators(page, "homepage")

    def go_to_home_page(self):
        self.page.goto(BASE_URL)
        print("✅ Navigated to homepage")

    def verify_home_page_load(self):
        assert self.is_element_visible(self.loc.homepage_logo)
        print("✅ Verified on homepage")

    def navigate_to_layout(self):
        self.loc.explore_the_range.scroll_into_view_if_needed()
        print("✅ Layout Loaded")

    def click_tech_addons_section(self):
        self.click_element(self.loc.tech_add_ons)
        print("✅ Layout Section Loaded")

    def click_layout_product(self):
        self.click_element(self.loc.layout_product_card)
        print("✅ Clicked Layout Section Product")

