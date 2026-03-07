from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # Radio buttons
    radio_btn_2 = page.get_by_label("Option two can be something else and selecting it will deselect option one")
    radio_btn_2.check()

    radio_btn_1 = page.get_by_label("Option one is this")
    radio_btn_1.check()

    # Checkbox
    checkbox = page.get_by_label("Default checkbox")

    checkbox.check()
    checkbox.uncheck()

    print(checkbox.is_checked())

    checkbox.check()

    # Switch
    switch_1 = page.get_by_label("Default switch checkbox input")

    switch_1.check()
    switch_1.uncheck()

    switch_1.click()
    switch_1.click()

    browser.close()