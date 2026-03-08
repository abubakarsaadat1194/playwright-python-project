from playwright.sync_api import Page, expect
import pytest


def test_UIAction(page: Page):
    page.goto("http://uitestingplayground.com/")
    scrlbar_btn=page.get_by_role("link", name="Scrollbars")
    scrlbar_btn.click()
    hiding_button=page.get_by_role("button", name="Hiding Button")
    hiding_button.scroll_into_view_if_needed()

    page.screenshot(path="test-scrollbars.jpg")
    