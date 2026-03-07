from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # Highlight email field
    page.get_by_label("Email address").highlight()

    # Highlight password field
    page.get_by_label("Password").highlight()

    # Highlight textarea field
    page.get_by_label("Example textarea").highlight()

    # Highlight placeholder inputs
    page.get_by_placeholder("Default input").highlight()
    page.get_by_placeholder("Email address").highlight()
    page.get_by_placeholder("name@example.com").highlight()

    browser.close()