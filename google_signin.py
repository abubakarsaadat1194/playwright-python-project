from playwright.sync_api import sync_playwright

"""
Title: Playwright Authentication Session Reuse Example

Description
-----------
This script demonstrates how to launch a browser using Playwright
and reuse a previously saved authentication session.

Instead of logging in every time, Playwright can load stored cookies
and session data from a JSON file. This allows automated scripts to
start with an already authenticated state.

Key Concepts Demonstrated
-------------------------
1. Launching a browser with custom startup arguments
2. Creating a browser context with a saved authentication state
3. Opening and navigating a page
4. Saving the updated session state
5. Using Playwright's debugging tools (page.pause)

Prerequisite
------------
A valid session file must exist at:

playwright/auth/session.json

This file contains cookies and storage data from a previous login.
"""


def run():
    """Main function that runs the Playwright automation script."""

    with sync_playwright() as p:

        # -----------------------------------------------------------
        # Launch Chromium Browser
        # -----------------------------------------------------------
        # headless=False -> opens a visible browser window
        # slow_mo -> slows down actions for easier debugging
        # args -> disables certain automation detection features
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000,
            args=[
                "--disable-dev-shm-usage",
                "--disable-blink-features=AutomationControlled"
            ]
        )

        # -----------------------------------------------------------
        # Create Browser Context
        # -----------------------------------------------------------
        # Browser contexts act like separate browser profiles.
        # storage_state loads cookies/local storage from a file,
        # allowing reuse of an authenticated session.
        context = browser.new_context(
            viewport={"width": 820, "height": 920}

        )

        # Open a new browser tab
        page = context.new_page()

        # -----------------------------------------------------------
        # Navigate to Google Accounts
        # -----------------------------------------------------------
        page.goto("https://accounts.google.com")

        # Print the page title for confirmation
        print("Page title:", page.title())

        # -----------------------------------------------------------
        # Optional Login Steps (commented for session reuse)
        # -----------------------------------------------------------
        # If a session file does not exist, you can use the code below
        # to log in manually and then save the session.

        
        email_input = page.locator("input[name='identifier']")
        email_input.fill("abubakar.saadat.qa@gmail.com")

        next_button = page.get_by_role("button", name="Next")
        next_button.click()

        # Pause the script to allow manual password entry
        page.pause()
        

        # -----------------------------------------------------------
        # Save Updated Authentication State
        # -----------------------------------------------------------
        # This writes cookies and local storage data to a JSON file.
        context.storage_state(path="playwright/auth/session.json")

        print("Session state saved successfully.")

        # Close browser context and browser
        context.close()
        browser.close()


# Run the automation script
if __name__ == "__main__":
    run()