from playwright.sync_api import BrowserContext, Page
import pytest
# Constants
BASE_URL = "https://playwright.dev/python"
DOCS_URL = "https://playwright.dev/python/docs/intro"

@pytest.fixture(autouse=True)
def trace_test(context: BrowserContext):
    context.tracing.start(
        name="playwright",
        screenshots=True,
        snapshots=True, 
        sources=True,

    )
    yield
    context.tracing.stop(path="traces/trace.zip")

def test_page_navigation_and_screenshots(page: Page):
    """
    Test navigation to the Playwright documentation page and demonstrate
    multiple ways of taking screenshots using Playwright.

    This test performs the following steps:
    1. Opens the Playwright Python homepage.
    2. Takes a screenshot of the visible viewport.
    3. Captures screenshots of specific elements.
    4. Navigates using the "GET STARTED" link.
    5. Captures a full-page screenshot of the documentation page.
    6. Verifies the navigation URL.
    """

    # Navigate to Playwright Python homepage
    page.goto(BASE_URL)

  

    # Locate "GET STARTED" link
    get_started_link = page.get_by_role("link", name="GET STARTED")


    # Locate "Docs" navigation link
    docs_link = page.get_by_role("link", name="Docs")


    

    # Click "GET STARTED" link
    get_started_link.click()

    

    # Verify navigation
    assert page.url == DOCS_URL