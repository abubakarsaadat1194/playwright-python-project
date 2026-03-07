from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # Locate button
    button = page.get_by_role("button", name="Block button").last

    button.highlight()

    # Mouse actions
    button.click()

    button.dblclick()

    button.dblclick(delay=500)

    button.click(button="right")

    button.click(modifiers=["Shift"])

    button.click(modifiers=["Shift", "Alt"])

    # Hover example
    page.locator("button.btn-outline-primary").hover()

    browser.close()