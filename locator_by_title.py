from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    url = "https://bootswatch.com/default"

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(url)

    # Highlight element using title attribute
    page.get_by_title("Source Title").highlight()

    browser.close()