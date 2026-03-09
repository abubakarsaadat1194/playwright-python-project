from playwright.sync_api import Page, Route


def modify_response(route: Route):

    # Step 1: fetch original response
    response = route.fetch()

    # Step 2: read response body
    html = response.text()

    # Step 3: modify HTML
    modified_html = html.replace(
        "<h1>Welcome</h1>",
        "<h1>Welcome Automation Engineer</h1>"
    )

    # Step 4: send modified response
    route.fulfill(
        response=response,
        body=modified_html
    )


def test_modify_heading(page: Page):

    page.route("**/sampleapp", modify_response)

    page.goto("http://uitestingplayground.com/sampleapp")