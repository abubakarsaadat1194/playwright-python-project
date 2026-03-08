from playwright.sync_api import Page, expect
import pytest


def test_UIAction(page: Page):
    page.goto("http://uitestingplayground.com/")
    Progress_button=page.get_by_role("link", name="Progress Bar")
    Progress_button.click()
    Start_btn=page.get_by_role("button", name="Start")
    Stop_btn = page.get_by_role("button", name="Stop")
    progress_bar=page.get_by_role("progressbar")
    Start_btn.click()
    while(int(progress_bar.inner_text().replace("%","")) < 75):
        pass
    Stop_btn.click()
    print(f"progress bar is {progress_bar.inner_text()}")
    
