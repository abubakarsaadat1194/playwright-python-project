from playwright.sync_api import Page, expect


def test_load_delay_button(page: Page):

    page.goto("http://uitestingplayground.com/")

    load_delay_link = page.get_by_role("link", name="Load Delay")
    load_delay_link.click()

    button_after_delay = page.get_by_role(
        "button",
        name="Button Appearing After Delay"
    )

    button_after_delay.wait_for(state="visible")

    expect(button_after_delay).to_be_visible()

    button_after_delay.click()