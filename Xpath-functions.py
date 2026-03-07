from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    page.locator("//h1[contains(text(),'Head')]").highlight()

    page.locator("//button[contains(@class,'btn-lg')]").highlight()

    page.locator("//input[contains(@value,'correct')]").highlight()

    browser.close()