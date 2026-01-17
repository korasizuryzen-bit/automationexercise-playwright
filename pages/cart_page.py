import re
from playwright.sync_api import Page, expect
from .base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_table = page.locator("#cart_info_table")
        self.cart_rows = page.locator("#cart_info_table tbody tr")

        self.proceed_checkout_by_text = page.locator('a:has-text("Proceed To Checkout")')
        self.proceed_checkout_any = page.get_by_text("Proceed To Checkout", exact=False)

    def verify_two_items_in_cart(self):
        expect(self.cart_table).to_be_visible()
        rows = self.cart_rows.count()
        if rows < 2:
            raise AssertionError(f"Ожидали минимум 2 товара в корзине, но нашли: {rows}")

    def proceed_to_checkout(self):
        # 1) Проверяем, что мы на странице корзины (view_cart)
        expect(self.page).to_have_url(re.compile(r".*view_cart.*"))

        # 2) Скроллим вниз (кнопка часто ниже)
        self.page.mouse.wheel(0, 2000)

        # 3) Кликаем по кнопке разными способами
        if self.proceed_checkout_by_text.first.is_visible():
            self.proceed_checkout_by_text.first.click()
            return

        expect(self.proceed_checkout_any).to_be_visible()
        self.proceed_checkout_any.click()
