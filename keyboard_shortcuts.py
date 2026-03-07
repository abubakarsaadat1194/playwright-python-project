from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    textarea = page.get_by_label("Example textarea")

    textarea.fill("word")
    textarea.clear()

    textarea.press("KeyW")
    textarea.press("Shift+KeyW")

    textarea.press("KeyO")
    textarea.press("Shift+KeyO")

    textarea.press("ArrowLeft")
    textarea.press("ArrowRight")

    textarea.press("Control+KeyA")

    browser.close()