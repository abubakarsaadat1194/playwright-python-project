from playwright.sync_api import Page, expect

# Constants
BASE_URL = "https://playwright.dev/python"
DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_get_started_link(page: Page):

    # Navigate to Playwright Python homepage
    page.goto(BASE_URL)
    input = page.get_by_placeholder("Search docs")

    #input is hidden before button click 
    expect(input).to_be_hidden()

    #search button 
    search_btn = page.get_by_role("button", name="Search")
    search_btn.click()

    #should pop the search menu 
    expect(input).to_be_editable()
    expect(input).to_be_empty

    text="Assertions"
    input.fill(text)
    expect(input).to_have_value(text)