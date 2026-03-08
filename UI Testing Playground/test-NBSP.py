from playwright.sync_api import Page, expect, TimeoutError
import pytest


def test_UIAction(page: Page):
    page.goto("http://uitestingplayground.com/")
    homepage_button=page.get_by_role("link", name="Non-Breaking Space")
    homepage_button.click()
    page.locator("//button[text()='My\u00a0Button']").click(
        timeout=2000
    )
