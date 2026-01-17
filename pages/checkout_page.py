import re
from playwright.sync_api import Page, expect
from .base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.place_order_btn = page.get_by_text("Place Order", exact=False)

        # payment form fields
        self.name_on_card = page.locator('input[data-qa="name-on-card"]')
        self.card_number = page.locator('input[data-qa="card-number"]')
        self.cvc = page.locator('input[data-qa="cvc"]')
        self.expiry_month = page.locator('input[data-qa="expiry-month"]')
        self.expiry_year = page.locator('input[data-qa="expiry-year"]')
        self.pay_and_confirm_btn = page.locator('button[data-qa="pay-button"]')

        # success elements (могут появляться после оплаты)
        self.order_placed_text = page.get_by_text("Order Placed!", exact=False)
        self.success_congrats = page.get_by_text("Congratulations", exact=False)
        self.continue_btn = page.get_by_text("Continue", exact=False)

    def ensure_checkout_opened(self):
        expect(self.place_order_btn).to_be_visible()

    def place_order_and_pay(self):
        self.page.mouse.wheel(0, 2000)
        self.place_order_btn.click()

        # Ждём поля оплаты
        expect(self.name_on_card).to_be_visible()

        self.name_on_card.fill("Test User")
        self.card_number.fill("4111111111111111")
        self.cvc.fill("123")
        self.expiry_month.fill("12")
        self.expiry_year.fill("2030")

        self.pay_and_confirm_btn.click()

    def verify_order_success(self):
        # 1) Попробуем поймать самый частый признак: "Order Placed!"
        if self.order_placed_text.first.is_visible():
            return

        # 2) Иногда пишут "Congratulations!"
        if self.success_congrats.first.is_visible():
            return

        # 3) Иногда успех — это наличие кнопки Continue
        if self.continue_btn.first.is_visible():
            return

        # 4) Если ничего из этого не нашли — покажем понятную ошибку
        # и оставим шанс увидеть правильную страницу по скриншоту failed.png
        raise AssertionError("Не нашли подтверждение успешного заказа (Order Placed / Congratulations / Continue).")
