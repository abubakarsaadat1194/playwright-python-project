from model.playwright_login import PlaywrightPage
from playwright.sync_api import Page, expect


def test_docs_link(page: Page):

    playwrightpage = PlaywrightPage(page)

    playwrightpage.open()
    playwrightpage.visit_docs()


def test_docs_search(page: Page):

    playwrightpage = PlaywrightPage(page)

    playwrightpage.open()
    playwrightpage.visit_docs()

    playwrightpage.search("assertions")

    expect(playwrightpage.search_results()).to_contain_text("List of assertions")