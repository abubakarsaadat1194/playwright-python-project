from playwright.sync_api import Page, expect
import pytest


def test_UIAction(page: Page):
    page.goto("http://uitestingplayground.com/")
    dynmic_table_btn=page.get_by_role("link", name="Dynamic Table")
    dynmic_table_btn.click()

    label=page.locator("p.bg-warning").inner_text()
    percentage = label.split()[-1]
    column_headers = page.get_by_role("columnheader")
    cpu_column=None

    for index in range(column_headers.count()):
        column_header = column_headers.nth(index)
        if column_header.inner_text() == "CPU":
            cpu_column = index
            break

    assert cpu_column!=None
    row_group =page.get_by_role("rowgroup").last
    chrome_row=page.get_by_role("row").filter(
        has_text="Chrome"
    )
    chrome_cpu= chrome_row.get_by_role("cell").nth(cpu_column)

    assert percentage==chrome_cpu.inner_text()