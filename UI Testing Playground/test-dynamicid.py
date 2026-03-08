from playwright.sync_api import sync_playwright, Page, expect

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/dynamicid")
    dynamic_id_button=page.get_by_role("button", name="Button with Dynamic ID")
    expect(dynamic_id_button).to_be_visible()
    dynamic_id_button.click()