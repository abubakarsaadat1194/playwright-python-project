from playwright.sync_api import sync_playwright

"""
This script demonstrates how to handle file downloads in Playwright.

Steps performed:
1. Open the Unsplash website.
2. Click an image to open its detail page.
3. Click the "Download free" button.
4. Capture the download event.
5. Save the downloaded file locally.

Playwright provides built-in mechanisms such as:
- page.expect_download()
- download.save_as()

These allow us to reliably capture and control file downloads.
"""


def handle_download(download):
    """
    Callback function triggered when a download starts.

    Parameters
    ----------
    download : playwright.sync_api.Download
        Represents the file being downloaded.

    The function prints information about the download and
    saves the file locally.
    """

    # Print information about the downloaded file
    print("Download started...")
    print("File URL:", download.url)
    print("Suggested filename:", download.suggested_filename)

    # Save the file locally using the suggested filename
    download.save_as(download.suggested_filename)

    print("Download saved successfully.")


with sync_playwright() as p:

    # Launch Chromium browser
    browser = p.chromium.launch(
        headless=False,  # Show browser UI
        slow_mo=1500     # Slow actions for visibility
    )

    # Open a new page
    page = browser.new_page()

    # Navigate to Unsplash free images page
    page.goto("https://unsplash.com/s/photos/free")

    # Click an image to open its detail page
    image = page.get_by_alt_text(
        "silhouette of person standing on rock surrounded by body of water"
    )
    image.click()

    # Locate the download button
    download_button = page.get_by_role("link", name="Download free")

    # Listen for the download event once
    page.once("download", handle_download)

    # Expect the download to start after clicking the button
    with page.expect_download() as download_info:
        download_button.click()

    # Get the download object
    download = download_info.value

    # Print confirmation
    print("Download completed:", download.suggested_filename)

    # Close browser
    browser.close()