from playwright.sync_api import Page, Locator


class PlaywrightPage:

    URL = "https://playwright.dev/python"

    def __init__(self, page: Page):
        self.page = page

        self.docs_link = page.get_by_role("link", name="Docs")
        self.search_input = page.get_by_placeholder("Search docs")

    def open(self):
        self.page.goto(self.URL)

    def visit_docs(self):
        self.docs_link.click()

    def search(self, query: str):
        self.page.keyboard.press("Control+KeyK")
        self.search_input.fill(query)

    def search_results(self) -> Locator:
        return self.page.locator("div.DocSearch-Dropdown")