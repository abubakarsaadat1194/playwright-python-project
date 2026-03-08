from playwright.sync_api import Page, expect, TimeoutError
import pytest


def test_UIAction(page: Page):
    page.goto("http://uitestingplayground.com/")
    homepage_button=page.get_by_role("link", name="Overlapped Element")
    homepage_button.click()
    input=page.get_by_placeholder("Name")
    scroll_placeholder=input.locator("..")
    scroll_placeholder.hover()
    page.mouse.wheel(0,200)
    data="python"
    input=page.get_by_placeholder("Name")
    input.fill(data)
    expect(input).to_have_value=data
