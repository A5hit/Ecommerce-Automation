# tests/test_setup.py
from playwright.sync_api import Page


def test_environment_is_ready(page: Page):
    # 1. Go to Google
    page.goto("https://www.google.com")

    # 2. Print title (Verifies Playwright is controlling browser)
    print(f"Page Title is: {page.title()}")

    # 3. Assert (Verifies Pytest is working)
    assert "Google" in page.title()
