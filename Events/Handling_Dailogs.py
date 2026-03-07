from playwright.sync_api import sync_playwright

"""
This script demonstrates how to handle JavaScript dialogs in Playwright.

The page contains three buttons that trigger:
1. Alert dialog
2. Confirm dialog
3. Prompt dialog

The script listens for the 'dialog' event and performs different actions
depending on the dialog type.

Special behavior:
The confirm dialog will be CANCELLED the first time it appears,
and ACCEPTED if it appears again.
"""

# Buttons that trigger dialogs
buttons = [
    "Show alert box",
    "Show confirm box",
    "Show confirm box",  # clicking twice to show cancel once and accept next
    "Show prompt box"
]

# Variable to track if confirm dialog has already been cancelled
confirm_cancelled = False


def handle_dialog(dialog):
    """
    Event handler for all JavaScript dialogs.

    Parameters
    ----------
    dialog : playwright.sync_api.Dialog
        The dialog object representing the alert/confirm/prompt window.
    """

    global confirm_cancelled

    print("\nDialog opened")
    print("Dialog type:", dialog.type)
    print("Dialog message:", dialog.message)

    # Handle ALERT dialog
    if dialog.type == "alert":
        print("Accepting alert dialog")
        dialog.accept()

    # Handle CONFIRM dialog
    elif dialog.type == "confirm":

        if not confirm_cancelled:
            print("Cancelling confirm dialog (first time)")
            dialog.dismiss()  # equivalent to clicking "Cancel"
            confirm_cancelled = True
        else:
            print("Accepting confirm dialog")
            dialog.accept()

    # Handle PROMPT dialog
    elif dialog.type == "prompt":
        print("Sending text to prompt dialog")
        dialog.accept("Playwright is cool with Python")


with sync_playwright() as p:

    # Launch browser
    browser = p.chromium.launch(
        headless=False,
        slow_mo=1500
    )

    page = browser.new_page()

    # Register dialog event listener
    page.on("dialog", handle_dialog)

    # Open the demo alerts page
    page.goto("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

    # Click each button that triggers a dialog
    for button in buttons:
        print(f"\nClicking button: {button}")

        dialog_button = page.get_by_text(button)
        dialog_button.click()

    # Close browser
    browser.close()