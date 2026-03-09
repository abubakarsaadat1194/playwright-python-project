from playwright.sync_api import Page, expect
from model.login_page import LoginPage


def test_successful_login(page: Page):

    username = "test"
    pswd = "pwd"

    login_page = LoginPage(page)

    login_page.login(username, pswd)

    expect(login_page.label).to_have_text(f"Welcome, {username}!")


def test_failed_login(page: Page):

    username = "test"
    pswd = "pwdfff"

    login_page = LoginPage(page)

    login_page.login(username, pswd)

    expect(login_page.label).to_have_text("Invalid username/password")