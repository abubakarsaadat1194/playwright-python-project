from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    page.locator("input[value='email@example.com']").highlight()

    page.locator("nav.bg-dark").highlight()
    page.locator("footer").highlight()

    page.locator("nav.bg-dark div.container-fluid").highlight()
    page.locator("nav.bg-dark div.container-fluid div.navbar-collapse").highlight()

    page.locator("nav.bg-dark div.container-fluid div.navbar-collapse a.active").highlight()
    page.locator("nav.bg-dark div.container-fluid div.navbar-collapse a.active").click()

    page.locator("div.bs-compenet > ul.list-group").highlight()
    page.locator("div.bs-compenet>ul.list-group").highlight()

    browser.close()