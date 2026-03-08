from playwright.sync_api import Page, expect, TimeoutError
import pytest


def test_UIAction(page: Page):
    page.goto("http://uitestingplayground.com/")
    sapp_button=page.get_by_role("link", name="Sample App")
    sapp_button.click()
    input=page.get_by_placeholder("User Name")
    username="test"
    pswd="pwd"
    password=page.get_by_placeholder("********")
    input.fill(username)
    password.fill(pswd)
    loginbtn=page.get_by_role("button",name="Log In")
    loginbtn.click()
    success_status=page.locator("label#loginstatus")
    
    expect(success_status).to_have_text(f"Welcome, {username}!")
