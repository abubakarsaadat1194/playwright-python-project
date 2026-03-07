from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    page.locator("//h1").highlight()

    page.locator("//h1[@id='Buttons']").highlight()

    page.locator("//input[@readonly]").highlight()

    page.locator("//input[@value='wrong value']").highlight()

    browser.close()