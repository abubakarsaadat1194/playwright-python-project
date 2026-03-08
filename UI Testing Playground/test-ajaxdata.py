from playwright.sync_api import Page, expect
import pytest


def test_ajaxdata(page: Page):
    page.goto("http://uitestingplayground.com/")
    load_dealy_btn =page.get_by_role("link", name="AJAX Data")
    load_dealy_btn.click()
    btn_triggering_ajax_request = page.get_by_role("button", name="Button Triggering AJAX Request")
    btn_triggering_ajax_request.click()
    confirmation_text=page.locator("p.bg-success")
    confirmation_text.wait_for(state="visible")
    expect(confirmation_text).to_be_visible()