import allure

from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.test_data import unique_email


@allure.title("E2E: Registration -> Add 2 products -> Check cart -> Checkout")
def test_e2e_buy_flow(page):
    home = HomePage(page)
    signup = SignupLoginPage(page)
    products = ProductsPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    with allure.step("Open home page"):
        home.open_home()

    with allure.step("Go to Signup/Login"):
        home.go_to_signup_login()

    with allure.step("Register new user"):
        email = unique_email()
        signup.start_signup(name="TestUser", email=email)
        signup.fill_account_info_and_create(password="Password123!")
        signup.confirm_account_created()

    with allure.step("Go to Products"):
        home.go_to_products()
        products.ensure_opened()

    with allure.step("Add first two products to cart and open cart"):
        products.add_first_two_products_to_cart()

    with allure.step("Verify 2 items in cart"):
        cart.verify_two_items_in_cart()

    with allure.step("Proceed to checkout"):
        cart.proceed_to_checkout()
        checkout.ensure_checkout_opened()

    with allure.step("Place order and pay"):
        checkout.place_order_and_pay()

    with allure.step("Verify order success"):
        checkout.verify_order_success()
