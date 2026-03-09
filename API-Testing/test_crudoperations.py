from playwright.sync_api import *
import pytest


@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com"
    )
    yield api_context
    api_context.dispose()


# ---------------------------------------------------
# GET: Search Users
# ---------------------------------------------------
def test_users_search(api_context: APIRequestContext):

    query = "John"

    response = api_context.get(f"/users/search?q={query}")

    assert response.status == 200

    users_data = response.json()

    print("Users found:", users_data["total"])

    for user in users_data["users"]:

        print("Checking user:", user["firstName"], user["lastName"])

        full_text = (
            user["firstName"]
            + user["lastName"]
            + user["maidenName"]
            + user["email"]
            + user["username"]
        ).lower()

        assert query.lower() in full_text


# ---------------------------------------------------
# POST: Create User
# ---------------------------------------------------
def test_create_user(api_context: APIRequestContext):

    response = api_context.post(
        "/users/add",
        headers={"Content-Type": "application/json"},
        data={
            "firstName": "Damien",
            "lastName": "Smith",
            "age": 27
        }
    )

    user_data = response.json()

    print("\nCreated user:", user_data)

    assert response.status == 200
    assert user_data["firstName"] == "Damien"
    assert user_data["lastName"] == "Smith"


# ---------------------------------------------------
# PUT: Update Entire User
# ---------------------------------------------------
def test_update_user(api_context: APIRequestContext):

    response = api_context.put(
        "/users/1",
        headers={"Content-Type": "application/json"},
        data={
            "firstName": "EmilyUpdated",
            "lastName": "JohnsonUpdated",
            "age": 30
        }
    )

    updated_user = response.json()

    print("\nUpdated user:", updated_user)

    assert response.status == 200
    assert updated_user["firstName"] == "EmilyUpdated"


# ---------------------------------------------------
# PATCH: Partial Update
# ---------------------------------------------------
def test_partial_update_user(api_context: APIRequestContext):

    response = api_context.patch(
        "/users/1",
        headers={"Content-Type": "application/json"},
        data={
            "age": 35
        }
    )

    patched_user = response.json()

    print("\nPatched user:", patched_user)

    assert response.status == 200
    assert patched_user["age"] == 35


# ---------------------------------------------------
# DELETE: Remove User
# ---------------------------------------------------
def test_delete_user(api_context: APIRequestContext):

    response = api_context.delete("/users/1")

    deleted_user = response.json()

    print("\nDeleted user:", deleted_user)

    assert response.status == 200
    assert deleted_user["isDeleted"] is True