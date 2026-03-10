from playwright.sync_api import sync_playwright, Page, expect
import pytest
def test_dynamic_class(page: Page):
    page.goto("http://uitestingplayground.com/classattr")
    button = page.locator("button.btn-primary")
    button = page.locator("//button[contains(@class, 'btn-primary')]")
    expect(button).to_be_visible()
    button.click
