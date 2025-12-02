from xml.dom.minidom import Element

from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # ===== BROWSER ACTIONS =====

    def reload_page(self):
        """Reload current page"""
        self.page.reload()

    def go_back(self):
        """Navigate back"""
        self.page.go_back()

    def go_forward(self):
        """Navigate forward"""
        self.page.go_forward()

    def navigate_to(self,url: str):
        self.page.goto(url)

    def click_element(self, selector: str):
        try:
            self.page.wait_for_selector(selector)
            self.page.click(selector)
        except:
            self.take_screenshot(f"{selector}ElementNotFound.png")
            raise Exception(f"Element {selector} not found")

    def enter_text(self,selector: str, text: str):
        try:
            self.page.wait_for_selector(selector)
            self.page.click(selector)
            self.page.fill(selector, text)
        except:
            self.take_screenshot(f"{selector}ElementNotFound.png")
            raise Exception(f"Element {selector} not found")

    def get_text(self,selector: str):
        try:
            self.page.wait_for_selector(selector)
            self.page.click(selector)
            return self.page.text_content(selector)
        except:
            self.take_screenshot(f"{selector}ElementNotFound.png")
            raise Exception(f"Element {selector} not found")

    def take_screenshot(self,path: str):
        self.page.screenshot(path=path)

    # ===== WAIT & VISIBILITY =====

    def wait_for_element_visible(self, locator):
        """Wait for element to be visible"""
        locator.wait_for(state="visible")

    def wait_for_element_hidden(self, locator):
        """Wait for element to be hidden"""
        locator.wait_for(state="hidden")

    def is_element_visible(self, locator) -> bool:
        """Check if element is visible"""
        try:
            self.page.wait_for_selector(locator)
            return True
        except:
            return False

    # ===== DEBUGGING =====

    def print_current_url(self):
        """Print current URL (debugging)"""
        print(f"Current URL: {self.page.url}")

    def print_page_title(self):
        """Print page title (debugging)"""
        print(f"Page title: {self.page.title()}")

