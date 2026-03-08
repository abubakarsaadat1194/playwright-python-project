from playwright.sync_api import Page, expect

# Constants
BASE_URL = "https://playwright.dev/python"
DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_navigation_and_screenshots(page: Page):

    # Navigate to Playwright Python homepage
    page.goto(BASE_URL)

    # Locate "GET STARTED" link
    get_started_link = page.get_by_role("link", name="GET STARTED")

    # Locate "Docs" navigation link
    docs_link = page.get_by_role("link", name="Docs")

    # Click "GET STARTED" link
    get_started_link.click()

    # Verify navigation
    expect(page).to_have_url(DOCS_URL)