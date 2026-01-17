from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")

    def wait_visible(self, locator):
        expect(locator).to_be_visible()

    def click(self, locator):
        locator.click()

    def fill(self, locator, value: str):
        locator.fill(value)

    def get_text(self, locator) -> str:
        return locator.inner_text()
