import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_context():
    print("\n[Setup] Launching Browser...")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()

    yield context

    print("\n[Teardown] Closing Browser...")
    context.close()
    browser.close()
    playwright.stop()

@pytest.fixture(scope="function")
def page(browser_context):
    print("\n[Setup] Launching Page...")
    return browser_context.new_page()