from playwright.sync_api import Page, expect, Request, Response, Route


# -------------------------------------------------------
# Capture outgoing network requests
# -------------------------------------------------------
def on_request(request: Request):
    print(f"\n➡️ Request made:")
    print(f"URL: {request.url}")
    print(f"Method: {request.method}")
    print(f"Headers: {request.headers}")


# -------------------------------------------------------
# Capture incoming responses
# -------------------------------------------------------
def on_response(response: Response):
    print(f"\n⬅️ Response received:")
    print(f"URL: {response.url}")
    print(f"Status: {response.status}")
    print(f"Content-Type: {response.headers.get('content-type')}")


# -------------------------------------------------------
# Intercept and modify requests
# -------------------------------------------------------
def on_route(route: Route):

    request = route.request

    # Example 1: Block images
    if request.resource_type == "image":
        print(f"🚫 Blocking image: {request.url}")
        route.abort()
        return

    # Example 2: Modify request headers
    if "playwright.dev" in request.url:
        headers = request.headers.copy()
        headers["X-Test-Automation"] = "Playwright-Python"

        print(f"✏️ Modifying headers for {request.url}")

        route.continue_(headers=headers)
        return

    # Example 3: Mock API response
    if "api" in request.url:

        print("🎭 Mocking API response")

        route.fulfill(
            status=200,
            content_type="application/json",
            body='{"message":"Mocked API response from Playwright"}'
        )
        return

    # Example 4: Redirect request
    if "old-endpoint" in request.url:

        print("🔁 Redirecting request")

        route.continue_(
            url="https://playwright.dev/python/docs/intro"
        )
        return

    # Default behavior
    route.continue_()


# -------------------------------------------------------
# Test Example
# -------------------------------------------------------
def test_docs_link(page: Page):

    # Listen to network events
    page.on("request", on_request)
    page.on("response", on_response)

    # Intercept requests
    page.route("**/*", on_route)

    # Navigate to Playwright docs
    page.goto("https://playwright.dev/python")

    docs_link = page.get_by_role("link", name="Docs")

    docs_link.click()

    expect(page).to_have_url("https://playwright.dev/python/docs/intro")