from playwright.sync_api import Page, expect

# Constants
BASE_URL = "https://playwright.dev/python"
DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_navigation_and_screenshots(page: Page):

    # Navigate to Playwright Python homepage
    page.goto(BASE_URL)

    dropdown_menu= page.locator("ul.dropdown__menu")

    expect(dropdown_menu).to_contain_text("Python")
    expect(dropdown_menu).to_contain_text("Java")
    expect(dropdown_menu).to_contain_text("Node.js")
    expect(dropdown_menu).to_contain_text(".NET")
    