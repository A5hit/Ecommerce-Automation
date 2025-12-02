from playwright.sync_api import Page

BASE_URL = "https://www.dailyobjects.com"


# ===== CLASS-BASED LOCATORS (for most pages) =====

class HomePageLocators:
    """Homepage semantic locators"""

    def __init__(self, page: Page):
        self.page = page

    @property
    def homepage_logo(self):
        return self.page.get_by_role("img", name="Store for Mobile Covers and Accessories")

    @property
    def explore_the_range(self):
        return self.page.get_by_role("heading", name="EXPLORE THE RANGE")

    @property
    def tech_add_ons(self):
        return self.page.get_by_text("Tech Add-ons", exact=True)

    @property
    def layout_product_card(self):
        return self.page.locator("//picture[@class='ng-star-inserted']//img[@alt='Airtag Cases']")


class ListingPageLocators:
    """Listing semantic locators"""
    def __init__(self, page: Page):
        self.page = page

    @property
    def product_listing_title(self):
        return self.page.locator("h1.listing-page-title")

    @property
    def listing_product_card(self):
        return self.page.locator("ul.products-result").locator("li")

class ProductDetailPageLocators:
    """Product detail semantic locators"""
    def __init__(self, page: Page):
        self.page = page

    @property
    def product_title(self):
        return self.page.get_by_role("heading")

    @property
    def product_price(self):
        return self.page.locator("p.desc__price.ng-star-inserted")

    @property
    def add_to_cart_btn(self):
        return self.page.locator("button").filter(has_text="ADD TO CART").first()

    @property
    def quick_sell_popup(self):
        return self.page.locator("button").filter(has_text="GO TO CART").last()

    @property
    def go_to_cart_btn(self):
        return self.page.locator('button').filter(has_text='GO TO CART').first()

class CartPageLocators:
    """CartPage semantic locators"""
    def __init__(self, page: Page):
        self.page = page

    @property
    def cart_page_title(self):
        return self.page.get_by_role("heading", name="SHOPPING BAG")

    @property
    def cart_product_card(self):
        xpath_loc = "//div[@class='description']"
        return self.page.locator(xpath_loc)

    @property
    def cart_product_title(self):
        xpath_loc = "/div/p[@ngstyle.xs='font-size: 13px']"
        return self.cart_product_card.locator(xpath_loc)

    @property
    def cart_product_price(self):
        xpath_loc = "/div/p[contains(.,'₹')]"
        return self.cart_product_card.locator(xpath_loc)

    @property
    def cart_grand_total(self):
        return  self.page.locator("span.grand-cost-value:visible")

    @property
    def checkout_btn(self):
        return self.page.get_by_role("button", name="CHECKOUT")

class CheckoutPageLocators:
    """Checkout semantic locators"""

    def __init__(self, page: Page):
        self.page = page

    @property
    def continue_btn(self):
        return self.page.get_by_role("button", name="CONTINUE")

    @property
    def cod_as_payment_type(self):
        return self.page.get_by_text("COD")

    @property
    def place_order_btn(self):
        return self.page.get_by_role("button", name="PLACE ORDER")

class OrderConfirmationPageLocators:
    """Order confirmation semantic locators"""
    def __init__(self, page: Page):
        self.page = page

    @property
    def order_confirmation(self):
        return self.page.get_by_text("ORDER RECEIVED", exact=True)

    @property
    def order_id(self):
        return self.page.locator("p.order-detail__data").nth(0)

    @property
    def order_details(self):
        return self.page.get_by_text("View order details")


# ===== LOCATOR REGISTRY (for page objects to use) =====

def get_locators(page: Page, page_name: str):
    """
    Get all locators for a page.

    Usage:
        locators = get_locators(page, "homepage")
        locators.product_item
    """
    locators_map = {
        "homepage": HomePageLocators,
        "listing": ListingPageLocators,
        "product": ProductDetailPageLocators,
        "cart": CartPageLocators,
        "checkout": CheckoutPageLocators,
        "order confirmation": OrderConfirmationPageLocators,
    }

    locator_class = locators_map.get(page_name)
    if not locator_class:
        raise ValueError(f"Unknown page: {page_name}")

    return locator_class(page)
