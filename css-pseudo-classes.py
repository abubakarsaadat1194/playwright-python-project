from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    page.locator("span.bg-secondary:text('Secondary')").highlight()
    page.locator("span.bg-secondary:text-is('Secondary')").highlight()

    page.locator("div.dropdown-menu").highlight()
    page.locator("div.dropdown-menu:visible").highlight()

    page.locator(":nth-match(button.btn-secondary, 2)").highlight()
    page.locator(":nth-match(button.btn-secondary, 3)").highlight()
    page.locator(":nth-match(button.btn-secondary, 5)").highlight()
    page.locator(":nth-match(button.btn-secondary, 6)").highlight()

    browser.close()