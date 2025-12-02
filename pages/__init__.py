"""
Page objects for Daily Objects e-commerce site.

Provides semantic page object implementations for:
- HomePage: Homepage browsing and navigation
- ListingPage: Product category/search listing
- ProductDetailPage: Individual product details
- CartPage: Shopping cart operations
- BasePage: Common browser actions and utilities

Usage:
    from pages import HomePage, CartPage, ProductDetailPage

    home = HomePage(page)
    home.navigate()
    home.click_tech_addons_category()
"""

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.listing_page import ListingPage
from pages.detail_page import DetailPage
from pages.cart_page import CartPage

__all__ = [
    "BasePage",
    "HomePage",
    "ListingPage",
    "DetailPage",
    "CartPage",
]
