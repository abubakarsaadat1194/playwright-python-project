from playwright.sync_api import Browser, Page
import pytest
# Constants
BASE_URL = "https://playwright.dev/python"
DOCS_URL = "https://playwright.dev/python/docs/intro"

@pytest.fixture()
def record_video(browser: Browser):
    context=browser.new_context(
        record_video_dir="video/"
    )
    page= context.new_page()
    yield page
    context.close()

def test_page_navigation_and_screenshots(record_video: Page):
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
    record_video.goto(BASE_URL)

    dark_mode_toggle_btn=record_video.locator("button.toggleButton_gllP")
    dark_mode_toggle_btn.click()

    # Locate "GET STARTED" link
    get_started_link = record_video.get_by_role("link", name="GET STARTED")


    # Locate "Docs" navigation link
    docs_link = record_video.get_by_role("link", name="Docs")
    

    # Click "GET STARTED" link
    get_started_link.click()

    
    # Verify navigation
    assert record_video.url == DOCS_URL