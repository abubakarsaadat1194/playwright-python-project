from playwright.sync_api import Page, expect

# Constants
BASE_URL = "https://playwright.dev/python"
DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_navigation_and_screenshots(page: Page):

    # Navigate to Playwright Python homepage
    page.goto(BASE_URL)

    docs_link = page.get_by_role("link", name="DOCS")

    expect(docs_link).to_have_attribute(
        "href", "/python/docs/intro"
    )