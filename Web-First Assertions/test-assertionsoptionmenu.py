from playwright.sync_api import Page, expect

# Constants
BASE_URL = "https://bootswatch.com/default"



def test_app(page: Page):

    # Navigate to Playwright Python homepage
    page.goto(BASE_URL)

    option_menu = page.get_by_label("Example select")

    expect(option_menu).to_have_value("1")

    multi_select_option_menu = page.get_by_label("Example multiple select")

    expect(multi_select_option_menu).to_have_values([])
    selected_options = ["2", "4"]
    multi_select_option_menu.select_option(selected_options)
    expect(multi_select_option_menu).to_have_values(selected_options)
