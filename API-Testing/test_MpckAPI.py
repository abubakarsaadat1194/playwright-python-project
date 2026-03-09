from playwright.sync_api import Page
import json


def modify_user(route):

    # Step 1: Fetch the original response
    response = route.fetch()

    original_data = response.json()

    print("\n--- Original API Response ---")
    print(original_data)

    # Step 2: Modify the response
    mocked_data = original_data.copy()

    mocked_data["firstName"] = "Automation"
    mocked_data["lastName"] = "Tester"

    print("\n--- Mocked API Response ---")
    print(mocked_data)

    # Step 3: Send modified response
    route.fulfill(
        response=response,
        body=json.dumps(mocked_data)
    )


def test_modify_user(page: Page):

    page.route("**/users/1", modify_user)

    page.goto("https://dummyjson.com/users/1")