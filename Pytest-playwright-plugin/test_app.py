from playwright.sync_api import Page

def test_page_has_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link",name="GET STARTED")
    link.click()
    assert page.url == "https://playwright.dev/python/docs/intro"