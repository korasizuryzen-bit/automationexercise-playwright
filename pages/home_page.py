from playwright.sync_api import Page, expect
from .base_page import BasePage


class HomePage(BasePage):
    URL = "https://www.automationexercise.com/"

    def __init__(self, page: Page):
        super().__init__(page)

        # Ищем "Signup / Login" более гибко (не строгое совпадение)
        self.signup_login_link = page.get_by_text("Signup / Login", exact=False)

        self.products_link = page.get_by_text("Products", exact=False)
        self.cart_link = page.get_by_text("Cart", exact=False)

    def open_home(self):
        self.open(self.URL)

        # Ждём, что страница загрузилась
        self.page.wait_for_load_state("domcontentloaded")

        # Проверяем, что элемент меню существует
        expect(self.signup_login_link.first).to_be_visible()

    def go_to_signup_login(self):
        self.signup_login_link.first.click()

    def go_to_products(self):
        self.products_link.first.click()

    def go_to_cart(self):
        self.cart_link.first.click()
