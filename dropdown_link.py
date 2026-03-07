from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # Open dropdown menu
    dropdown_menu = page.locator("button#btnGroupDrop1")
    dropdown_menu.click()

    # Highlight dropdown items
    page.locator("a.dropdown-item").highlight()

    # Select third dropdown link
    dropdown_link = page.locator("div.show > a.dropdown-item").nth(2)
    dropdown_link.highlight()

    # Select last dropdown link
    dropdown_link = page.locator("div.show > a.dropdown-item").last
    dropdown_link.highlight()

    dropdown_link.click()

    browser.close()