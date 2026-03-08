from playwright.sync_api import Page, expect
import pytest


def test_UIAction(page: Page):
    page.goto("http://uitestingplayground.com/")
    Text_input_btn=page.get_by_role("link", name="Text Input")
    Text_input_btn.click()
    input_field=page.get_by_label("Set New Button Name")
    query="Awesome"
    input_field.fill(query)
    btn_that_changes_name_on_input_text = page.locator("button.btn-primary")
    btn_that_changes_name_on_input_text.click()
    expect(btn_that_changes_name_on_input_text).to_have_text(query)