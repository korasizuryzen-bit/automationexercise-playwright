from playwright.sync_api import Page, expect
from .base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.continue_shopping_btn = page.get_by_role("button", name="Continue Shopping")
        self.view_cart_link = page.get_by_role("link", name="View Cart")

    def ensure_opened(self):
        expect(self.page.locator("body")).to_contain_text("Products")

    def add_first_two_products_to_cart(self):
        product_cards = self.page.locator(".product-image-wrapper")
        count = product_cards.count()
        if count < 2:
            raise AssertionError("На странице меньше 2 товаров, невозможно добавить 2 товара.")

        first = product_cards.nth(0)
        first.hover()
        first.locator('a:has-text("Add to cart")').first.click()

        expect(self.page.locator(".modal-content")).to_be_visible()
        self.continue_shopping_btn.click()

        second = product_cards.nth(1)
        second.hover()
        second.locator('a:has-text("Add to cart")').first.click()

        expect(self.page.locator(".modal-content")).to_be_visible()
        self.view_cart_link.click()
