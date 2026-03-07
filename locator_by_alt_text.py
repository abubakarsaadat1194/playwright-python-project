from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://unsplash.com")

    # Highlight image using alt text
    page.get_by_alt_text("Elderly couple with harvested garlic bulbs").highlight()

    # Click another image using alt text
    page.get_by_alt_text("Rocky formations under a colorful, hazy sky.").click()

    browser.close()