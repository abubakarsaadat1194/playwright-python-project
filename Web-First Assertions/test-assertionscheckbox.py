from playwright.sync_api import Page, expect

# Constants
BASE_URL = "https://bootswatch.com/default"



def test_get_started_link(page: Page):

    # Navigate to Playwright Python homepage
    page.goto(BASE_URL)

    default_checkbox = page.get_by_label("Default Checkbox")
    checked_checkbox = page.get_by_label("Checked checkbox")

    expect(checked_checkbox).to_be_checked()

    expect(default_checkbox).not_to_be_checked()