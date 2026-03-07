from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # Single select dropdown
    single_select = page.get_by_label("Example select")

    single_select.select_option("2")
    single_select.select_option("4")

    # Multi select dropdown
    multi_select = page.get_by_label("Example multiple select")

    multi_select.select_option(["2", "5"])
    multi_select.select_option(["2", "5", "1"])

    browser.close()