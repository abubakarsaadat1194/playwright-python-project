import pytest
from playwright.sync_api import Playwright, APIRequestContext
from creds import *


# -------------------------------------------------------------
# Fixture: Create API request context for GitHub API
# -------------------------------------------------------------
# This fixture creates a reusable API client for the entire
# test session. It includes authentication headers and base URL.
# -------------------------------------------------------------
@pytest.fixture(scope="session")
def api_context(playwright: Playwright) -> APIRequestContext:

    context = playwright.request.new_context(
        base_url="https://api.github.com",
        extra_http_headers={
            # Required GitHub API header
            "Accept": "application/vnd.github.v3+json",

            # GitHub Personal Access Token authentication
            "Authorization": f"token {GITHUB_ACCESS_TOKEN}",
        }
    )

    yield context

    # Cleanup after all tests finish
    context.dispose()


# -------------------------------------------------------------
# Fixture: Automatically create and delete a test repository
# -------------------------------------------------------------
# autouse=True means this runs automatically before tests
# and deletes the repository after the session completes.
# -------------------------------------------------------------
@pytest.fixture(scope="session", autouse=True)
def create_test_repository(api_context: APIRequestContext):

    print("\nCreating test repository...")

    # Create repository
    api_response = api_context.post(
        "/user/repos",
        data={
            "name": GITHUB_REPO
        }
    )

    # Verify repository creation succeeded
    assert api_response.ok, f"Repo creation failed: {api_response.text()}"

    yield

    print("\nDeleting test repository...")

    # Delete repository after tests finish
    delete_response = api_context.delete(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}"
    )

    # Verify repository deletion succeeded
    assert delete_response.ok, f"Repo deletion failed: {delete_response.text()}"