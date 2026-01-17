from playwright.sync_api import Page, expect
from .base_page import BasePage


class SignupLoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # New User Signup
        self.new_user_name = page.locator('input[data-qa="signup-name"]')
        self.new_user_email = page.locator('input[data-qa="signup-email"]')
        self.signup_button = page.locator('button[data-qa="signup-button"]')

        # Account Information
        self.title_mr = page.locator('input[id="id_gender1"]')
        self.password = page.locator('input[data-qa="password"]')
        self.days = page.locator('select[data-qa="days"]')
        self.months = page.locator('select[data-qa="months"]')
        self.years = page.locator('select[data-qa="years"]')

        self.first_name = page.locator('input[data-qa="first_name"]')
        self.last_name = page.locator('input[data-qa="last_name"]')
        self.address = page.locator('input[data-qa="address"]')
        self.state = page.locator('input[data-qa="state"]')
        self.city = page.locator('input[data-qa="city"]')
        self.zipcode = page.locator('input[data-qa="zipcode"]')
        self.mobile_number = page.locator('input[data-qa="mobile_number"]')

        self.create_account_btn = page.locator('button[data-qa="create-account"]')
        self.continue_btn = page.locator('a[data-qa="continue-button"]')

    def start_signup(self, name: str, email: str):
        expect(self.new_user_name).to_be_visible()
        self.new_user_name.fill(name)
        self.new_user_email.fill(email)
        self.signup_button.click()

    def fill_account_info_and_create(self, password: str):
        expect(self.page.get_by_text("ENTER ACCOUNT INFORMATION")).to_be_visible()

        self.title_mr.check()
        self.password.fill(password)

        self.days.select_option("1")
        self.months.select_option("1")
        self.years.select_option("2000")

        self.first_name.fill("Test")
        self.last_name.fill("User")
        self.address.fill("Tashkent street 1")
        self.state.fill("Tashkent")
        self.city.fill("Tashkent")
        self.zipcode.fill("100000")
        self.mobile_number.fill("901234567")

        self.create_account_btn.click()

    def confirm_account_created(self):
        expect(self.page.get_by_text("ACCOUNT CREATED!")).to_be_visible()
        self.continue_btn.click()
