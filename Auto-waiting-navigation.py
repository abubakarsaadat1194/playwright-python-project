from playwright.sync_api import sync_playwright
from time import perf_counter

"""
This script measures how long a page takes to load using different
Playwright navigation waiting strategies.

It includes:
1. Default navigation behavior (no wait_until specified)
2. commit
3. domcontentloaded
4. load
5. networkidle
"""

# Different navigation strategies
wait_states = [
    "default",
    "commit",
    "domcontentloaded",
    "load",
    "networkidle"
]

with sync_playwright() as p:

    for state in wait_states:

        print(f"\nLoading page using strategy: {state}")

        browser = p.chromium.launch(
            headless=False,
            slow_mo=500
        )

        page = browser.new_page()

        # Start timer
        start_time = perf_counter()

        # Default navigation (no wait_until parameter)
        if state == "default":
            page.goto("https://playwright.dev/")
        else:
            page.goto("https://playwright.dev/", wait_until=state)

        # Calculate load time
        load_time = perf_counter() - start_time

        print(f"Page loaded in {round(load_time, 2)} seconds")

        browser.close()