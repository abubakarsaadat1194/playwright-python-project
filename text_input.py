from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    input_field = page.get_by_label("Email address").first

    input_field.fill("ABC")

    input_field.clear()

    input_field.type("ABC")

    input_field.type("ABC", delay=500)

    input_field.clear()

    correct_value = page.locator("input.is-valid")

    print(correct_value.input_value())

    browser.close()