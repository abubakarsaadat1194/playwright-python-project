from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # CSS selectors examples
    page.locator("button").highlight()
    page.locator("button.btn-success").highlight()
    page.locator("button.btn-primary").highlight()
    page.locator("button.btn-lg").highlight()

    page.locator("h1").highlight()

    page.locator("input.form-control").highlight()
    page.locator("input#exampleInputEmail1").highlight()

    page.locator("small.text-muted").highlight()

    page.locator("input[readonly]").highlight()
    page.locator("input[value='email@example.com']").highlight()

    browser.close()