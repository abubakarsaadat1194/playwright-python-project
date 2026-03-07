from playwright.sync_api import sync_playwright


"""
Title: Gmail Inbox Unread Email Extractor

Description:
This script uses Playwright to open Gmail and extract information
from unread emails directly from the inbox view.

It prints:
- Sender
- Subject
- Preview text

The script does NOT open the email messages.
"""


def run():

    with sync_playwright() as p:

        # Launch browser
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000,
            args=[
                "--disable-dev-shm-usage",
                "--disable-blink-features=AutomationControlled"
            ]
        )

        # Load saved Gmail session
        context = browser.new_context(
            viewport={"width": 820, "height": 900},
            storage_state="playwright/auth/session.json"
        )

        page = context.new_page()

        # Open Gmail inbox
        page.goto("https://mail.google.com/mail/u/0/#inbox", wait_until="load")


        # Select unread emails
        email_count = page.locator("//tr[@tabindex='-1']").count()

        print("\nemails found:", email_count)

        print("\n---- Unread Email Summary ----")
        i=0
        emails=page.locator("div.UI table tr")
        for email in emails.all():
            
            is_new_email=email.locator("td li[data-tooltip='Mark as read']").count()==1
            if is_new_email:
                i=i+1
                sender = email.locator("span").nth("2").get_attribute("name")
                sender_email = email.locator("span").nth("2").get_attribute("email")
                subject = email.locator("span.bog").text_content()
                preview = email.locator("span.y2").inner_text()
            
                print("-----------------------")
                print("Sender :", sender)
                print("Sender email :", sender_email)
                print("Subject :", subject)
                print("Preview:", preview)
                print("-----------------------")
                

        print("\nFinished scanning inbox.")
        print(f"There were {i} unread emails")
        context.close()


if __name__ == "__main__":
    run()