from playwright.sync_api import Page

# Constants
BASE_URL = "https://playwright.dev/python"
DOCS_URL = "https://playwright.dev/python/docs/intro"


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

    # Screenshot Method 1: Capture visible page viewport
    page.screenshot(path="screenshots/homepage_viewport.png")

    # Locate "GET STARTED" link
    get_started_link = page.get_by_role("link", name="GET STARTED")

    # Screenshot Method 2: Capture specific element
    get_started_link.screenshot(path="screenshots/get_started_element.png")

    # Locate "Docs" navigation link
    docs_link = page.get_by_role("link", name="Docs")

    # Screenshot Method 3: Capture another element
    docs_link.screenshot(path="screenshots/docs_link.png")

    # Screenshot Method 4: Highlight area by bounding box screenshot
    box = docs_link.bounding_box()
    if box:
        page.screenshot(
            path="screenshots/docs_link_area.png",
            clip={
                "x": box["x"],
                "y": box["y"],
                "width": box["width"],
                "height": box["height"],
            },
        )

    # Click "GET STARTED" link
    get_started_link.click()

    # Screenshot Method 5: Capture full page screenshot
    page.screenshot(
        path="screenshots/docs_full_page.png",
        full_page=True
    )

    # Verify navigation
    assert page.url == DOCS_URL