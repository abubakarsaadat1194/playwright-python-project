from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    page.get_by_role("button", name="Primary").locator("nth=1").highlight()

    page.locator("button").locator("nth=1").highlight()

    page.get_by_label("Email address").locator("..").highlight()

    page.locator("id=btnGroupDrop1").highlight()

    page.locator("div.dropdown").highlight()
    page.locator("div.dropdown-menu").highlight()

    page.locator("div.dropdown-menu").locator("visible=true").highlight()

    page.get_by_role("heading").filter(has_text="Heading").highlight()

    page.get_by_role("heading").filter(has_text="Heading").locator("nth=1").highlight()

    page.locator("div.form-group").filter(has=page.get_by_label("Password")).highlight()

    browser.close()