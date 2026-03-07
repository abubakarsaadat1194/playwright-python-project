from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # Highlight elements using text locators
    page.get_by_text("faded secondary").highlight()
    page.get_by_text("faded secondary", exact=True).highlight()

    # Highlight button
    page.get_by_text("Small button", exact=True).highlight()

    # Click buttons
    page.get_by_text("Small button", exact=True).click()
    page.get_by_text("Large button", exact=True).click()

    browser.close()