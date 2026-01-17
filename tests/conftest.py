import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        context = browser.new_context()
        page = context.new_page()

        # Дадим побольше времени ожиданиям (60 секунд)
        page.set_default_timeout(60000)

        yield page

        context.close()
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Этот хук запускается после каждого шага теста.
    # Если тест упал — мы сохраним скриншот.
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            page.screenshot(path="failed.png", full_page=True)
