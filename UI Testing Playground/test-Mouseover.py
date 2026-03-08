from playwright.sync_api import Page, expect, TimeoutError
import pytest


def test_UIAction(page: Page):
    page.goto("http://uitestingplayground.com/")
    homepage_button=page.get_by_role("link", name="Mouse Over")
    homepage_button.click()
    Click_me_button=page.get_by_title("Click me")
    Click_me_button.hover()
    active_link=page.get_by_title("Active Link")
    active_link.click(click_count=2)
    count_on_site=page.locator("span#clickCount")
    expect(count_on_site).to_have_text("2")