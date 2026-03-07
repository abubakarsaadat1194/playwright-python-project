from playwright.sync_api import sync_playwright

"""
This script demonstrates how to listen to different Playwright page events.

Events are useful for:
- debugging network activity
- monitoring navigation
- handling file uploads
- observing browser lifecycle actions

Each event triggers a callback function that prints information
when the event occurs.
"""

# -------------------------
# Event Callback Functions
# -------------------------

def on_load(page):
    """Triggered when the page 'load' event fires."""
    print("Page finished loading:", page.url)


def on_close(page):
    """Triggered when the page is closed."""
    print("Page has been closed.")


def on_request(request):
    """
    Triggered whenever the page sends a network request.
    Useful for monitoring API calls.
    """
    print("Request sent:", request.method, request.url)


def on_response(response):
    """
    Triggered when the browser receives a response from the server.
    """
    print("Response received:", response.status, response.url)


def on_domcontentloaded(page):
    """
    Fired when the DOMContentLoaded event occurs,
    meaning the HTML document has been fully parsed.
    """
    print("DOM fully loaded for:", page.url)


def on_filechooser(file_chooser):
    """
    Triggered when a file upload dialog opens.
    We can automatically upload a file using set_files().
    """
    print("File chooser opened")
    file_chooser.set_files("input_files.py")


def on_console(message):
    """
    Triggered when a console message appears in the browser.
    Useful for debugging JavaScript logs.
    """
    print("Console message:", message.text)


def on_pageerror(error):
    """
    Triggered when a JavaScript error occurs in the page.
    """
    print("Page JavaScript error:", error)


# List of events to demonstrate
events = [
    "load",
    "domcontentloaded",
    "request",
    "response",
    "console",
    "pageerror",
    "filechooser",
    "close"
]


with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # Register event listeners
    page.on("load", lambda _: on_load(page))
    page.on("domcontentloaded", lambda _: on_domcontentloaded(page))
    page.on("request", on_request)
    page.on("response", on_response)
    page.on("console", on_console)
    page.on("pageerror", on_pageerror)
    page.on("filechooser", on_filechooser)
    page.on("close", lambda _: on_close(page))

    # Navigate to example site
    page.goto("https://bootswatch.com/default")

    # Trigger file chooser event
    file_input = page.get_by_label("Default file input example")
    file_input.click()

    # Close browser
    browser.close()