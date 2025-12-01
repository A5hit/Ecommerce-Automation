from xml.dom.minidom import Element

from playwright.sync_api import Page

class base_page:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self,url: str):
        self.page.goto(url)

    def click_element(self, selector: str):
        try:
            self.psge.wait_for_element(selector)
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

    def is_visible(self,selector: str):
        try:
            self.page.wait_for_selector(selector)
            return self.page.is_visible(selector)
        except:
            self.take_screenshot(f"{selector}ElementNotFound.png")
            raise Exception(f"Element {selector} not found")