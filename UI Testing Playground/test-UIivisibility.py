from playwright.sync_api import Page, expect, TimeoutError
import pytest


def test_UIAction(page: Page):
    page.goto("http://uitestingplayground.com/")
    vis_button=page.get_by_role("link", name="Visibility")
    vis_button.click()
    hide_button=page.get_by_role("button",name="Hide")
    Removed_button=page.get_by_role("button",name="Removed")
    ZeroWidth_button=page.get_by_role("button",name="Zero Width")
    Overlapped_button=page.get_by_role("button",name="Overlapped")
    Opacity_button=page.get_by_role("button",name="Opacity 0")
    Visibility_button=page.get_by_role("button",name="Visibility Hidden")
    Display_button=page.get_by_role("button",name="Display None")
    Offscreen_button=page.get_by_role("button",name="Offscreen")


    hide_button.click()

    expect(Removed_button).to_be_hidden()
    expect(ZeroWidth_button).to_have_css("width", "0px")
    with pytest.raises(TimeoutError):
        Overlapped_button.click(timeout=2000)                                     
    expect(Opacity_button).to_have_css("opacity", "0")

    expect(Visibility_button).to_be_hidden()
    expect(Offscreen_button).not_to_be_in_viewport()