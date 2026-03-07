from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    button = page.get_by_role("button", name="Default button")
    button.click()

    heading = page.get_by_role("heading", name="Heading 4")
    heading.click()

    switchbox = page.get_by_role("checkbox", name="Default switch checkbox input")
    switchbox.click()

    browser.close()