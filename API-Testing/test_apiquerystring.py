from playwright.sync_api import *
import pytest

@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com")
    yield api_context
    api_context.dispose()

def test_users_search(api_context: APIRequestContext):
    query= "John"
    response=api_context.get(f"/users/search?q={query}")
    assert response.status == 200
    users_data= response.json()
    print("Users found:", users_data["total"])

    for user in users_data["users"]:
        print("Checking user:", user["firstName"])
        print("Checking user:", user["firstName"], user["lastName"])

        full_text = (
            user["firstName"]
            + user["lastName"]
            + user["maidenName"]
            + user["email"]
            + user["username"]
        ).lower()
        assert query.lower() in full_text