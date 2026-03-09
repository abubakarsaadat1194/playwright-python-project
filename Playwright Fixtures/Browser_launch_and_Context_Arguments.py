import pytest
from playwright.sync_api import Page, Browser, BrowserContext, Playwright, expect


# -------------------------------
# Browser Launch Configuration
# -------------------------------
@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False,
        "slow_mo": 50,
        "args": [
            "--disable-dev-shm-usage",
            "--disable-blink-features=AutomationControlled",
            "--start-maximized",
            "--disable-infobars",
            "--disable-notifications"
        ],
            
    }

@pytest.fixture(scope="session")
def browser_name():
    return "firefox"
# -------------------------------
# Browser Context Configuration
# -------------------------------
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
        # Uncomment when storage state is created
        # "storage_state": "storage/google_auth.json",
    }


# -------------------------------
# Base URL Fixture
# -------------------------------
@pytest.fixture(scope="session")
def base_url():
    return "https://playwright.dev/python"


# -------------------------------
# Page Fixture with Default Setup
# -------------------------------
@pytest.fixture(scope="function")
def app_page(page: Page, base_url):
    page.goto(base_url)
    return page


# -------------------------------
# Storage State Fixture
# -------------------------------
@pytest.fixture(scope="session")
def google_storage_state(playwright: Playwright):
    """
    Creates a storage state file after authenticating with Google.
    This allows tests to run with an already logged-in session.
    """

    browser = playwright.chromium.launch(headless=False,
            slow_mo=1000,
            args=[
                "--disable-dev-shm-usage",
                "--disable-blink-features=AutomationControlled"
            ])
    context = browser.new_context()

    page = context.new_page()

    # Google sign in page
    page.goto("https://accounts.google.com/")

    print("Please login manually to Google...")
    page.wait_for_timeout(60000)

    # Save authenticated session
    context.storage_state(path="storage/google_auth.json")

    context.close()
    browser.close()

    return "storage/google_auth.json"


# -------------------------------
# Authenticated Context Fixture
# -------------------------------
@pytest.fixture(scope="session")
def authenticated_context(playwright: Playwright, google_storage_state):
    browser = playwright.chromium.launch(headless=False,
            slow_mo=1000,
            args=[
                "--disable-dev-shm-usage",
                "--disable-blink-features=AutomationControlled"
            ])       

    context = browser.new_context(
        storage_state=google_storage_state
    )

    yield context

    context.close()
    browser.close()


# -------------------------------
# Authenticated Page Fixture
# -------------------------------
@pytest.fixture(scope="function")
def authenticated_page(authenticated_context: BrowserContext):
    page = authenticated_context.new_page()
    yield page
    page.close()


# -------------------------------
# Test Example
# -------------------------------
def test_page_has_docs_link(app_page: Page):

    docs_link = app_page.get_by_role("link", name="Docs")

    expect(docs_link).to_be_visible()


# -------------------------------
# Example Authenticated Test
# -------------------------------
def test_google_account_page(authenticated_page: Page):

    authenticated_page.goto("https://myaccount.google.com/")

    expect(authenticated_page).to_have_title("Google Account")