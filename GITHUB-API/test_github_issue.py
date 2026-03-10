from creds import *
from playwright.sync_api import APIRequestContext, Page


# ------------------------------------------------------------
# Test: Create a new GitHub Issue using the API
# ------------------------------------------------------------
# This test verifies that a new issue can be created successfully
# in the test repository using the GitHub REST API.
# ------------------------------------------------------------
def test_create_issue(api_context: APIRequestContext):

    issue_data = {
        "title": "[BUG] Something Went Wrong",
        "body": "When performing this action, the application failed."
    }

    # Send POST request to create an issue
    post_response = api_context.post(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues",
        data=issue_data
    )

    # Verify request succeeded
    assert post_response.ok, f"Issue creation failed: {post_response.text()}"

    issue = post_response.json()

    # Validate response data
    assert issue["title"] == issue_data["title"]
    assert issue["body"] == issue_data["body"]

    print("\nCreated issue:", issue["html_url"])


# ------------------------------------------------------------
# Test: Capture Screenshot of GitHub Issues Page
# ------------------------------------------------------------
# This test uses Playwright UI automation to open the repository
# issues page and capture a full-page screenshot.
# ------------------------------------------------------------
def test_take_issue_screenshot(page: Page):

    issues_url = f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/issues"

    page.goto(issues_url)

    # Capture screenshot of the entire page
    page.screenshot(
        path="issues-page.jpg",
        full_page=True
    )

    print("\nScreenshot saved: issues-page.jpg")


# ------------------------------------------------------------
# Test: Verify Newly Created Issue Exists
# ------------------------------------------------------------
# This test fetches all repository issues via API and verifies
# that the issue created in the previous test exists.
# ------------------------------------------------------------
def test_new_issue_in_repo(api_context: APIRequestContext):

    # Get all issues in the repository
    all_issues_response = api_context.get(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues"
    )

    assert all_issues_response.ok, "Failed to retrieve issues"

    issues = all_issues_response.json()

    # Find the issue with the expected title
    matching_issues = [
        issue for issue in issues
        if issue["title"] == "[BUG] Something Went Wrong"
    ]

    # Ensure at least one matching issue exists
    assert matching_issues, "Created issue not found in repository"

    new_issue = matching_issues[0]

    # Validate issue body
    assert new_issue["body"] == "When performing this action, the application failed."

    print("\nVerified issue:", new_issue["html_url"])