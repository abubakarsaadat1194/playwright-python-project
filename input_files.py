from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # Method 1: Direct file upload
    file_input = page.get_by_label("Default file input example")
    file_input.set_input_files("Xpath-functions.py")

    # Method 2: File chooser dialog
    with page.expect_file_chooser() as fc_info:
        file_input.click()

    file_chooser = fc_info.value

    file_chooser.set_files("text_input.py")

    browser.close()