from playwright.sync_api import Page, TimeoutError
import pytest


def test_dynamic_class(page: Page):
    page.goto("http://uitestingplayground.com/hiddenlayers")

    green_btn = page.locator("button#greenButton")

    # First click works
    green_btn.click()

    # Second click should fail because the button is hidden
    with pytest.raises(TimeoutError):
        green_btn.click(timeout=2000)