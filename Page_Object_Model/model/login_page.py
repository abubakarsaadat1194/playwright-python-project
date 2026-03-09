from playwright.sync_api import Page


class LoginPage:

    URL = "http://uitestingplayground.com/sampleapp"

    def __init__(self, page: Page):
        self.page = page
        self.page.goto(self.URL)

        self.username_input = page.get_by_placeholder("User Name")
        self.password_input = page.get_by_placeholder("********")
        self.login_btn = page.get_by_role("button", name="Log In")
        self.label = page.locator("#loginstatus")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()