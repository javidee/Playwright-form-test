import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True для безголового режиму
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
