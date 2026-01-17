from playwright.sync_api import Page, expect
from .base_page import BasePage


class HomePage(BasePage):
    URL = "https://www.automationexercise.com/"

    def __init__(self, page: Page):
        super().__init__(page)
        self.signup_login_link = page.get_by_role("link", name="Signup / Login")
        self.products_link = page.get_by_role("link", name="Products")
        self.cart_link = page.get_by_role("link", name="Cart")

    def open_home(self):
        self.open(self.URL)

        # Ждём, что URL реально стал сайтом
        expect(self.page).to_have_url("https://www.automationexercise.com/")

        # И ждём, что меню видно
        expect(self.signup_login_link).to_be_visible()

    def go_to_signup_login(self):
        self.signup_login_link.click()

    def go_to_products(self):
        self.products_link.click()

    def go_to_cart(self):
        self.cart_link.click()
