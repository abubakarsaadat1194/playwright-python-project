from playwright.sync_api import Page, expect
import pytest


def test_UIAction(page: Page):
    page.goto("http://uitestingplayground.com/")
    btn = page.get_by_role("link", name="Click")
    btn.click()
    btn_that_ignores_DOM_click=page.locator("button.btn-primary")
    btn_that_ignores_DOM_click.click()
    btn_that_comes_after_click=page.locator("button.btn-success")
    expect(btn_that_comes_after_click).to_be_visible()