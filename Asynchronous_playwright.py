import asyncio
from playwright.async_api import async_playwright

"""
This script demonstrates basic browser automation using the
Playwright Async API.

Steps performed:
1. Launch a Chromium browser.
2. Open a new browser page (tab).
3. Navigate to a website.
4. Retrieve and print the page title.
5. Close the browser.

The script uses Python's asyncio framework because Playwright's
async API relies on asynchronous operations.
"""


async def main():
    """
    Main asynchronous function that runs the browser automation.
    """

    # Start Playwright
    async with async_playwright() as p:

        # Launch Chromium browser
        browser = await p.chromium.launch(
            headless=False  # Set to True to run without UI
        )

        # Create a new browser tab
        page = await browser.new_page()

        # Target URL
        url = "https://www.unsplash.com"

        # Navigate to the webpage
        await page.goto(url)

        # Retrieve page title
        title = await page.title()

        # Print page title in terminal
        print("Page Title:", title)

        # Close browser after completion
        await browser.close()


# Run the asynchronous program
asyncio.run(main())