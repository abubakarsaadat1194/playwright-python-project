# Playwright Automation with Python - From A to Z

## Table of Contents

- [Playwright Python Setup Guide](#playwright-python-setup-guide)
  - [1. Install Python](#1-install-python)
  - [2. Create a Project Folder](#2-create-a-project-folder)
  - [3. Create a Virtual Environment (Recommended)](#3-create-a-virtual-environment-recommended)
  - [4. Install Playwright](#4-install-playwright)
  - [5. Install Browsers for Playwright](#5-install-browsers-for-playwright)
  - [6. Create a Sample Test](#6-create-a-sample-test)
  - [7. Run the Test](#7-run-the-test)
  - [8. Install Playwright Code Generator](#8-install-playwright-code-generator-optional-but-powerful)

---

- [How to Open Terminal in Visual Studio Code](#how-to-open-terminal-in-visual-studio-code)

- [Fix: Python Cannot Find test.py (Playwright)](#fix-python-cannot-find-testpy-playwright)

- [Fix: zsh: command not found: code](#fix-zsh-command-not-found-code)

- [How to Open an Interactive Playwright REPL on macOS](#how-to-open-an-interactive-playwright-repl-on-macos)

- [How to Clear the Terminal in Visual Studio Code](#how-to-clear-the-terminal-in-visual-studio-code)

---

# Playwright Locators

- [Playwright Locator: get_by_role() Example](#playwright-locator-get_by_role-example)
- [Playwright Locator: get_by_label() and get_by_placeholder()](#playwright-locator-get_by_label-and-get_by_placeholder)
- [Playwright Locator: get_by_text()](#playwright-locator-get_by_text)
- [Playwright Locator: get_by_alt_text()](#playwright-locator-get_by_alt_text)
- [Playwright Locator: get_by_title()](#playwright-locator-get_by_title)

---

# CSS Selectors in Playwright

- [Playwright Locators Using CSS Selectors](#playwright-locators-using-css-selectors)
- [Playwright CSS Hierarchy Selectors](#playwright-css-hierarchy-selectors)
- [Playwright CSS Pseudo-Classes](#playwright-css-pseudo-classes)

---

# XPath in Playwright

- [Playwright Locators Using XPath](#playwright-locators-using-xpath)
- [Playwright XPath Functions: text() and contains()](#playwright-xpath-functions-text-and-contains)

---

# Advanced Locator Techniques

- [Playwright Miscellaneous Selectors](#playwright-miscellaneous-selectors)

---

# User Interaction Automation

- [Playwright Mouse Actions](#playwright-mouse-actions)
- [Playwright Write Text Functions](#playwright-write-text-functions)
- [Playwright Radio Buttons, Switches, and Checkboxes](#playwright-radio-buttons-switches-and-checkboxes)
- [Playwright Dropdown and Multi-Select](#playwright-dropdown-and-multi-select)
- [Playwright Dropdown Links](#playwright-dropdown-links)

---

# File Handling

- [Playwright File Inputs and File Uploads](#playwright-file-inputs-and-file-uploads)
- [Playwright Handling File Downloads](#playwright-handling-file-downloads)

---

# Keyboard Automation

- [Playwright Keyboard Shortcuts](#playwright-keyboard-shortcuts)

---

# Waiting Strategies

- [Playwright Navigation Wait States (`wait_until`)](#playwright-navigation-wait-states-wait_until)
- [Playwright Custom Wait States](#playwright-custom-wait-states)

---

# Browser Events and Dialogs

- [Playwright Event Listeners](#playwright-event-listeners)
- [Playwright Handling JavaScript Dialogs](#playwright-handling-javascript-dialogs)

---

# Playwright APIs

- [Playwright Synchronous vs Asynchronous API](#playwright-synchronous-vs-asynchronous-api)

---

# Authentication

- [Playwright Authentication: Reusing Login Session with storage_state](#playwright-authentication-reusing-login-session-with-storage_state)
# Playwright Python Setup Guide

This guide explains how to install and configure **Playwright with Python** on macOS.

---

# 1. Install Python

First check if Python is already installed.

```bash
python3 --version
```

If you see a version like **Python 3.10+**, Python is already installed.

If not, install it using **Homebrew**:

```bash
brew install python
```

Or download it from the official website:

➡️ https://www.python.org/

After installing, verify the installation:

```bash
python3 --version
pip3 --version
```

---

# 2. Create a Project Folder

Create a folder for your Playwright project.

```bash
mkdir playwright-python-project
cd playwright-python-project
```

---

# 3. Create a Virtual Environment (Recommended)

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Your terminal should now show:

```
(venv)
```

---

# 4. Install Playwright

Install the Playwright Python package:

```bash
pip install playwright
```

This installs the **Playwright automation library** for Python.

---

# 5. Install Browsers for Playwright

Playwright requires its own browser binaries.

Run:

```bash
playwright install
```

This installs the following browsers:

- Chromium
- Firefox
- WebKit

---

# 6. Create a Sample Test

Create a file called:

```
test_playwright.py
```

Add the following code:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://playwright.dev/python")
    docs_button = page.get_by_role('link',name="Docs")
    docs_button.click()
    print("Docs=", page.url)
    print(page.title())
    browser.close()
```

---

# 7. Run the Test

Run the script using:

```bash
python test_playwright.py
```

A browser window should open automatically 🌐.

---

# 8. Install Playwright Code Generator (Optional but Powerful)

Playwright can record browser actions and generate automation code.

Run:

```bash
playwright codegen https://example.com
```

This will open a browser and generate automation scripts based on your actions.

---

✅ **Your Playwright Python environment is now ready!**
# How to Open Terminal in Visual Studio Code

Opening the **Terminal in Visual Studio Code** is very easy. Here are the main methods. 💻

---

# 1. Keyboard Shortcut (Fastest) ⚡

Press:

```bash
Ctrl + `
```

The key **`** is the **backtick** (usually below the **ESC** key).

This will open the **integrated terminal** at the bottom of VS Code.

To close it, press the same shortcut again.

---

# 2. From the Menu

1. Open **Visual Studio Code**
2. Click **Terminal** in the top menu
3. Click **New Terminal**

The terminal will appear at the bottom of the editor.

---

# 3. Using Command Palette

Press:

```bash
Cmd + Shift + P
```

(Mac)

Then type:

```
Terminal: New Terminal
```

Press **Enter**.

---

# 4. What Terminal Opens on Mac

On **macOS**, VS Code usually opens:

- `zsh` (default shell)
- or `bash`

Example terminal prompt:

```bash
abu@MacBook-Pro project-folder %
```

---

# 5. Open Terminal in Your Project Folder

1. Open your **project folder** in VS Code
2. Press:

```bash
Ctrl + `
```

The terminal automatically opens inside that folder.

Example:

```bash
cd playwright-python-project
```

---

# 6. Run Python or Playwright Commands

Once the terminal is open, you can run commands like:

```bash
python3 --version
```

```bash
playwright install
```

```bash
python test_playwright.py
```

---

# Pro Tip (Very Useful for Testing Projects) 🚀

You can open **multiple terminals** in VS Code.
# Fix: Python Cannot Find `test.py` (Playwright)

The error means **Python cannot find the file `test.py` in your current folder**.

This usually happens because:

- The file does not exist
- The file has a different name
- You are in the wrong directory

Let's fix it step-by-step. 🔧

---

# 1. Check What Files Exist in the Folder

Run the following command in your terminal:

```bash
ls
```

This lists all files inside your folder:

```
playwright-python-project
```

Example output:

```bash
venv
test_playwright.py
```

If you see:

```
test_playwright.py
```

Run:

```bash
python test_playwright.py
```

instead of:

```bash
python test.py
```

---

# 2. Create the Test File (If It Doesn't Exist)

If `ls` does not show any `.py` file, create one.

## Option A — Create it from Terminal

```bash
touch test.py
```

Open it in Visual Studio Code:

```bash
code test.py
```

Paste the following Playwright code:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()
```

Save the file.

---

# 3. Run the Script

Run:

```bash
python test.py
```

A browser should open automatically 🌐.

---

# 4. Confirm You Are in the Correct Folder

Check your current directory:

```bash
pwd
```

Expected output example:

```bash
/Users/abubakar/playwright-python-project
```

If not, navigate to the folder:

```bash
cd ~/playwright-python-project
```

---

# 5. Activate Virtual Environment Again (If Needed)

If `(venv)` disappears from your terminal, activate it again:

```bash
source venv/bin/activate
```

Your terminal should show:

```
(venv)
```

Now Playwright should run correctly.

---

# Fix: `zsh: command not found: code`

Example error:

```bash
(venv) abubakar@Abus-Air playwright-python-project % code test.py
zsh: command not found: code
```

This means the **VS Code terminal command is not added to your system PATH**.

This is common on macOS.

---

# Enable `code` Command in Terminal

## Step 1 — Open Visual Studio Code

Start **Visual Studio Code** normally from **Applications**.

---

## Step 2 — Open Command Palette

Press:

```bash
Cmd + Shift + P
```

---

## Step 3 — Search for the Command

Type:

```
Shell Command: Install 'code' command in PATH
```

Click it.

This installs the `code` command for the terminal.

---

## Step 4 — Restart Terminal

Close the terminal and open it again.

Then test:

```bash
code .
```

This opens your **current project folder** in VS Code.

---

# Open Your Test File

Inside your project folder run:

```bash
code test.py
```

Paste this Playwright example:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()
```

Save the file.

---

# Run the Test

```bash
python test.py
```

If everything works correctly:

- ✅ A browser window will open
- ✅ The script prints the page title

---

# Pro Tip (Recommended Workflow)

Instead of opening individual files, open the entire project:

```bash
code .
```

This loads the full folder:

```
playwright-python-project
```

into VS Code.

---

# How to Open an Interactive Playwright REPL on macOS

You can open a **Python REPL session** to test Playwright commands interactively.

This is useful for:

- Learning Playwright
- Debugging selectors
- Testing automation steps

---

# 1. Activate Virtual Environment

Go to your project folder:

```bash
cd ~/playwright-python-project
```

Activate the environment:

```bash
source venv/bin/activate
```

Example prompt:

```bash
(venv) abubakar@Abus-Air playwright-python-project %
```

---

# 2. Start Python REPL

Run:

```bash
python
```

You should see something like:

```bash
Python 3.11.x
>>>
```

This is the **Python interactive shell**.

---

# 3. Start Playwright Inside REPL

Enter the following commands step-by-step:

```python
from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://playwright.dev/")
link=page.get_by_role('link', name="GET STARTED")
link.highlight()
link.click()
browser.close()
playwright.stop()
```

Now you can test commands interactively.

Example:

```python
page.title()
```

or

```python
page.locator("h1").text_content()
```

---

# 4. Close the Browser

When finished:

```python
browser.close()
playwright.stop()
```

---

# 5. Exit the Python REPL

Press:

```bash
Ctrl + D
```

or type:

```python
exit()
```

---

# Alternative (Better for Learning Playwright)

Playwright provides a **code generator tool** that records browser actions.

Run:

```bash
playwright codegen https://example.com
```

This will:

- Open a browser
- Record your actions
- Generate Playwright code automatically

Example:

```bash
playwright codegen https://google.com
```

Click elements in the browser and **Playwright will generate Python automation code automatically**.

---

💡 **Useful for automation engineers building projects with:**

- Selenium
- Playwright
- Appium
- JMeter

Click the **"+" icon** in the terminal panel to create another terminal session.

---

✅ This is especially useful when working with **automation testing projects like Selenium, Playwright, or Appium**.
# Playwright Locator: `get_by_role()` Example

This example demonstrates how to use **Playwright's `get_by_role()` locator** to interact with elements on a webpage.

The example uses the website:

https://bootswatch.com/default

`get_by_role()` is recommended because it uses **accessible roles from the ARIA specification**, making tests more reliable and closer to how users interact with the page.

---

# Start Playwright in Python REPL

```python
from playwright.sync_api import sync_playwright
```
# Import the synchronous Playwright API to control browsers using Python.

```python
playwright = sync_playwright().start()
```
# Start the Playwright engine.  
# This initializes the Playwright driver and allows us to launch browsers.

```python
browser = playwright.chromium.launch(headless=False)
```
# Launch the Chromium browser.
# headless=False means the browser UI will be visible.

```python
page = browser.new_page()
```
# Create a new browser tab (page).

```python
url = "https://bootswatch.com/default"
```
# Store the target website URL in a variable.

```python
page.goto(url)
```
# Navigate the browser to the specified URL.

Example response returned by Playwright:

```
<Response url='https://bootswatch.com/default/' request=<Request url='https://bootswatch.com/default/' method='GET'>>
```

---

# Locate a Button Using Role

```python
button = page.get_by_role('button', name="Default button")
```
# Locate a button element using the ARIA role "button".
# The locator searches for a button with accessible name "Default button".

```python
button.highlight()
```
# Visually highlight the located element in the browser.
# Useful for debugging and learning.

```python
button.click()
```
# Click the located button element.

---

# Locate a Heading

Incorrect code example:

```python
heading 4 = page.get_by_role('heading', name="Heading 4")
```

This produces a **SyntaxError** because variable names cannot contain spaces.

Correct version:

```python
heading = page.get_by_role('heading', name="Heading 4")
```
# Locate a heading element with accessible name "Heading 4".

```python
heading.highlight()
```
# Highlight the heading element in the browser.

```python
heading.click()
```
# Click the heading element.

---

# Locate a Switch / Checkbox

Initial attempt:

```python
switchbox = page.get_by_role('switchbox', name="Default switch checkbox input")
```

```python
switchbox.highlight()
```

```python
switchbox.switch()
```

Error:

```
AttributeError: 'Locator' object has no attribute 'switch'
```

Reason:

- `switch()` is **not a valid Playwright method**
- The correct method to interact with checkboxes or switches is usually `.click()`

---

# Timeout Error

```python
switchbox.click()
```

Error example:

```
TimeoutError: Locator.click: Timeout 30000ms exceeded
```

Reason:

- The role **switchbox** does not exist
- Playwright cannot find the element

---

# Correct Locator

Use the correct ARIA role **checkbox**.

```python
switchbox = page.get_by_role('checkbox', name="Default switch checkbox input")
```
# Locate the checkbox element using role "checkbox".

```python
switchbox.highlight()
```
# Highlight the checkbox element for debugging.

```python
switchbox.click()
```
# Click the checkbox (toggle the switch).

---

# Key Learning Points

### 1️⃣ Use Accessible Roles

Preferred Playwright locators:

- `get_by_role()`
- `get_by_label()`
- `get_by_text()`
- `get_by_placeholder()`

These are more **stable than CSS/XPath selectors**.

---

### 2️⃣ Common Roles

Examples of roles:

| Role | Example |
|-----|------|
| button | Submit button |
| heading | Page headings |
| checkbox | Checkboxes |
| textbox | Input fields |
| link | Anchor links |

---

### 3️⃣ Debugging Tips

Helpful Playwright debugging commands:

```python
locator.highlight()
```

Highlight the element visually.

```python
locator.count()
```

Check how many elements match the locator.

```python
page.pause()
```

Open Playwright inspector for debugging.

---

# Example Final Working Code

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    button = page.get_by_role("button", name="Default button")
    button.click()

    heading = page.get_by_role("heading", name="Heading 4")
    heading.click()

    switchbox = page.get_by_role("checkbox", name="Default switch checkbox input")
    switchbox.click()

    browser.close()
```

---
# Playwright Locator: `get_by_label()` and `get_by_placeholder()`

This example demonstrates how to use Playwright's **`get_by_label()`** and **`get_by_placeholder()`** locators to identify form fields.

Test website used in this example:

https://bootswatch.com/default

These locators are useful for interacting with **form inputs**, because they rely on **user-visible labels and placeholders**, which makes tests more reliable and readable.

---

# Using `get_by_label()`

`get_by_label()` locates form elements using their **associated label text**.

Example labels on the Bootswatch page include:

- Email address
- Password
- Example textarea

---

## Highlight the Email Field

```python
page.get_by_label("Email address").highlight()
```

# Locate the input field associated with the label **"Email address"**.
# The highlight() method visually highlights the element in the browser.
# This is useful for debugging and confirming that the correct element is selected.

---

## Highlight the Password Field

```python
page.get_by_label("Password").highlight()
```

# Locate the input field associated with the label **"Password"**.
# Playwright automatically connects the label with its corresponding input field.

---

## Highlight the Textarea Field

```python
page.get_by_label("Example textarea").highlight()
```

# Locate a textarea input using its label **"Example textarea"**.
# Textareas are commonly used for multi-line input fields.

---

# Using `get_by_placeholder()`

`get_by_placeholder()` locates input fields based on the **placeholder text inside the input box**.

Placeholder text usually appears inside input fields as a hint for the user.

Examples:

- Default input
- Email address
- name@example.com

---

## Highlight Input Field with Placeholder "Default input"

```python
page.get_by_placeholder("Default input").highlight()
```

# Locate the input field where the placeholder text is **"Default input"**.
# The element will be highlighted in the browser.

---

## Highlight Input Field with Placeholder "Email address"

```python
page.get_by_placeholder("Email address").highlight()
```

# Locate the input element with placeholder **"Email address"**.

---

## Highlight Input Field with Placeholder "name@example.com"

```python
page.get_by_placeholder("name@example.com").highlight()
```

# Locate the input field containing the placeholder **"name@example.com"**.

---

# Why These Locators Are Recommended

Playwright recommends **user-facing locators** because they are more stable than CSS or XPath selectors.

Preferred locator priority in Playwright:

1. `get_by_role()`
2. `get_by_label()`
3. `get_by_placeholder()`
4. `get_by_text()`
5. `get_by_test_id()`
6. CSS or XPath selectors

---

# Example Automation Script

Example Playwright script using these locators:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # Highlight email field
    page.get_by_label("Email address").highlight()

    # Highlight password field
    page.get_by_label("Password").highlight()

    # Highlight textarea field
    page.get_by_label("Example textarea").highlight()

    # Highlight placeholder inputs
    page.get_by_placeholder("Default input").highlight()
    page.get_by_placeholder("Email address").highlight()
    page.get_by_placeholder("name@example.com").highlight()

    browser.close()
```

---

# Key Takeaways

✔ `get_by_label()` works with **form labels**

✔ `get_by_placeholder()` works with **placeholder text inside inputs**

✔ These locators make tests:

- More readable
- More stable
- Closer to real user interaction

---

# Useful Debugging Tip

You can visually inspect locators using:

```python
locator.highlight()
```

This helps verify that Playwright is selecting the **correct element on the page**.

---

# Next Playwright Locator Topics

Common locators used in automation testing:

- `get_by_role()`
- `get_by_label()`
- `get_by_placeholder()`
- `get_by_text()`
- `get_by_test_id()`
- `locator()`
- CSS selectors
- XPath selectors

✅ This example demonstrates:
# Playwright Locator: `get_by_text()`

This section demonstrates how to use Playwright's **`get_by_text()` locator** to identify elements based on the visible text on a webpage.

Test website used in this example:

https://bootswatch.com/default

The `get_by_text()` locator searches for elements that contain specific **visible text**.

This is useful when interacting with:

- Buttons
- Links
- Labels
- Paragraph text
- Headings

---

# Highlight Element Using Text

```python
page.get_by_text("faded secondary").highlight()
```

# Locate an element containing the visible text **"faded secondary"**.
# The `highlight()` method visually marks the element in the browser.
# This is useful for debugging and verifying the correct element.

---

# Exact Text Matching

Playwright allows you to specify whether the text match should be **exact**.

---

## Exact Match Enabled

```python
page.get_by_text("faded secondary", exact=True).highlight()
```

# Locate an element whose text exactly matches **"faded secondary"**.
# `exact=True` ensures that Playwright only selects elements with the exact text.

---

## Exact Match Disabled

```python
page.get_by_text("faded secondary", exact=False).highlight()
```

# Locate elements that **contain** the text "faded secondary".
# This allows partial matching.

---

# Highlight a Button by Text

```python
page.get_by_text("Small button", exact=True).highlight()
```

# Locate the element with visible text **"Small button"**.
# Highlight the button in the browser.

---

# Click the Button

```python
page.get_by_text("Small button", exact=True).click()
```

# Locate the element containing text **"Small button"** and click it.

---

# Click Another Button

```python
page.get_by_text("Large button", exact=True).click()
```

# Locate the element with visible text **"Large button"** and perform a click action.

---

# Why `get_by_text()` Is Useful

`get_by_text()` is useful when:

- Elements do not have labels
- Elements do not have unique attributes
- You want to interact with **user-visible content**

---

# Example Automation Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # Highlight elements using text locators
    page.get_by_text("faded secondary").highlight()
    page.get_by_text("faded secondary", exact=True).highlight()

    # Highlight button
    page.get_by_text("Small button", exact=True).highlight()

    # Click buttons
    page.get_by_text("Small button", exact=True).click()
    page.get_by_text("Large button", exact=True).click()

    browser.close()
```

---

# Key Takeaways

✔ `get_by_text()` locates elements using **visible text on the page**

✔ `exact=True` ensures **exact text matching**

✔ `exact=False` allows **partial matching**

✔ Useful for locating:

- Buttons
- Links
- Labels
- Messages

---

# Debugging Tip

You can verify locators visually using:

```python
locator.highlight()
```

This helps ensure that **Playwright is targeting the correct element**.

---

# Recommended Playwright Locator Priority

Playwright recommends using locators in this order:

1. `get_by_role()`
2. `get_by_label()`
3. `get_by_placeholder()`
4. `get_by_text()`
5. `get_by_test_id()`
6. CSS or XPath selectors
- Using **Playwright role-based locators**
- Debugging locators
- Clicking buttons, headings, and checkboxes
# How to Clear the Terminal in Visual Studio Code

You can clear the **Terminal in Visual Studio Code** in several simple ways. 🧹💻

---

# 1. Keyboard Shortcut (Fastest)

Press:

```bash
Cmd + K
```

This clears the **terminal output instantly on macOS**.

---

# 2. Using the `clear` Command

In the terminal, type:

```bash
clear
```

Then press **Enter**.

This works in:

- `zsh`
- `bash`
- Python virtual environments

Example terminal prompt:

```bash
(venv) abubakar@Abus-Air playwright-python-project %
```

---

# 3. Using `Ctrl + L`

Press:

```bash
Ctrl + L
```

This also **clears the terminal screen** without closing the session.

---

# 4. Using the Trash Icon

In the **VS Code terminal panel**:

1. Look at the **top right of the terminal window**
2. Click the **trash bin icon 🗑**

This will:

- Kill the current terminal
- Start a **new clean terminal session**

---

# 5. Restart Terminal

Click the **"+" icon** in the terminal panel to open a new terminal.

This creates a **fresh terminal instance**.

---

# Recommended Method for Developers

Use:

```bash
Ctrl + L
```

This is the **fastest and most commonly used method** in coding environments.

---

# Example Workflow for Playwright + Python

Clearing the terminal before running tests keeps output clean.

Example:

```bash
clear
python test.py
```

or

```bash
Ctrl + L
python test.py
```

This helps you easily read the **latest test execution results**.
# Playwright Locator: `get_by_alt_text()`

This example demonstrates how to use Playwright's **`get_by_alt_text()` locator** to interact with images on a webpage.

Test website used in this example:

https://unsplash.com

The `get_by_alt_text()` locator identifies **images based on their `alt` attribute**.  
The `alt` attribute provides **alternative text descriptions for images**, which improves accessibility and helps screen readers.

---

# Start Playwright

```python
from playwright.sync_api import sync_playwright
```

# Import the synchronous Playwright API to control browsers with Python.

```python
playwright = sync_playwright().start()
```

# Start the Playwright engine.  
# This initializes the Playwright driver so we can launch browsers.

```python
browser = playwright.chromium.launch(headless=False)
```

# Launch the Chromium browser.
# `headless=False` means the browser UI will be visible.

---

# Create a New Page

```python
page = browser.new_page()
```

# Create a new browser tab (page) where automation will run.

---

# Navigate to the Website

```python
page.goto("https://www.unsplash.com")
```

# Navigate to the Unsplash website.

Example response returned by Playwright:

```
<Response url='https://unsplash.com/' request=<Request url='https://unsplash.com/' method='GET'>>
```

---

# Locate Image Using Alt Text

```python
page.get_by_alt_text("Elderly couple with harvested garlic bulbs").highlight()
```

# Locate an image whose **alt attribute** is  
# `"Elderly couple with harvested garlic bulbs"`.

# The `highlight()` method visually highlights the image in the browser.  
# This is useful for debugging and verifying the correct element.

---

# Click an Image Using Alt Text

```python
page.get_by_alt_text("Rocky formations under a colorful, hazy sky.").click()
```

# Locate the image with alt text  
# `"Rocky formations under a colorful, hazy sky."`.

# Perform a **click action** on that image.

---

# Example Full Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://unsplash.com")

    # Highlight image using alt text
    page.get_by_alt_text("Elderly couple with harvested garlic bulbs").highlight()

    # Click another image using alt text
    page.get_by_alt_text("Rocky formations under a colorful, hazy sky.").click()

    browser.close()
```

---

# Why `get_by_alt_text()` Is Useful

This locator is recommended when working with **images**, because it relies on **accessible alt text**.

Benefits:

✔ Works well with **image elements**

✔ Improves **test readability**

✔ Supports **accessible testing practices**

---

# Common Playwright Image Locator Methods

| Locator | Purpose |
|------|------|
| `get_by_alt_text()` | Locate images using alt attribute |
| `get_by_role("img")` | Locate image elements by role |
| `locator("img")` | Locate images using CSS selector |

---

# Debugging Tip

Use:

```python
locator.highlight()
```

to visually confirm the element selected by Playwright.

---

# Recommended Locator Priority in Playwright

Playwright recommends using locators in this order:

1. `get_by_role()`
2. `get_by_label()`
3. `get_by_placeholder()`
4. `get_by_text()`
5. `get_by_alt_text()`
6. `get_by_test_id()`
7. CSS or XPath selectors

---

✅ `get_by_alt_text()` is especially useful when automating **image-heavy websites like Unsplash or e-commerce platforms**.

---
# Playwright Locator: `get_by_title()`

This example demonstrates how to use Playwright's **`get_by_title()` locator** to identify elements using the HTML **`title` attribute**.

Test website used in this example:

https://bootswatch.com/default

The `title` attribute is commonly used to provide **additional information about an element**.  
When users hover over such elements, a tooltip usually appears.

Playwright can locate these elements using `get_by_title()`.

---

# Define the Target URL

```python
url = "https://bootswatch.com/default"
```

# Store the Bootswatch webpage URL in a variable.  
# This keeps the code cleaner and easier to maintain.

---

# Launch the Browser

```python
browser = playwright.chromium.launch(headless=False)
```

# Launch the Chromium browser.  
# `headless=False` means the browser will open with a visible UI.

---

# Create a New Page

```python
page = browser.new_page()
```

# Create a new browser tab where automation will run.

---

# Navigate to the Website

```python
page.goto(url)
```

# Navigate to the Bootswatch webpage.

Example response returned by Playwright:

```
<Response url='https://bootswatch.com/default/' request=<Request url='https://bootswatch.com/default/' method='GET'>>
```

---

# Locate Element Using Title Attribute

```python
page.get_by_title("Source Title").highlight()
```

# Locate an element whose HTML `title` attribute is **"Source Title"**.

# The `highlight()` method visually highlights the element in the browser.  
# This helps confirm that Playwright has correctly located the element.

---

# Example Full Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    url = "https://bootswatch.com/default"

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(url)

    # Highlight element using title attribute
    page.get_by_title("Source Title").highlight()

    browser.close()
```

---

# Why Use `get_by_title()`?

`get_by_title()` is useful when:

- Elements contain a **title attribute**
- Tooltips are used
- Other locators (role, label, text) are unavailable

---

# Example HTML Element

An example element that Playwright may locate:

```html
<a href="..." title="Source Title">View Source</a>
```

Playwright can locate this element using:

```python
page.get_by_title("Source Title")
```

---

# Debugging Tip

Use:

```python
locator.highlight()
```

This visually highlights the element to ensure the correct locator is used.

---

# Recommended Locator Priority in Playwright

Playwright recommends using locators in this order:

1. `get_by_role()`
2. `get_by_label()`
3. `get_by_placeholder()`
4. `get_by_text()`
5. `get_by_alt_text()`
6. `get_by_title()`
7. `get_by_test_id()`
8. CSS or XPath selectors

---

# Key Takeaways

✔ `get_by_title()` locates elements using the **HTML title attribute**

✔ Useful for elements with **tooltips**

✔ Helps create **readable and maintainable automation tests**

✅ Keeping the terminal clean is useful when running **automation tests with Playwright, Selenium, or Appium**.
# Playwright Locators Using CSS Selectors

This section demonstrates how to use **CSS selectors with Playwright's `locator()` method**.

Test website used in this example:

https://bootswatch.com/default

CSS selectors are useful when:

- ARIA locators are not available
- Elements have unique classes or attributes
- You need more precise element targeting

---

# Highlight All Buttons

```python
page.locator("button").highlight()
```

# Locate all `<button>` elements on the page.
# `highlight()` visually highlights the matching elements in the browser.
# Useful for debugging and verifying selectors.

---

# Locate Button Using Class Selector

```python
page.locator("button.btn-success").highlight()
```

# Locate all buttons with the class **btn-success**.
# This uses a CSS **class selector**.

Example HTML:

```html
<button class="btn btn-success">Success</button>
```

---

# Locate Primary Buttons

```python
page.locator("button.btn-primary").highlight()
```

# Locate buttons with the **btn-primary** class.

---

# Locate Large Buttons

```python
page.locator("button.btn-lg").highlight()
```

# Locate buttons with the **btn-lg** class.

---

# Locate Heading Elements

```python
page.locator("h1").highlight()
```

# Locate all `<h1>` heading elements on the page.

---

# Locate Input Using Class

```python
page.locator("input.form-control").highlight()
```

# Locate input fields with the class **form-control**.

Example HTML:

```html
<input class="form-control" type="email">
```

---

# Locate Input Using ID

```python
page.locator("input#exampleInputEmail1").highlight()
```

# Locate the input element with the ID **exampleInputEmail1**.
# `#` represents an **ID selector** in CSS.

Example HTML:

```html
<input id="exampleInputEmail1" type="email">
```

---

# Locate Element Using Class Selector

```python
page.locator("small.text-muted").highlight()
```

# Locate `<small>` elements with the class **text-muted**.

---

# Locate Element Using Attribute Selector

```python
page.locator("input[readonly]").highlight()
```

# Locate input elements that contain the **readonly attribute**.

Example HTML:

```html
<input type="text" value="email@example.com" readonly>
```

---

# Locate Element Using Attribute Value

```python
page.locator("input[value='email@example.com']").highlight()
```

# Locate an input element whose **value attribute equals "email@example.com"**.

---

# Example Full Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # CSS selectors examples
    page.locator("button").highlight()
    page.locator("button.btn-success").highlight()
    page.locator("button.btn-primary").highlight()
    page.locator("button.btn-lg").highlight()

    page.locator("h1").highlight()

    page.locator("input.form-control").highlight()
    page.locator("input#exampleInputEmail1").highlight()

    page.locator("small.text-muted").highlight()

    page.locator("input[readonly]").highlight()
    page.locator("input[value='email@example.com']").highlight()

    browser.close()
```

---

# Common CSS Selectors Used in Playwright

| Selector | Meaning | Example |
|------|------|------|
| `element` | Select by tag | `button` |
| `.class` | Select by class | `.btn-primary` |
| `#id` | Select by ID | `#exampleInputEmail1` |
| `element.class` | Tag + class | `button.btn-success` |
| `[attribute]` | Attribute exists | `input[readonly]` |
| `[attribute=value]` | Attribute equals value | `input[value='text']` |

---

# Important Note

Playwright recommends using **user-facing locators first**, such as:

1. `get_by_role()`
2. `get_by_label()`
3. `get_by_placeholder()`
4. `get_by_text()`

CSS selectors should be used when **semantic locators are not available**.

---

# Debugging Tip

You can visually inspect elements using:

```python
locator.highlight()
```

This helps verify that **the locator is selecting the correct element**.

---

# Key Takeaways

✔ `locator()` allows using **CSS selectors in Playwright**

✔ CSS selectors are powerful for targeting elements by:

- Tag
- Class
- ID
- Attributes

✔ Useful when semantic locators are unavailable
# Playwright CSS Hierarchy Selectors

This section demonstrates how to use **CSS hierarchy selectors** in Playwright using the `locator()` method.

Test website used in this example:

https://bootswatch.com/default

CSS hierarchy selectors allow you to locate elements based on their **position within the HTML structure (parent → child relationships)**.

This helps create **more precise selectors**.

---

# Locate Input Using Attribute Selector

```python
page.locator("input[value='email@example.com']").highlight()
```

# Locate an `<input>` element whose **value attribute equals "email@example.com"**.
# This uses a **CSS attribute selector**.

---

# Locate Navigation Bar Using Class

```python
page.locator("nav.bg-dark").highlight()
```

# Locate the `<nav>` element with class **bg-dark**.
# This represents the main navigation bar on the Bootswatch page.

Example HTML:

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
```

---

# Locate Footer Element

```python
page.locator("footer").highlight()
```

# Locate the `<footer>` element at the bottom of the page.

---

# Locate Nested Elements Using Hierarchy

```python
page.locator("nav.bg-dark div.container-fluid").highlight()
```

# Locate a `<div>` element with class **container-fluid**
# that exists inside the **nav.bg-dark** element.

Structure example:

```
nav.bg-dark
   └── div.container-fluid
```

---

# Locate Navbar Collapse Section

```python
page.locator("nav.bg-dark div.container-fluid div.navbar-collapse").highlight()
```

# Locate the **navbar-collapse div** inside the container-fluid div
# which itself is inside the navigation bar.

Structure:

```
nav.bg-dark
   └── div.container-fluid
         └── div.navbar-collapse
```

---

# Locate Active Navigation Link

```python
page.locator("nav.bg-dark div.container-fluid div.navbar-collapse a.active").highlight()
```

# Locate an `<a>` element with class **active**
# inside the navbar-collapse section.

---

# Click the Active Navigation Link

```python
page.locator("nav.bg-dark div.container-fluid div.navbar-collapse a.active").click()
```

# Locate the active navigation link and perform a **click action**.

---

# Locate Direct Child Elements Using `>`

```python
page.locator("div.bs-compenet > ul.list-group").highlight()
```

# The `>` symbol selects **direct child elements only**.

Structure example:

```
div.bs-compenet
   └── ul.list-group
```

This selector finds:

- `ul.list-group`
- that is a **direct child of div.bs-compenet**

---

# Alternative Syntax Without Spaces

```python
page.locator("div.bs-compenet>ul.list-group").highlight()
```

# This is the same as the previous selector.
# CSS allows removing spaces around the `>` operator.

---

# Example Full Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    page.locator("input[value='email@example.com']").highlight()

    page.locator("nav.bg-dark").highlight()
    page.locator("footer").highlight()

    page.locator("nav.bg-dark div.container-fluid").highlight()
    page.locator("nav.bg-dark div.container-fluid div.navbar-collapse").highlight()

    page.locator("nav.bg-dark div.container-fluid div.navbar-collapse a.active").highlight()
    page.locator("nav.bg-dark div.container-fluid div.navbar-collapse a.active").click()

    page.locator("div.bs-compenet > ul.list-group").highlight()
    page.locator("div.bs-compenet>ul.list-group").highlight()

    browser.close()
```

---

# Common CSS Hierarchy Selectors

| Selector | Meaning | Example |
|------|------|------|
| `A B` | Descendant selector | `nav div` |
| `A > B` | Direct child selector | `div > ul` |
| `A.class` | Element with class | `nav.bg-dark` |
| `#id` | Element with ID | `#navbar` |

---

# Why CSS Hierarchy Is Useful

Hierarchy selectors help when:

- Multiple elements share the same class
- You want to target **specific nested elements**
- The page structure must be used to locate elements

---

# Debugging Tip

Use:

```python
locator.highlight()
```

This visually highlights elements so you can **verify your CSS selector is correct**.

---

# Key Takeaways

✔ CSS hierarchy selectors help locate **nested elements**
# Playwright CSS Pseudo-Classes

This section demonstrates how to use **CSS pseudo-classes in Playwright** with the `locator()` method.

Test website used in this example:

https://bootswatch.com/default

Pseudo-classes allow you to **filter elements based on state, text, visibility, or position**.

They make CSS selectors more **powerful and precise** when locating elements.

---

# Locate Element Using Text Filter

```python
page.locator("span.bg-secondary:text('Secondary')").highlight()
```

# Locate a `<span>` element with class **bg-secondary** that contains the text **"Secondary"**.
# The `:text()` pseudo-class matches elements that contain the specified text.

---

# Exact Text Matching

```python
page.locator("span.bg-secondary:text-is('Secondary')").highlight()
```

# Locate a `<span>` element with class **bg-secondary** whose text is exactly **"Secondary"**.
# `:text-is()` ensures an **exact match** rather than partial text matching.

---

# Locate Dropdown Menu

```python
page.locator("div.dropdown-menu").highlight()
```

# Locate `<div>` elements with class **dropdown-menu**.

Example HTML:

```html
<div class="dropdown-menu">
```

---

# Locate Only Visible Dropdown Menus

```python
page.locator("div.dropdown-menu:visible").highlight()
```

# Locate dropdown menus that are **currently visible on the page**.
# `:visible` is useful when elements exist in the DOM but are hidden.

---

# Locate Elements Using `:nth-match()`

Playwright provides the **`:nth-match()` pseudo-class** to select elements by index.

---

## Select Second Matching Button

```python
page.locator(":nth-match(button.btn-secondary, 2)").highlight()
```

# Locate the **second button** with class **btn-secondary**.

Structure example:

```html
<button class="btn btn-secondary">Secondary</button>
```

---

## Select Third Matching Button

```python
page.locator(":nth-match(button.btn-secondary, 3)").highlight()
```

# Locate the **third button** that matches the selector.

---

## Select Fifth Matching Button

```python
page.locator(":nth-match(button.btn-secondary, 5)").highlight()
```

# Locate the **fifth button** with class **btn-secondary**.

---

## Select Sixth Matching Button

```python
page.locator(":nth-match(button.btn-secondary, 6)").highlight()
```

# Locate the **sixth button** matching the selector.

---

# Example Full Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    page.locator("span.bg-secondary:text('Secondary')").highlight()
    page.locator("span.bg-secondary:text-is('Secondary')").highlight()

    page.locator("div.dropdown-menu").highlight()
    page.locator("div.dropdown-menu:visible").highlight()

    page.locator(":nth-match(button.btn-secondary, 2)").highlight()
    page.locator(":nth-match(button.btn-secondary, 3)").highlight()
    page.locator(":nth-match(button.btn-secondary, 5)").highlight()
    page.locator(":nth-match(button.btn-secondary, 6)").highlight()

    browser.close()
```

---

# Common Playwright CSS Pseudo-Classes

| Pseudo-Class | Purpose | Example |
|------|------|------|
| `:text()` | Match elements containing text | `button:text("Submit")` |
| `:text-is()` | Exact text match | `button:text-is("Submit")` |
| `:visible` | Select visible elements | `div:visible` |
| `:nth-match()` | Select element by index | `:nth-match(button,2)` |

---

# Why CSS Pseudo-Classes Are Useful

Pseudo-classes help when:

- Multiple elements match the same selector
- You need to filter by **text content**
- Elements may be **hidden or visible**
- You want to target a **specific instance of an element**

---

# Debugging Tip

Use:

```python
locator.highlight()
```

This visually highlights the element so you can **verify the selector is correct**.

---

# Key Takeaways

✔ Playwright extends CSS with powerful **pseudo-classes**

✔ `:text()` and `:text-is()` allow **text filtering**

✔ `:visible` ensures the element is **displayed**

✔ `:nth-match()` helps target **specific elements by index**

✔ `A B` selects **any descendant**

✔ `A > B` selects **direct children only**

✔ Useful when creating **precise Playwright locators**
# Playwright Locators Using XPath

This section demonstrates how to use **XPath selectors** with Playwright using the `locator()` method.

Test website used in this example:

https://bootswatch.com/default

XPath is a powerful way to locate elements based on:

- Element attributes
- Element hierarchy
- Element relationships

Although Playwright recommends **role-based locators first**, XPath is still useful in many real-world automation scenarios.

---

# Locate Heading Element

```python
page.locator("//h1").highlight()
```

# Locate all `<h1>` elements on the page using XPath.
# The `//` symbol means **search anywhere in the document**.

Example HTML:

```html
<h1>Buttons</h1>
```

---

# Locate Element Using Attribute

```python
page.locator("//h1[@id='Buttons']").highlight()
```

# Locate an `<h1>` element with the attribute **id="Buttons"**.

Explanation:

- `//h1` → Select all `<h1>` elements
- `[@id='Buttons']` → Filter elements with the specified attribute value

Example HTML:

```html
<h1 id="Buttons">Buttons</h1>
```

---

# Locate Input Element with Attribute

```python
page.locator("//input[@readonly]").highlight()
```

# Locate `<input>` elements that contain the **readonly attribute**.

Example HTML:

```html
<input type="text" value="email@example.com" readonly>
```

---

# Locate Input Using Attribute Value

```python
page.locator("//input[@value='wrong value']").highlight()
```

# Locate an input element whose **value attribute equals "wrong value"**.

Structure example:

```html
<input type="text" value="wrong value">
```

---

# Example Full Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    page.locator("//h1").highlight()

    page.locator("//h1[@id='Buttons']").highlight()

    page.locator("//input[@readonly]").highlight()

    page.locator("//input[@value='wrong value']").highlight()

    browser.close()
```

---

# Common XPath Syntax

| XPath | Meaning | Example |
|------|------|------|
| `//element` | Select element anywhere in DOM | `//h1` |
| `//element[@attr='value']` | Select element with attribute | `//input[@type='text']` |
| `//element[@attr]` | Attribute exists | `//input[@readonly]` |
| `//parent/child` | Direct child | `//div/input` |

---

# Why XPath Is Useful

XPath helps when:

- Elements do not have unique CSS classes
- You need to locate elements by **complex hierarchy**
- You want **flexible element navigation**

---

# Debugging Tip

Use:

```python
locator.highlight()
```

This visually highlights the element in the browser to confirm the selector is correct.

---

# Recommended Locator Strategy in Playwright

Playwright suggests using locators in this order:

1. `get_by_role()`
2. `get_by_label()`
3. `get_by_placeholder()`
4. `get_by_text()`
5. `get_by_alt_text()`
6. `get_by_title()`
7. CSS selectors
8. XPath selectors

---

# Key Takeaways

✔ XPath locates elements using **XML-style path expressions**

✔ Useful for selecting elements based on **attributes or hierarchy**

✔ Works well when **CSS selectors are not sufficient**
# Playwright XPath Functions: `text()` and `contains()`

This section demonstrates how to use **XPath functions** such as `text()` and `contains()` in Playwright.

Test website used in this example:

https://bootswatch.com/default

XPath functions allow you to locate elements when:

- The full text is not known
- The attribute value changes dynamically
- You want partial matching

These functions make XPath **more flexible and powerful**.

---

# Locate Element Using Partial Text

```python
page.locator("//h1[contains(text(),'Head')]").highlight()
```

# Locate an `<h1>` element whose text contains **"Head"**.

Explanation:

- `//h1` → Select all `<h1>` elements
- `contains(text(),'Head')` → Match elements whose text contains the word **Head**

Example HTML:

```html
<h1>Headings</h1>
```

This XPath works because **"Headings" contains "Head"**.

---

# Locate Element Using Class Attribute

```python
page.locator("//button[contains(@class,'btn-lg')]").highlight()
```

# Locate `<button>` elements where the **class attribute contains "btn-lg"**.

Explanation:

- `@class` refers to the **class attribute**
- `contains()` allows partial matching of the attribute value

Example HTML:

```html
<button class="btn btn-primary btn-lg">Large Button</button>
```

This XPath will match the element because the class includes **btn-lg**.

---

# Locate Input Element Using Partial Attribute Value

```python
page.locator("//input[contains(@value,'correct')]").highlight()
```

# Locate `<input>` elements where the **value attribute contains the text "correct"**.

Example HTML:

```html
<input type="text" value="correct value">
```

Since the value contains **"correct"**, the XPath selector will match the element.

---

# Example Full Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    page.locator("//h1[contains(text(),'Head')]").highlight()

    page.locator("//button[contains(@class,'btn-lg')]").highlight()

    page.locator("//input[contains(@value,'correct')]").highlight()

    browser.close()
```

---

# Common XPath Functions

| Function | Purpose | Example |
|------|------|------|
| `text()` | Match element text | `//h1[text()='Heading']` |
| `contains()` | Partial text or attribute match | `//button[contains(@class,'btn')]` |
| `starts-with()` | Match starting text | `//input[starts-with(@id,'user')]` |

---

# Why XPath Functions Are Useful

XPath functions help when:

- Text is **partially known**
- Attribute values **change dynamically**
- Elements share similar attributes

They make locators **more flexible and reliable**.

---

# Debugging Tip

Use:

```python
locator.highlight()
```

This visually highlights the element so you can **confirm the XPath selector is correct**.

---

# Key Takeaways

✔ `text()` locates elements using **exact text**

✔ `contains()` allows **partial text or attribute matching**

✔ These functions make XPath **more flexible for automation**
# Playwright Miscellaneous Selectors

This section demonstrates **additional Playwright locator techniques** that help when standard locators are not sufficient.

Test website used in this example:

https://bootswatch.com/default

These selectors include:

- `nth` index selection
- Parent selection (`..`)
- `id=` selector
- `filter()` with `has_text`
- `filter()` with `has`
- Visibility filtering

These techniques help create **more precise and flexible Playwright locators**.

---

# Select Element by Index Using `nth`

Sometimes multiple elements match the same locator.  
Playwright allows selecting a specific element using **`nth`**.

### Highlight Second Primary Button

```python
page.get_by_role("button", name="Primary").locator("nth=1").highlight()
```

# Locate all buttons with accessible name **Primary**  
# Select the **second matching element** (`nth=1`, because indexing starts at 0)

---

### Highlight Second Button on Page

```python
page.locator("button").locator("nth=1").highlight()
```

# Locate all `<button>` elements  
# Select the **second button** on the page

---

### Highlight 25th Button

```python
page.locator("button").locator("nth=24").highlight()
```

# Locate the **25th button** element (index starts from 0)

---

### Highlight 149th Button

```python
page.locator("button").locator("nth=148").highlight()
```

# Locate the **149th button** on the page

---

# Select Parent Element

You can select the **parent element** using `..`.

### Highlight Parent of Email Field

```python
page.get_by_label("Email address").locator("..").highlight()
```

# Locate the input field with label **Email address**  
# `..` moves **one level up in the DOM hierarchy** to the parent element

Example structure:

```
div.form-group
   └── input (Email address)
```

---

# Locate Element Using ID Selector

```python
page.locator("id=btnGroupDrop1").highlight()
```

# Locate element with **ID = btnGroupDrop1**

Example HTML:

```html
<button id="btnGroupDrop1">Dropdown</button>
```

---

# Locate Dropdown Elements

```python
page.locator("div.dropdown").highlight()
```

# Locate `<div>` elements with class **dropdown**

---

```python
page.locator("div.dropdown-menu").highlight()
```

# Locate `<div>` elements with class **dropdown-menu**

---

# Locate Visible Elements

```python
page.locator("div.dropdown-menu").locator("visible=true").highlight()
```

# Locate **only visible dropdown menu elements**

This is useful when elements exist in the DOM but are hidden.

---

# Filter Elements by Text

Playwright provides the **`filter()` method** to refine locators.

```python
page.get_by_role("heading").filter(has_text="Heading").highlight()
```

# Locate all heading elements  
# Filter them to only those containing the text **"Heading"**

---

### Select Specific Filtered Heading

```python
page.get_by_role("heading").filter(has_text="Heading").locator("nth=1").highlight()
```

# Locate headings containing text **Heading**  
# Select the **second matching heading**

---

# Filter Elements by Contained Element

Playwright allows filtering based on **child elements** using `has=`.

```python
page.locator("div.form-group").filter(has=page.get_by_label("Password")).highlight()
```

# Locate `<div class="form-group">` elements  
# Filter to only those that contain an element labeled **Password**

Example HTML:

```html
<div class="form-group">
   <label>Password</label>
   <input type="password">
</div>
```

---

# Example Full Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    page.get_by_role("button", name="Primary").locator("nth=1").highlight()

    page.locator("button").locator("nth=1").highlight()

    page.get_by_label("Email address").locator("..").highlight()

    page.locator("id=btnGroupDrop1").highlight()

    page.locator("div.dropdown").highlight()
    page.locator("div.dropdown-menu").highlight()

    page.locator("div.dropdown-menu").locator("visible=true").highlight()

    page.get_by_role("heading").filter(has_text="Heading").highlight()

    page.get_by_role("heading").filter(has_text="Heading").locator("nth=1").highlight()

    page.locator("div.form-group").filter(has=page.get_by_label("Password")).highlight()

    browser.close()
```

---

# Key Miscellaneous Locator Techniques

| Feature | Purpose | Example |
|------|------|------|
| `nth=` | Select element by index | `locator("nth=1")` |
| `..` | Move to parent element | `locator("..")` |
| `id=` | Locate by ID | `locator("id=myId")` |
| `filter(has_text=)` | Filter by text | `.filter(has_text="Login")` |
| `filter(has=)` | Filter by child element | `.filter(has=page.get_by_label("Password"))` |
| `visible=true` | Select visible elements only | `locator("visible=true")` |

---

# Why These Selectors Are Useful

Miscellaneous selectors help when:

- Many elements match the same locator
- You need **index-based selection**
- You want to navigate the **DOM hierarchy**
- Elements must be filtered by **text or child elements**

These techniques allow building **more advanced and precise Playwright locators**.

---

# Debugging Tip

Use:

```python
locator.highlight()
```

to visually confirm that Playwright has selected the **correct element**.

---

# Key Takeaways

✔ `nth=` selects elements by **index**

✔ `..` allows **parent navigation**

✔ `filter()` helps refine locators

✔ `visible=true` ensures elements are **displayed**

✔ These techniques improve **locator precision in complex pages**

# Playwright Mouse Actions

This section demonstrates how to perform **mouse interactions in Playwright**.

Mouse actions are commonly used in automation testing to simulate **real user interactions**, such as:

- Clicking buttons
- Double-clicking elements
- Right-clicking (context menu)
- Hovering over elements
- Using keyboard modifiers during clicks

Test website used in this example:

https://bootswatch.com/default

---

# Locate a Button Element

```python
page.get_by_role("button", name="Block button").highlight()
```

# Locate a button with accessible name **"Block button"**  
# `highlight()` visually highlights the element in the browser.

---

# Select the Last Matching Button

```python
button = page.get_by_role("button", name="Block button").last
```

# Locate all buttons with name **Block button**  
# `.last` selects the **last matching element**.

---

# Highlight the Selected Button

```python
button.highlight()
```

# Highlight the selected button to verify the locator.

---

# Perform a Click Action

```python
button.click()
```

# Perform a **single mouse click** on the button.

---

# Highlight Footer Element

```python
page.locator("footer").highlight()
```

# Highlight the footer element on the page.

---

# Double Click the Button

```python
button.dblclick()
```

# Perform a **double-click action** on the button.

---

# Double Click with Delay

```python
button.dblclick(delay=500)
```

# Perform a double-click with **500 ms delay between clicks**.

---

# Right Click (Context Menu)

```python
button.click(button="right")
```

# Perform a **right mouse click** on the button.  
# This usually opens the **context menu**.

---

# Click with Keyboard Modifier

```python
button.click(modifiers=["Shift"])
```

# Perform a click while holding the **Shift key**.

---

# Click with Multiple Modifiers

```python
button.click(modifiers=["Shift", "Alt"])
```

# Perform a click while holding **Shift + Alt keys**.

This simulates advanced keyboard + mouse interaction.

---

# Hover Over an Element

```python
page.locator("button.btn-outline-primary").hover()
```

# Move the mouse cursor over a button with class **btn-outline-primary**.

Hover actions are useful for:

- Triggering dropdown menus
- Revealing hidden elements
- Testing hover animations

---

# Example Full Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # Locate button
    button = page.get_by_role("button", name="Block button").last

    button.highlight()

    # Mouse actions
    button.click()

    button.dblclick()

    button.dblclick(delay=500)

    button.click(button="right")

    button.click(modifiers=["Shift"])

    button.click(modifiers=["Shift", "Alt"])

    # Hover example
    page.locator("button.btn-outline-primary").hover()

    browser.close()
```

---

# Common Playwright Mouse Actions

| Action | Method |
|------|------|
| Single click | `click()` |
| Double click | `dblclick()` |
| Right click | `click(button="right")` |
| Hover | `hover()` |
| Click with modifier | `click(modifiers=["Shift"])` |

---

# Why Mouse Actions Are Important

Mouse actions help automate **real user interactions**, including:

- Clicking UI elements
- Testing context menus
- Triggering hover effects
- Simulating keyboard + mouse combinations

---

# Debugging Tip

Use:

```python
locator.highlight()
```

This visually highlights elements to confirm the **correct locator**.

---

# Key Takeaways

✔ Playwright supports advanced **mouse interactions**

✔ `click()` performs standard clicks

✔ `dblclick()` performs double clicks

✔ `click(button="right")` performs right-click

✔ `hover()` simulates mouse hover

✔ Modifiers simulate **keyboard + mouse combinations**
# Playwright Write Text Functions

This section demonstrates how to **write text into input fields using Playwright**.

These functions simulate real user typing behavior and are commonly used for:

- Login forms
- Search boxes
- Registration forms
- Input validation testing

Test website used in this example:

https://bootswatch.com/default

---

# Start Playwright

```python
from playwright.sync_api import sync_playwright
```

# Import the synchronous Playwright API to control browsers.

---

```python
playwright = sync_playwright().start()
```

# Start the Playwright engine.

---

```python
browser = playwright.chromium.launch(headless=False)
```

# Launch the Chromium browser with visible UI.

---

```python
page = browser.new_page()
```

# Create a new browser tab.

---

```python
page.goto("https://bootswatch.com/default")
```

# Navigate to the Bootswatch demo page.

---

# Locate Email Input Field

```python
page.get_by_label("Email address").highlight()
```

# Highlight the input field labeled **Email address**.

---

# Select the First Matching Email Field

Sometimes multiple elements match the same locator.  
We can select the **first element** using `.first`.

```python
input_field = page.get_by_label("Email address").first
```

# Locate the first email input field.

---

# Fill Text in the Input Field

```python
input_field.fill("ABC")
```

# `fill()` clears the existing value and inserts the new text **ABC**.

---

# Clear the Input Field

```python
input_field.clear()
```

# Remove all text from the input field.

---

# Type Text Like a Real User

```python
input_field.type("ABC")
```

# `type()` simulates real keyboard typing.

---

# Type Text with Delay

```python
input_field.type("ABC", delay=500)
```

# Type text with **500 ms delay between keystrokes**.

This simulates **real user typing behavior**.

---

# Clear Field Again

```python
input_field.clear()
```

# Remove previously typed text.

---

# Locate Valid Input Field

```python
correct_value = page.locator("input.is-valid")
```

# Locate input elements that contain the class **is-valid**.

Example HTML:

```html
<input class="form-control is-valid" value="correct value">
```

---

# Read Value from Input Field

```python
correct_value.input_value()
```

# Retrieve the current value inside the input field.

Example output:

```
'correct value'
```

---

# Example Full Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    input_field = page.get_by_label("Email address").first

    input_field.fill("ABC")

    input_field.clear()

    input_field.type("ABC")

    input_field.type("ABC", delay=500)

    input_field.clear()

    correct_value = page.locator("input.is-valid")

    print(correct_value.input_value())

    browser.close()
```

---

# Common Text Input Methods in Playwright

| Method | Purpose |
|------|------|
| `fill()` | Replace existing text |
| `type()` | Simulate typing |
| `clear()` | Remove text |
| `input_value()` | Read text from input |

---

# Difference Between `fill()` and `type()`

| Function | Behavior |
|------|------|
| `fill()` | Instantly replaces text |
| `type()` | Types characters one by one |

Example:

```
fill("ABC") → instantly writes ABC
type("ABC") → types A → B → C
```

---

# Why These Functions Are Important

Text input functions are essential for automating:

- Login forms
- Signup forms
- Search functionality
- Form validation

---

# Debugging Tip

Use:

```python
locator.highlight()
```

to visually confirm the correct element before interacting with it.

---

# Key Takeaways

✔ `fill()` replaces text instantly  
✔ `type()` simulates real typing  
✔ `clear()` removes text from input fields  
✔ `input_value()` reads the value from an input element
# Playwright Radio Buttons, Switches, and Checkboxes

This section demonstrates how to interact with **radio buttons, checkboxes, and switches using Playwright**.

These form controls are commonly used in:

- Forms
- Settings panels
- User preferences
- Feature toggles

Playwright provides simple methods to **check, uncheck, and verify selection states**.

Test website used in this example:

https://bootswatch.com/default

---

# Highlight Footer Element

```python
page.locator("footer").highlight()
```

# Highlight the footer section of the page.
# This helps visually confirm that the page has loaded correctly.

---

# Radio Buttons

Radio buttons allow users to **select one option from a group**.

Selecting one radio button automatically **deselects the others**.

---

## Select Radio Button Option Two

```python
radio_btn_2 = page.get_by_label("Option two can be something else and selecting it will deselect option one")
```

# Locate the radio button using its associated label.

---

```python
radio_btn_2.check()
```

# Select the radio button.
# `.check()` ensures the radio button becomes selected.

---

## Select Radio Button Option One

```python
radio_btn_1 = page.get_by_label("Option one is this")
```

```python
radio_btn_1.check()
```

# Selecting this radio button will automatically deselect option two.

---

# Checkboxes

Checkboxes allow users to **select multiple options independently**.

---

## Locate Checkbox

```python
checkbox = page.get_by_label("Default checkbox")
```

# Locate the checkbox using its label text.

---

## Check the Checkbox

```python
checkbox.check()
```

# Select the checkbox.

---

## Uncheck the Checkbox

```python
checkbox.uncheck()
```

# Remove the checkmark from the checkbox.

---

## Verify Checkbox State

```python
checkbox.is_checked()
```

Example output:

```
False
```

# `is_checked()` returns **True or False** depending on the checkbox state.

---

## Check the Checkbox Again

```python
checkbox.check()
```

# Select the checkbox again.

---

# Switch Controls

Switches behave like **toggle buttons**.

They allow enabling or disabling a setting.

---

## Locate Switch

```python
switch_1 = page.get_by_label("Default switch checkbox input")
```

# Locate the switch element using its label.

---

## Turn Switch ON

```python
switch_1.check()
```

# Enable the switch.

---

## Turn Switch OFF

```python
switch_1.uncheck()
```

# Disable the switch.

---

## Toggle Switch Using Click

```python
switch_1.click()
```

# Toggle the switch state.

---

```python
switch_1.click()
```

# Clicking again toggles the switch back.

---

# Example Full Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # Radio buttons
    radio_btn_2 = page.get_by_label("Option two can be something else and selecting it will deselect option one")
    radio_btn_2.check()

    radio_btn_1 = page.get_by_label("Option one is this")
    radio_btn_1.check()

    # Checkbox
    checkbox = page.get_by_label("Default checkbox")

    checkbox.check()
    checkbox.uncheck()

    print(checkbox.is_checked())

    checkbox.check()

    # Switch
    switch_1 = page.get_by_label("Default switch checkbox input")

    switch_1.check()
    switch_1.uncheck()

    switch_1.click()
    switch_1.click()

    browser.close()
```

---

# Common Form Control Methods

| Method | Purpose |
|------|------|
| `check()` | Select radio/checkbox |
| `uncheck()` | Deselect checkbox |
| `click()` | Toggle checkbox or switch |
| `is_checked()` | Verify selection state |

---

# Why These Methods Are Important

These functions are commonly used when testing:

- Login preferences
- Settings panels
- Feature toggles
- Multi-select options

---

# Debugging Tip

Use:

```python
locator.highlight()
```

to visually confirm that Playwright has selected the **correct element**.

---

# Key Takeaways

✔ `check()` selects radio buttons or checkboxes  
✔ `uncheck()` removes selection  
✔ `click()` toggles switches  
✔ `is_checked()` verifies the selection state
# Playwright Dropdown and Multi-Select

This section demonstrates how to interact with **dropdown menus and multi-select lists using Playwright**.

Dropdown elements allow users to select **one or multiple options** from a list.

Playwright provides the `select_option()` method to handle these elements easily.

Test website used in this example:

https://bootswatch.com/default

---

# Single Select Dropdown

A **single select dropdown** allows the user to choose **one option at a time**.

---

## Locate Dropdown Element

```python
single_select = page.get_by_label("Example select")
```

# Locate the dropdown using its associated label **Example select**.

Example HTML:

```html
<select class="form-select">
  <option value="1">1</option>
  <option value="2">2</option>
  <option value="3">3</option>
</select>
```

---

## Select Option by Value

```python
single_select.select_option("2")
```

Output:

```
['2']
```

# Select the option with **value = 2**.

---

## Change Selection

```python
single_select.select_option("4")
```

Output:

```
['4']
```

# Select the option with **value = 4**.

Selecting a new option automatically **replaces the previous selection**.

---

# Multi-Select Dropdown

A **multi-select dropdown** allows selecting **multiple options simultaneously**.

---

## Locate Multi-Select Dropdown

```python
multi_select = page.get_by_label("Example multiple select")
```

# Locate the dropdown labeled **Example multiple select**.

Example HTML:

```html
<select multiple class="form-select">
  <option value="1">1</option>
  <option value="2">2</option>
  <option value="3">3</option>
</select>
```

---

## Select Multiple Options

```python
multi_select.select_option(["2", "5"])
```

Output:

```
['2', '5']
```

# Select options with **values 2 and 5**.

---

## Select Multiple Options Including Previous Ones

```python
multi_select.select_option(["2", "5", "1"])
```

Output:

```
['1', '2', '5']
```

# Select multiple options at the same time.

---

# Example Full Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # Single select dropdown
    single_select = page.get_by_label("Example select")

    single_select.select_option("2")
    single_select.select_option("4")

    # Multi select dropdown
    multi_select = page.get_by_label("Example multiple select")

    multi_select.select_option(["2", "5"])
    multi_select.select_option(["2", "5", "1"])

    browser.close()
```

---

# Common Dropdown Methods in Playwright

| Method | Purpose |
|------|------|
| `select_option(value)` | Select option by value |
| `select_option(label="text")` | Select option by visible text |
| `select_option(index=1)` | Select option by index |

Example:

```python
dropdown.select_option(label="Option 2")
dropdown.select_option(index=2)
```

---

# Why Dropdown Handling Is Important

Dropdown interaction is commonly used when automating:

- Registration forms
- Country selection
- Product filters
- Settings pages

---

# Debugging Tip

Use:

```python
locator.highlight()
```

to visually confirm that Playwright selected the **correct dropdown element**.

---

# Key Takeaways

✔ `select_option()` is used to interact with dropdown menus  
✔ Single dropdowns allow **one selection**  
✔ Multi-select dropdowns allow **multiple selections**  
✔ Playwright can select options by **value, label, or index**
# Playwright Dropdown Links

This section demonstrates how to interact with **dropdown menus that contain clickable links**.

Unlike `<select>` dropdowns, these dropdowns are typically built using **HTML buttons and anchor links (`<a>`)**.

To interact with them in Playwright we usually:

1. Click the dropdown button
2. Locate the visible dropdown items
3. Click the desired link

Test website used in this example:

https://bootswatch.com/default

---

# Locate Dropdown Button

```python
dropdown_menu = page.locator("button#btnGroupDrop1")
```

# Locate the dropdown button using its **ID selector**.

Example HTML:

```html
<button id="btnGroupDrop1" class="btn btn-primary dropdown-toggle">
```

---

# Open the Dropdown Menu

```python
dropdown_menu.click()
```

# Click the button to open the dropdown menu.

---

# Highlight All Dropdown Links

```python
page.locator("a.dropdown-item").highlight()
```

# Locate all links inside the dropdown menu using the class **dropdown-item**.

Example HTML:

```html
<a class="dropdown-item" href="#">Dropdown link</a>
```

---

# Highlight Visible Dropdown Links

```python
page.locator("div.show > a.dropdown-item").highlight()
```

# Locate dropdown links that are currently **visible**.

Explanation:

- `div.show` indicates the dropdown menu is open
- `>` selects direct child links inside the dropdown

---

# Select a Specific Dropdown Link Using `nth`

```python
dropdown_link = page.locator("div.show > a.dropdown-item").nth(2)
```

# Select the **third dropdown link**.

Note:

```
nth(0) → first item  
nth(1) → second item  
nth(2) → third item
```

---

# Highlight the Selected Dropdown Link

```python
dropdown_link.highlight()
```

# Highlight the selected dropdown link for debugging.

---

# Select the Last Dropdown Link

```python
dropdown_link = page.locator("div.show > a.dropdown-item").last
```

# Locate the **last dropdown item**.

---

# Highlight the Last Link

```python
dropdown_link.highlight()
```

---

# Click the Dropdown Link

```python
dropdown_link.click()
```

# Click the selected dropdown link.

---

# Select the First Dropdown Link

```python
dropdown_link = page.locator("div.show > a.dropdown-item").first
```

# Locate the **first dropdown item**.

---

# Example Full Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # Open dropdown menu
    dropdown_menu = page.locator("button#btnGroupDrop1")
    dropdown_menu.click()

    # Highlight dropdown items
    page.locator("a.dropdown-item").highlight()

    # Select third dropdown link
    dropdown_link = page.locator("div.show > a.dropdown-item").nth(2)
    dropdown_link.highlight()

    # Select last dropdown link
    dropdown_link = page.locator("div.show > a.dropdown-item").last
    dropdown_link.highlight()

    dropdown_link.click()

    browser.close()
```

---

# Common Dropdown Link Methods

| Method | Purpose |
|------|------|
| `first` | Select first element |
| `last` | Select last element |
| `nth(index)` | Select element by index |
| `click()` | Click dropdown link |

---

# Why This Technique Is Important

Many modern websites use **custom dropdown components instead of `<select>` elements**.

These dropdowns require:

- Clicking a button
- Selecting links inside a menu

This approach is common in:

- Navigation menus
- Filter menus
- Settings menus

---

# Debugging Tip

Use:

```python
locator.highlight()
```

to visually confirm that Playwright selected the **correct dropdown element**.

---

# Key Takeaways

✔ Some dropdowns contain **links instead of `<option>` elements**  
✔ Use `click()` to open dropdown menus  
✔ Use `locator()` to find dropdown links  
✔ Use `first`, `last`, or `nth()` to select specific items
# Playwright File Inputs and File Uploads

This section demonstrates how to **upload files using Playwright**.

File uploads are commonly used in automation testing for:

- Uploading profile pictures
- Submitting documents
- Uploading test data
- Testing file validation

Playwright provides **two main methods** for file uploads:

1️⃣ Using `set_input_files()`  
2️⃣ Using the **file chooser dialog**

Test website used in this example:

https://bootswatch.com/default

---

# Method 1 — Upload File Using `set_input_files()`

This is the **simplest and most common method**.

---

## Locate File Input Field

```python
file_input = page.get_by_label("Default file input example")
```

# Locate the file upload input using its label.

Example HTML:

```html
<input type="file" class="form-control">
```

---

## Upload a File

```python
file_input.set_input_files("Xpath-functions.py")
```

# Upload the file **Xpath-functions.py**.

Playwright automatically sets the file path into the file input.

---

# Method 2 — Upload File Using File Chooser

Some websites trigger the **system file chooser dialog** when clicking a file upload button.

Playwright allows handling this using `expect_file_chooser()`.

---

## Wait for File Chooser

```python
with page.expect_file_chooser() as fc_info:
    file_input.click()
```

# Click the file input element and wait for the file chooser dialog to open.

---

## Get the File Chooser Object

```python
file_chooser = fc_info.value
```

# Retrieve the file chooser object.

---

## Upload File Through File Chooser

```python
file_chooser.set_files("text_input.py")
```

# Upload the file **text_input.py**.

---

## Upload Another File

```python
file_chooser.set_files("css-hierarchy.py")
```

# Upload the file **css-hierarchy.py**.

---

# Example Full Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    # Method 1: Direct file upload
    file_input = page.get_by_label("Default file input example")
    file_input.set_input_files("Xpath-functions.py")

    # Method 2: File chooser dialog
    with page.expect_file_chooser() as fc_info:
        file_input.click()

    file_chooser = fc_info.value

    file_chooser.set_files("text_input.py")

    browser.close()
```

---

# Common File Upload Methods in Playwright

| Method | Purpose |
|------|------|
| `set_input_files()` | Upload file directly |
| `expect_file_chooser()` | Handle system file dialog |
| `set_files()` | Upload file through file chooser |

---

# Why File Upload Automation Is Important

File upload testing is required for:

- Document submission systems
- Image upload forms
- Resume upload portals
- Profile picture uploads

---

# Debugging Tip

If the file upload fails:

- Ensure the **file path is correct**
- Ensure the **file exists in the project directory**

Example absolute path:

```python
file_input.set_input_files("/Users/abubakar/playwright-python-project/file.txt")
```

---

# Key Takeaways

✔ `set_input_files()` is the **fastest way to upload files**  
✔ `expect_file_chooser()` handles **system file dialogs**  
✔ `set_files()` uploads files through the chooser  
✔ File uploads are common in **form automation tests**
# Playwright Keyboard Shortcuts

This section demonstrates how to simulate **keyboard actions in Playwright** using the `press()` method.

Keyboard automation is useful for:

- Typing shortcuts
- Navigating text fields
- Selecting text
- Triggering keyboard-based UI actions

Test website used in this example:

https://bootswatch.com/default

---

# Locate the Textarea

```python
textarea = page.get_by_label("Example textarea")
```

Locate the textarea element using its label.

Example HTML:

```html
<textarea rows="3" class="form-control" id="exampleTextarea"></textarea>
```

---

# Fill Text

```python
textarea.fill("word")
```

Fill the textarea with the text **word**.

---

# Clear the Field

```python
textarea.clear()
```

Remove all text from the textarea.

---

# Press a Key

```python
textarea.press("KeyW")
```

Simulate pressing the **W key**.

Playwright uses **standard keyboard key names**.

---

# Use Shift + Key

```python
textarea.press("Shift+KeyW")
```

Simulate pressing **Shift + W** (capital letter).

---

# Press Another Key

```python
textarea.press("KeyO")
```

Simulate pressing the **O key**.

---

# Shift + Key Combination

```python
textarea.press("Shift+KeyO")
```

Simulate pressing **Shift + O**.

---

# Arrow Keys

Move the cursor using arrow keys.

```python
textarea.press("ArrowLeft")
```

Move cursor left.

```python
textarea.press("ArrowRight")
```

Move cursor right.

---

# Select All Text

```python
textarea.press("Control+KeyA")
```

Select all text inside the textarea.

Note:

On **macOS**, the equivalent shortcut is usually:

```python
textarea.press("Meta+KeyA")
```

Meta represents the **Command (⌘)** key.

---

# Example Full Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default")

    textarea = page.get_by_label("Example textarea")

    textarea.fill("word")
    textarea.clear()

    textarea.press("KeyW")
    textarea.press("Shift+KeyW")

    textarea.press("KeyO")
    textarea.press("Shift+KeyO")

    textarea.press("ArrowLeft")
    textarea.press("ArrowRight")

    textarea.press("Control+KeyA")

    browser.close()
```

---

# Common Keyboard Keys in Playwright

| Key | Purpose |
|----|----|
| `KeyA` | Letter A |
| `KeyW` | Letter W |
| `Enter` | Press Enter |
| `ArrowLeft` | Move cursor left |
| `ArrowRight` | Move cursor right |
| `Backspace` | Delete previous character |
| `Tab` | Move to next field |

---

# Common Keyboard Modifiers

| Modifier | Meaning |
|------|------|
| `Shift` | Uppercase or secondary function |
| `Control` | Control key |
| `Alt` | Alt key |
| `Meta` | Command key (Mac) |

Example combinations:

```python
textarea.press("Shift+KeyA")
textarea.press("Control+KeyA")
textarea.press("Alt+KeyF")
```

---

# Why Keyboard Automation Is Important

Keyboard actions are commonly used when testing:

- Text editors
- Keyboard shortcuts
- Accessibility features
- Form navigation

---

# Debugging Tip

You can slow down typing using:

```python
textarea.type("Hello", delay=300)
```

This simulates **real user typing**.

---

# Key Takeaways

✔ `press()` simulates keyboard key presses  
✔ Key combinations use `Modifier+Key` format  
✔ Arrow keys can control cursor movement  
✔ `Control+KeyA` selects all text  
✔ Keyboard testing helps validate **real user interactions**
# Playwright Navigation Wait States (`wait_until`)

When Playwright navigates to a page using `page.goto()`, it can **wait for different loading stages** before continuing the script.

These loading strategies are controlled using the **`wait_until` parameter**.

Understanding these states is important for **automation reliability and performance testing**.

---

# Why Navigation Wait States Matter

Different websites load resources at different times:

- HTML loads first
- CSS and JavaScript load later
- API calls may continue loading after the page appears

Playwright allows choosing **when the navigation should be considered "complete"**.

This helps:

✔ Avoid flaky tests  
✔ Improve automation speed  
✔ Handle dynamic websites correctly

---

# Available `wait_until` States

| State | Description |
|------|------|
| `commit` | Navigation is considered finished once the response is received and the document starts loading |
| `domcontentloaded` | Page DOM is fully loaded (HTML parsed) |
| `load` | Page and all resources (images, CSS, scripts) are fully loaded |
| `networkidle` | No network activity for at least **500 ms** |
| `default` | Uses Playwright's default navigation strategy |

---

# Example Script: Compare Page Load Times

The following script measures how long a page takes to load using different **Playwright navigation strategies**.

```python
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
```

---

# What the Script Does

1. Defines different **navigation strategies**
2. Opens the browser for each strategy
3. Navigates to the Playwright website
4. Measures page load time using `perf_counter`
5. Prints the result for comparison

Example output:

```
Loading page using strategy: commit
Page loaded in 0.45 seconds

Loading page using strategy: domcontentloaded
Page loaded in 0.78 seconds

Loading page using strategy: load
Page loaded in 1.21 seconds
```

---

# When to Use Each Wait Strategy

### `commit`

Best for:

- Performance measurements
- Very fast navigation
- API testing

---

### `domcontentloaded`

Best for:

- When HTML must be loaded
- JavaScript-heavy websites
- Most automation scripts

---

### `load`

Best for:

- When images and resources must load
- UI verification tests

---

### `networkidle`

Best for:

- Single-page applications
- Websites with many API calls

Note:

Playwright documentation warns that **`networkidle` should be used cautiously**, because some sites continuously make network requests.

---

# Recommended Strategy for Automation

Most Playwright automation uses:

```python
page.goto(url, wait_until="domcontentloaded")
```

This balances **speed and reliability**.

---

# Debugging Tip

If your script fails because elements are not ready:

Use:

```python
page.wait_for_selector("element")
```

Example:

```python
page.wait_for_selector("button")
```

This ensures the element exists before interacting with it.

---

# Key Takeaways

✔ `wait_until` controls **when navigation is considered complete**  
✔ `commit` is the fastest  
✔ `domcontentloaded` is the most commonly used  
✔ `load` waits for full page resources  
✔ `networkidle` waits until network activity stops  

Understanding these states helps create **stable and faster Playwright automation scripts**.
# Playwright Custom Wait States

Modern web applications often load data **dynamically using AJAX or API calls**.  
In these cases, elements may appear **after the initial page load**.

Playwright provides several ways to **wait for elements to appear or become usable**.

This example demonstrates how different **custom waiting strategies** affect the time required for movie data to load on a dynamic webpage.

Test website used:

https://www.scrapethissite.com/pages/ajax-javascript/

---

# Purpose of the Script

The script performs the following steps:

1. Opens the AJAX movie page
2. Clicks the **2015** link
3. The website loads movie data using **AJAX**
4. The script waits for the movie table to appear using different strategies
5. It measures how long each strategy takes

---

# Waiting Strategies Tested

| Strategy | Description |
|--------|-------------|
| `default` | No explicit wait (Playwright auto-waiting) |
| `visible` | Wait until the element becomes visible |
| `attached` | Wait until the element is attached to the DOM |
| `wait_for_selector` | Explicitly wait for a selector to appear |

---

# Example Script

```python
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
            headless=False,
            slow_mo=500
        )

        # Create a new browser tab
        page = browser.new_page()

        # Start performance timer
        start_time = perf_counter()

        # Navigate to AJAX movie page
        page.goto(URL)

        # Click the "2015" year link
        year_link = page.get_by_role("link", name="2015")
        year_link.click()

        # Locator for first movie title
        film_title = page.locator("td.film-title").first

        # Apply different waiting strategies
        if wait_state == "default":
            pass

        elif wait_state == "wait_for_selector":
            page.wait_for_selector("td.film-title")

        else:
            film_title.wait_for(state=wait_state)

        # Stop timer
        load_time = perf_counter() - start_time

        print(f"Movies loaded in {round(load_time, 2)} seconds")

        browser.close()
```

---

# Script Output

Example output from running the script:

```
Loading movies using wait strategy: default
Movies loaded in 2.61 seconds

Loading movies using wait strategy: visible
Movies loaded in 3.64 seconds

Loading movies using wait strategy: attached
Movies loaded in 3.58 seconds

Loading movies using wait strategy: wait_for_selector
Movies loaded in 3.98 seconds
```

---

# Explanation of Results

### Default (2.61 seconds)

- Fastest execution
- Relies on **Playwright's built-in auto-waiting**
- Works well in many scenarios

---

### Visible (3.64 seconds)

Waits until the element:

- Exists in the DOM
- Is visible on the page

Useful when interacting with elements users must see.

---

### Attached (3.58 seconds)

Waits until the element is **present in the DOM** but may not yet be visible.

Useful when checking **background DOM updates**.

---

### wait_for_selector (3.98 seconds)

Explicit wait until the selector appears.

This method is often used when:

- Elements load asynchronously
- Tests need guaranteed element presence

---

# Common Element Wait States

| State | Meaning |
|-----|------|
| `attached` | Element exists in DOM |
| `detached` | Element removed from DOM |
| `visible` | Element visible to user |
| `hidden` | Element exists but hidden |

Example:

```python
locator.wait_for(state="visible")
```

---

# When to Use Custom Waits

Custom waits are useful when testing:

- AJAX content
- Single Page Applications (SPA)
- Lazy-loaded elements
- Dynamic UI updates

---

# Best Practice

Playwright recommends relying on **auto-waiting whenever possible**.

Use explicit waits only when necessary.

Example:

```python
page.wait_for_selector("table.movies")
```

---

# Key Takeaways

✔ Playwright provides **built-in auto-waiting**  
✔ Custom waits help handle **dynamic content**  
✔ `visible` ensures element is ready for interaction  
✔ `attached` ensures element exists in DOM  
✔ `wait_for_selector()` provides explicit control over waiting
# Playwright Event Listeners

Playwright allows you to listen to **browser and page events**.  
Event listeners are useful for monitoring what happens inside the browser while automation is running.

They are commonly used for:

- Debugging network activity
- Monitoring page navigation
- Handling file uploads
- Observing JavaScript errors
- Tracking console messages

Playwright uses the `.on()` method to register event listeners.

---

# Common Playwright Page Events

| Event | Description |
|------|-------------|
| `load` | Fired when the page fully loads |
| `domcontentloaded` | Fired when the HTML DOM has finished loading |
| `request` | Triggered when the browser sends a network request |
| `response` | Triggered when a server response is received |
| `console` | Fired when the browser console logs a message |
| `pageerror` | Triggered when JavaScript errors occur |
| `filechooser` | Fired when a file upload dialog opens |
| `close` | Triggered when the page closes |

---

# Example Script

This script demonstrates how to listen to different **Playwright page events**.

```python
from playwright.sync_api import sync_playwright

"""
This script demonstrates how to listen to different Playwright page events.

Events are useful for:
- debugging network activity
- monitoring navigation
- handling file uploads
- observing browser lifecycle actions
"""

# -------------------------
# Event Callback Functions
# -------------------------

def on_load(page):
    print("Page finished loading:", page.url)


def on_close(page):
    print("Page has been closed.")


def on_request(request):
    print("Request sent:", request.method, request.url)


def on_response(response):
    print("Response received:", response.status, response.url)


def on_domcontentloaded(page):
    print("DOM fully loaded for:", page.url)


def on_filechooser(file_chooser):
    print("File chooser opened")
    file_chooser.set_files("input_files.py")


def on_console(message):
    print("Console message:", message.text)


def on_pageerror(error):
    print("Page JavaScript error:", error)


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

    browser.close()
```

---

# How Event Listeners Work

Event listeners follow this structure:

```python
page.on("event_name", callback_function)
```

Example:

```python
page.on("request", on_request)
```

Whenever a **network request is sent**, the function `on_request()` will automatically run.

---

# Example Console Output

When running the script, you may see output similar to:

```
Request sent: GET https://bootswatch.com/default
Response received: 200 https://bootswatch.com/default
DOM fully loaded for: https://bootswatch.com/default
Page finished loading: https://bootswatch.com/default
File chooser opened
Page has been closed.
```

---

# Why Event Listeners Are Useful

Event listeners help when testing:

### Network Monitoring

```python
page.on("request", handler)
page.on("response", handler)
```

Used to monitor API calls.

---

### Debugging JavaScript

```python
page.on("console", handler)
page.on("pageerror", handler)
```

Used to capture browser console logs and errors.

---

### Handling File Uploads

```python
page.on("filechooser", handler)
```

Used when a website opens the **system file upload dialog**.

---

### Tracking Page Lifecycle

```python
page.on("load", handler)
page.on("domcontentloaded", handler)
```

Used to monitor page loading stages.

---

# Best Practice

Register event listeners **before navigation** so that no events are missed.

Example:

```python
page.on("request", on_request)
page.goto("https://example.com")
```

---

# Key Takeaways

✔ Event listeners allow monitoring browser activity  
✔ `.on()` registers event handlers  
✔ Useful for debugging and automation monitoring  
✔ Commonly used for network requests, console logs, and file uploads  
✔ Helps build more **powerful Playwright automation frameworks**
# Playwright Handling JavaScript Dialogs

Web applications sometimes display **JavaScript dialogs** that require user interaction.

Common dialog types include:

- **Alert**
- **Confirm**
- **Prompt**

Playwright allows you to automatically handle these dialogs using the **`dialog` event listener**.

---

# Types of JavaScript Dialogs

| Dialog Type | Description |
|-------------|-------------|
| `alert` | Displays a message with an **OK** button |
| `confirm` | Displays a message with **OK** and **Cancel** |
| `prompt` | Allows the user to enter text |

---

# Example Script

The following script demonstrates how to handle all three dialog types using Playwright.

It performs these actions:

1. Accepts the **alert dialog**
2. Cancels the **confirm dialog the first time**
3. Accepts the **confirm dialog the second time**
4. Sends text to the **prompt dialog**

```python
from playwright.sync_api import sync_playwright

"""
This script demonstrates how to handle JavaScript dialogs in Playwright.

The page contains three buttons that trigger:
1. Alert dialog
2. Confirm dialog
3. Prompt dialog
"""

# Buttons that trigger dialogs
buttons = [
    "Show alert box",
    "Show confirm box",
    "Show confirm box",
    "Show prompt box"
]

# Variable to track confirm dialog behavior
confirm_cancelled = False


def handle_dialog(dialog):

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
            dialog.dismiss()
            confirm_cancelled = True
        else:
            print("Accepting confirm dialog")
            dialog.accept()

    # Handle PROMPT dialog
    elif dialog.type == "prompt":
        print("Sending text to prompt dialog")
        dialog.accept("Playwright is cool with Python")


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=1500
    )

    page = browser.new_page()

    # Register dialog event listener
    page.on("dialog", handle_dialog)

    # Open demo alerts page
    page.goto("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

    # Click each dialog button
    for button in buttons:
        print(f"\nClicking button: {button}")

        dialog_button = page.get_by_text(button)
        dialog_button.click()

    browser.close()
```

---

# Understanding the `dialog` Event

Playwright listens for dialogs using:

```python
page.on("dialog", handler_function)
```

Example:

```python
page.on("dialog", handle_dialog)
```

Whenever a dialog appears, the **handler function is automatically triggered**.

---

# Dialog Methods

| Method | Description |
|------|-------------|
| `dialog.accept()` | Clicks **OK** |
| `dialog.dismiss()` | Clicks **Cancel** |
| `dialog.accept("text")` | Sends text to a prompt dialog |

---

# Example Console Output

Example output from the script:

```
Dialog opened
Dialog type: alert
Dialog message: I am an alert box!
Accepting alert dialog

Dialog opened
Dialog type: confirm
Dialog message: I am a confirm alert
Cancelling confirm dialog (first time)

Dialog opened
Dialog type: confirm
Dialog message: I am a confirm alert
Accepting confirm dialog

Dialog opened
Dialog type: prompt
Dialog message: I prompt you
Sending text to prompt dialog
```

---

# Best Practice

Always register the dialog listener **before triggering the dialog**.

Correct:

```python
page.on("dialog", handle_dialog)
page.click("button")
```

Incorrect:

```python
page.click("button")
page.on("dialog", handle_dialog)
```

---

# Key Takeaways

✔ JavaScript dialogs must be handled using the **`dialog` event**  
✔ Playwright automatically pauses execution until the dialog is handled  
✔ `accept()` clicks **OK**  
✔ `dismiss()` clicks **Cancel**  
✔ `accept("text")` sends input to **prompt dialogs**
# Playwright Handling File Downloads

Playwright provides built-in support for **handling file downloads** during browser automation.

Using Playwright, we can:

- Detect when a download starts
- Capture download information
- Save downloaded files locally
- Verify downloaded files

This is useful for testing:

- Report downloads
- Image downloads
- Document exports
- File attachments

---

# Playwright Download APIs

Playwright provides the following methods to handle downloads:

| Method | Purpose |
|------|------|
| `page.expect_download()` | Wait for a download to start |
| `download.save_as()` | Save the downloaded file |
| `download.url` | Get the download URL |
| `download.suggested_filename` | Get the suggested file name |

---

# Example Script

The following script demonstrates how to capture and save a downloaded file.

Steps performed:

1. Open the **Unsplash website**
2. Click an image
3. Click the **Download free** button
4. Capture the download event
5. Save the downloaded file locally

```python
from playwright.sync_api import sync_playwright

"""
This script demonstrates how to handle file downloads in Playwright.

Steps performed:
1. Open the Unsplash website.
2. Click an image to open its detail page.
3. Click the "Download free" button.
4. Capture the download event.
5. Save the downloaded file locally.
"""


def handle_download(download):

    # Print information about the download
    print("Download started...")
    print("File URL:", download.url)
    print("Suggested filename:", download.suggested_filename)

    # Save the file locally
    download.save_as(download.suggested_filename)

    print("Download saved successfully.")


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=1500
    )

    page = browser.new_page()

    # Navigate to Unsplash
    page.goto("https://unsplash.com/s/photos/free")

    # Click an image
    image = page.get_by_alt_text(
        "silhouette of person standing on rock surrounded by body of water"
    )
    image.click()

    # Locate download button
    download_button = page.get_by_role("link", name="Download free")

    # Listen for download event
    page.once("download", handle_download)

    # Expect download to start
    with page.expect_download() as download_info:
        download_button.click()

    # Get download object
    download = download_info.value

    print("Download completed:", download.suggested_filename)

    browser.close()
```

---

# How `expect_download()` Works

Playwright waits for the **download event** triggered by a user action.

Example:

```python
with page.expect_download() as download_info:
    download_button.click()
```

After the download starts:

```python
download = download_info.value
```

This gives access to the **Download object**.

---

# Access Download Information

Playwright provides useful download metadata.

Example:

```python
print(download.url)
print(download.suggested_filename)
```

Example output:

```
Download started...
File URL: https://images.unsplash.com/photo123.jpg
Suggested filename: photo123.jpg
```

---

# Save Downloaded File

To save the downloaded file locally:

```python
download.save_as(download.suggested_filename)
```

You can also specify a custom path:

```python
download.save_as("downloads/image.jpg")
```

---

# Using Download Event Listener

You can also listen to downloads using:

```python
page.once("download", handle_download)
```

This ensures the handler runs **only once** when a download occurs.

---

# Best Practice

Always wrap download actions with:

```python
page.expect_download()
```

This ensures Playwright reliably captures the download event.

---

# Key Takeaways

✔ Playwright can capture and control file downloads  
✔ `expect_download()` waits for download events  
✔ `download.save_as()` stores files locally  
✔ `download.suggested_filename` provides the file name  
✔ Download handling is useful for testing reports and attachments
# Playwright Synchronous vs Asynchronous API

Playwright provides **two APIs in Python**:

1. **Synchronous API**
2. **Asynchronous API**

Both APIs provide the same browser automation features, but they differ in **how tasks are executed**.

---

# Synchronous Playwright

The **synchronous API** executes commands **one after another**.

Each operation **waits until the previous one finishes** before continuing.

This makes the code:

- Easier to read
- Easier for beginners
- Similar to traditional Python scripts

Example:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://example.com")

    print(page.title())

    browser.close()
```

Execution order:

```
launch browser
↓
open page
↓
navigate to site
↓
get title
↓
close browser
```

Everything runs **step-by-step**.

---

# Asynchronous Playwright

The **asynchronous API** uses **Python's asyncio framework**.

Operations are executed using **coroutines** with the `async` and `await` keywords.

This allows the program to **handle multiple tasks efficiently without blocking execution**.

Async Playwright is useful for:

- High-performance web scraping
- Parallel browser automation
- Handling multiple pages simultaneously
- Scalable automation frameworks

---

# Key Differences

| Feature | Synchronous API | Asynchronous API |
|-------|----------------|----------------|
| Execution | Sequential | Non-blocking |
| Keywords | None | `async` / `await` |
| Framework | Standard Python | `asyncio` |
| Complexity | Easier | More advanced |
| Performance | Slower for large workloads | Faster for concurrent tasks |

---

# Example: Playwright Async Script

The following script demonstrates **browser automation using the Async Playwright API**.

Steps performed:

1. Launch Chromium
2. Open a new page
3. Navigate to Unsplash
4. Retrieve the page title
5. Close the browser

```python
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
"""


async def main():
    """
    Main asynchronous function that runs the browser automation.
    """

    # Start Playwright
    async with async_playwright() as p:

        # Launch Chromium browser
        browser = await p.chromium.launch(
            headless=False
        )

        # Create a new browser tab
        page = await browser.new_page()

        # Target URL
        url = "https://www.unsplash.com"

        # Navigate to webpage
        await page.goto(url)

        # Retrieve page title
        title = await page.title()

        # Print page title
        print("Page Title:", title)

        # Close browser
        await browser.close()


# Run async program
asyncio.run(main())
```

---

# Understanding `async` and `await`

| Keyword | Purpose |
|------|------|
| `async` | Defines an asynchronous function |
| `await` | Waits for an asynchronous task to complete |
| `asyncio.run()` | Starts the async event loop |

Example:

```python
await page.goto(url)
```

The script **waits for navigation to finish** before continuing.

---

# When to Use Sync vs Async

### Use Sync API when

- Learning Playwright
- Writing simple automation scripts
- Running tests with pytest
- Building UI automation

---

### Use Async API when

- Running many browser tasks
- Web scraping at scale
- Handling multiple pages concurrently
- Building high-performance systems

---

# Playwright Recommendation

Playwright documentation suggests:

- **Sync API** → best for **testing frameworks**
- **Async API** → best for **advanced automation and scraping**

---

# Key Takeaways

✔ Playwright provides **two APIs in Python**  
✔ Sync API executes **step-by-step**  
✔ Async API uses **asyncio for non-blocking execution**  
✔ Async is better for **performance and concurrency**  
✔ Sync is easier for **testing and beginners**
# Playwright Authentication: Reusing Login Session with `storage_state`

When automating websites that require authentication (such as **Google sign-in**), logging in every time can slow down tests.

Playwright allows us to **save authentication data** (cookies and local storage) and **reuse it in future sessions**.

This is done using:

```
storage_state
```

The authentication state is saved in a **JSON file** and reused whenever the browser launches.

---

# Why Use Storage State?

Without session reuse:

```
Script starts
↓
Login page opens
↓
Enter email
↓
Enter password
↓
Authenticate
↓
Run automation
```

With session reuse:

```
Script starts
↓
Load stored authentication state
↓
Already logged in
↓
Run automation immediately
```

Benefits:

✔ Faster automation  
✔ Avoid repeated login steps  
✔ Useful for testing authenticated pages  
✔ Ideal for automation frameworks

---

# Playwright Authentication Flow

Typical workflow:

### Step 1 — Login Once

Log in manually or via automation.

### Step 2 — Save Session

```
context.storage_state(path="session.json")
```

This stores:

- cookies
- local storage
- authentication tokens

---

### Step 3 — Reuse Session

Load the saved session:

```
browser.new_context(storage_state="session.json")
```

Now the browser opens **already authenticated**.

---

# Example: Google Sign-In Session Reuse

This example demonstrates how to:

1. Launch Chromium browser
2. Load stored authentication state
3. Open Google Accounts page
4. Save updated session state

---

# Example Script

```python
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
"""


def run():

    with sync_playwright() as p:

        # Launch Chromium browser
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000,
            args=[
                "--disable-dev-shm-usage",
                "--disable-blink-features=AutomationControlled"
            ]
        )

        # Create browser context with saved session
        context = browser.new_context(
            viewport={"width": 820, "height": 920},
            storage_state="playwright/auth/session.json"
        )

        # Open a new browser tab
        page = context.new_page()

        # Navigate to Google Accounts page
        page.goto("https://accounts.google.com")

        # Print page title
        print("Page title:", page.title())

        # Save updated authentication state
        context.storage_state(path="playwright/auth/session.json")

        print("Session state saved successfully.")

        # Close context and browser
        context.close()
        browser.close()


if __name__ == "__main__":
    run()
```

---

# Creating the Initial Session File

If the session file **does not exist**, you can login once manually.

Example:

```python
email_input = page.locator("input[name='identifier']")
email_input.fill("example@gmail.com")

next_button = page.get_by_role("button", name="Next")
next_button.click()

page.pause()
```

The `page.pause()` command opens **Playwright Inspector**, allowing you to manually enter the password.

Once logged in:

```
context.storage_state(path="playwright/auth/session.json")
```

Now the session file is created.

---

# Example Session File

Example structure of `session.json`:

```json
{
  "cookies": [
    {
      "name": "SID",
      "value": "example_cookie_value",
      "domain": ".google.com"
    }
  ],
  "origins": []
}
```

This file contains:

- authentication cookies
- local storage data
- session information

---

# Browser Contexts in Playwright

A **browser context** is like a separate browser profile.

Each context has its own:

- cookies
- storage
- sessions
- cache

Example:

```python
context = browser.new_context(storage_state="session.json")
```

This loads the saved login session.

---

# Debugging Authentication

Helpful Playwright debugging commands:

```python
page.pause()
```

Opens the **Playwright Inspector**.

---

```python
page.context.storage_state()
```

Prints the current storage state.

---

# Project Folder Structure

Recommended structure for authentication reuse:

```
playwright-python-project
│
├── playwright
│   └── auth
│       └── session.json
│
├── scripts
│   └── google_login.py
│
└── venv
```

---

# Key Takeaways

✔ Playwright can reuse login sessions  
✔ Authentication data is stored in **JSON files**  
✔ `storage_state` loads saved cookies and local storage  
✔ Helps skip login steps in automation  
✔ Useful for **authenticated test environments**
# Playwright Automated Mail Checker (Gmail Unread Email Extractor)

This example demonstrates how to use **Playwright with Python** to automatically scan a **Gmail inbox** and extract information from unread emails.

The script:

1. Opens Gmail using a previously saved login session
2. Scans the inbox
3. Detects unread emails
4. Extracts important details such as:
   - Sender name
   - Sender email
   - Subject
   - Email preview text

⚠️ The script **does not open the email messages**.  
It only reads information directly from the **inbox view**.

---

# Prerequisite

The script requires a previously saved authentication session:

```
playwright/auth/session.json
```

This file contains the Gmail login cookies and storage state.

See the **Playwright Authentication section** to learn how to generate this file.

---

# How the Script Works

The automation follows these steps:

```
Launch browser
↓
Load saved Gmail session
↓
Open Gmail inbox
↓
Scan inbox rows
↓
Detect unread emails
↓
Extract sender, subject, preview
↓
Print email summary
```

---

# Example Script

```python
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

        # Count email rows
        email_count = page.locator("//tr[@tabindex='-1']").count()

        print("\nemails found:", email_count)

        print("\n---- Unread Email Summary ----")

        i = 0

        emails = page.locator("div.UI table tr")

        for email in emails.all():

            # Check if the email is unread
            is_new_email = email.locator("td li[data-tooltip='Mark as read']").count() == 1

            if is_new_email:

                i += 1

                sender = email.locator("span").nth(2).get_attribute("name")
                sender_email = email.locator("span").nth(2).get_attribute("email")
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
```

---

# Example Output

Example terminal output:

```
emails found: 25

---- Unread Email Summary ----

-----------------------
Sender : GitHub
Sender email : noreply@github.com
Subject : New login to your account
Preview: A new sign-in was detected...
-----------------------

-----------------------
Sender : LinkedIn
Sender email : notifications@linkedin.com
Subject : 5 new job recommendations
Preview: Based on your profile we found...
-----------------------

Finished scanning inbox.
There were 2 unread emails
```

---

# Key Playwright Techniques Used

| Technique | Purpose |
|------|------|
| `storage_state` | Reuse Gmail login session |
| `locator()` | Locate email rows in inbox |
| `count()` | Count matching elements |
| `get_attribute()` | Extract sender metadata |
| `text_content()` | Extract email subject |
| `inner_text()` | Extract preview text |

---

# Detecting Unread Emails

The script determines if an email is unread using:

```python
email.locator("td li[data-tooltip='Mark as read']")
```

If this element exists, the email is **unread**.

---

# Why This Automation Is Useful

This type of automation is useful for:

- Email monitoring systems
- Notification dashboards
- Automated alert systems
- Workflow automation
- Email scraping tools

---

# Important Notes

⚠️ Gmail's UI structure can change over time.

If the script stops working:

- Inspect Gmail elements using browser DevTools
- Update the Playwright locators

---

# Possible Improvements

You could extend this script to:

- Save emails to a **CSV file**
- Send **Slack notifications**
- Store results in a **database**
- Automatically **open unread emails**
- Download **email attachments**

---

# Key Takeaways

✔ Playwright can automate **web-based email clients**

✔ Gmail sessions can be reused using **storage_state**

✔ Inbox data can be extracted **without opening emails**

✔ This technique is useful for **email automation workflows**
