from playwright.sync_api import sync_playwright
from time import perf_counter

"""
This script demonstrates different ways of waiting for elements
to appear on a dynamically loaded webpage.

The target page loads movie data via AJAX after clicking a year link.
We measure how long it takes for the movie table to appear using
different Playwright waiting strategies.
"""

# Different element waiting strategies
wait_states = [
    "default",            # No explicit wait
    "visible",            # Wait until element becomes visible
    "attached",           # Wait until element is attached to DOM
    "wait_for_selector"   # Explicit Playwright selector wait
]

URL = "https://www.scrapethissite.com/pages/ajax-javascript/"

with sync_playwright() as p:

    for wait_state in wait_states:

        print(f"\nLoading movies using wait strategy: {wait_state}")

        # Launch Chromium browser
        browser = p.chromium.launch(
            headless=False,   # Show browser window
            slow_mo=500       # Slow actions for visualization
        )

        # Create a new browser tab
        page = browser.new_page()

        # Start performance timer
        start_time = perf_counter()

        # Navigate to AJAX movie page
        page.goto(URL)

        # Click the "2015" year link which triggers AJAX loading
        year_link = page.get_by_role("link", name="2015")
        year_link.click()

        # Locator for the first movie title in the table
        film_title = page.locator("td.film-title").first

        # Apply different waiting strategies
        if wait_state == "default":
            # No explicit waiting
            # Playwright auto-waiting handles most actions
            pass

        elif wait_state == "wait_for_selector":
            # Explicitly wait until selector appears in the DOM
            page.wait_for_selector("td.film-title")

        else:
            # Wait for element state using locator.wait_for()
            film_title.wait_for(state=wait_state)

        # Stop timer
        load_time = perf_counter() - start_time

        print(f"Movies loaded in {round(load_time, 2)} seconds")

        # Close browser
        browser.close()