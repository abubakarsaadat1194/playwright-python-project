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

# Environment and IDE Setup

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

# Authentication and Session Handling

- [Playwright Authentication: Reusing Login Session with storage_state](#playwright-authentication-reusing-login-session-with-storage_state)

---

# Automation Projects

- [Playwright Automated Mail Checker (Gmail Unread Email Extractor)](#playwright-automated-mail-checker-gmail-unread-email-extractor)

---

# Python Development Best Practices

- [Python Type Hinting Guide](#python-type-hinting-guide)

---

# Testing with Pytest

- [Pytest JSON Test Report Generator](#pytest-json-test-report-generator)
- [Writing Tests with Pytest](#writing-tests-with-pytest)
- [Running Tests with Configuration](#running-tests-with-configuration)
- [Benefits of Using pytest.ini](#benefits-of-using-pytestini)
- [Example Project Structure](#example-project-structure)
- [Overriding pytest.ini Options](#overriding-pytestini-options)

---

## Pytest Fixtures and Test Hooks

- [Test Hooks and Fixtures in Pytest](#test-hooks-and-fixtures-in-pytest-playwright)

---

## Debugging and Test Artifacts

- [Taking Screenshots with Playwright](#taking-screenshots-with-playwright)
- [Recording Test Videos with Playwright](#recording-test-videos-with-playwright)
- [Playwright Tracing (Debugging with Trace Viewer)](#playwright-tracing-debugging-with-trace-viewer)

---

## Playwright Web-First Assertions

- [Web-First Assertions on Page](#web-first-assertions-in-playwright-assertions-on-page)
- [Web-First Assertions on Elements](#web-first-assertions-on-elements-locator-assertions)
- [Web-First Assertions on Element Text](#web-first-assertions-on-element-text)
- [Web-First Assertions on Element Attributes](#web-first-assertions-on-element-attributes)
- [Web-First Assertions on Input Fields](#web-first-assertions-on-input-fields)
- [Web-First Assertions for Checkboxes](#web-first-assertions-for-checkboxes)
- [Web-First Assertions for Option Menus](#web-first-assertions-for-option-menus-select-dropdowns)

---

## UI Testing Playground Automation Scenarios

- [Overlapped Element Handling](#ui-testing-playground--overlapped-element-handling)
- [Handling AJAX Requests](#ui-testing-playground--handling-ajax-requests)
- [Sample App Login Automation](#ui-testing-playground--sample-app-login-form-automation)
- [Handling Dynamic Class Attributes](#ui-testing-playground--handling-dynamic-class-attributes)
- [Handling Dynamic IDs](#ui-testing-playground--handling-dynamic-ids)
- [Dynamic Table Validation](#ui-testing-playground--dynamic-table-validation)
- [Hidden Layers (Click Interception)](#ui-testing-playground--hidden-layers-click-interception)
- [Load Delay (Handling Delayed Elements)](#ui-testing-playground--load-delay-handling-delayed-elements)
- [Mouse Over Interactions](#ui-testing-playground--mouse-over-hover--double-click-actions)
- [Handling Non-Breaking Space](#ui-testing-playground--non-breaking-space-handling-special-characters-in-locators)
- [Progress Bar Handling](#ui-testing-playground--progress-bar-handling-dynamic-ui-updates)
- [Scrollbars (Handling Elements Outside Viewport)](#ui-testing-playground--scrollbars-handling-elements-outside-the-viewport)
- [Text Input Dynamic UI Updates](#ui-testing-playground--text-input-dynamic-ui-update)
- [Click Event Handling](#ui-testing-playground--click-handling-real-user-click-events)
- [Visibility States Testing](#ui-testing-playground--visibility-understanding-different-hidden-element-states)

### Playwright UI Automation (Page Object Model)

- [Page Object Model (POM)](#page-object-model-pom)
- [Project Structure](#project-structure)
- [Page Object Implementation](#page-object-implementation)
- [Test Implementation](#test-implementation)
- [Running the Tests](#running-the-tests)
- [Key Automation Concepts Demonstrated](#key-automation-concepts-demonstrated)
- [Future Enhancements](#future-enhancements)
- [Learning Objective](#learning-objective)

### Playwright Documentation Automation Example

- [Playwright Documentation Site – Automation Tests (POM Example)](#playwright-documentation-site--automation-tests-pom-example)
- [Test Scenarios Implemented](#test-scenarios-implemented)
- [Page Object Model Implementation](#page-object-model-implementation)
- [Automation Concepts Demonstrated](#automation-concepts-demonstrated)
- [Skills Demonstrated](#skills-demonstrated)

### Network Interception & Request Handling

- [Network Interception and Request/Response Handling with Playwright](#network-interception-and-requestresponse-handling-with-playwright)
- [Capturing Network Requests](#capturing-network-requests)
- [Capturing Network Responses](#capturing-network-responses)
- [Route Handlers for Network Interception](#route-handlers-for-network-interception)
- [Blocking Resource Requests](#blocking-resource-requests)
- [Modifying Request Headers](#modifying-request-headers)
- [Mocking API Responses](#mocking-api-responses)
- [Redirecting Network Requests](#redirecting-network-requests)
- [Example Test: Network Interception](#example-test-network-interception)
- [Key Playwright Networking Concepts](#key-playwright-networking-concepts)

### Response and Request Modification

- [Modifying HTTP Responses with Playwright](#modifying-http-responses-with-playwright)
- [Steps to Modify a Response](#steps-to-modify-a-response)
- [Example: Modifying an HTML Heading](#example-modifying-an-html-heading)
- [Explanation of Key Methods](#explanation-of-key-methods)
- [Request Flow When Modifying Responses](#request-flow-when-modifying-responses)
- [Benefits of Response Modification](#benefits-of-response-modification)

### POST Request Interception

- [Modifying POST Request Data with Playwright](#modifying-post-request-data-with-playwright)
- [Accessing POST Request Data](#accessing-post-request-data)
- [Modifying JSON POST Data](#modifying-json-post-data)
- [Request Flow When Modifying POST Data](#request-flow-when-modifying-post-data)
- [Key Methods and Properties](#key-methods-and-properties)
- [Why Modify POST Requests?](#why-modify-post-requests)

### Advanced Networking Concepts

- [Understanding route.fetch() vs route.fulfill()](#understanding-routefetch-vs-routefulfill)

### API Testing with Playwright

- [API Testing with Playwright (APIRequestContext)](#api-testing-with-playwright-apirequestcontext)
- [Creating an API Request Context](#creating-an-api-request-context)
- [Example API Test](#example-api-test)
- [Validating API Responses](#validating-api-responses)
- [Why Combine API and UI Testing?](#why-combine-api-and-ui-testing)

### API Validation and Search Testing

- [Basic API Validation Using Playwright](#basic-api-validation-using-playwright)
- [Example Test: Validate API Response Data](#example-test-validate-api-response-data)
- [API Testing Using Playwright APIRequestContext](#api-testing-using-playwright-apirequestcontext)
- [API Search Testing Using Playwright and Pytest Fixtures](#api-search-testing-using-playwright-and-pytest-fixtures)
- [Creating a Reusable API Fixture](#creating-a-reusable-api-fixture)
- [Example Test: Search Users API](#example-test-search-users-api)
- [Why Test Search APIs?](#why-test-search-apis)
---
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
# Python Type Hinting Guide

This document provides a detailed overview of **Type Hinting (Type Annotations) in Python**.  
Type hints improve **code readability, maintainability, and static analysis** by allowing developers to explicitly specify expected data types.

Type hinting is especially useful when working in large projects or collaborative environments, as it helps developers understand how variables and functions are intended to be used.

---

# What is Type Hinting?

Type hinting allows developers to annotate variables, function parameters, and return types with expected data types.

Example:

```python
num: int = 10
```

This tells readers and tools that `num` is expected to be an integer.

Static type checking tools such as **mypy** can analyze these hints and detect potential bugs before runtime.

---

# 1. Variable Type Hinting

You can specify the type of a variable directly when declaring it.

```python
age: int = 25
name: str = "Alice"
height: float = 5.9
is_active: bool = True
```

### Why use it?

- Improves readability
- Helps IDE autocompletion
- Enables static type checking

---

# 2. Function Parameter Type Hinting

You can annotate the expected types of function parameters.

```python
def greet(name: str, age: int):
    print(f"{name} is {age} years old")
```

Here:

- `name` must be a `str`
- `age` must be an `int`

---

# 3. Function Return Type Hinting

You can also specify the type a function returns using `->`.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Another example:

```python
def get_username() -> str:
    return "admin"
```

---

# 4. Optional Types

Sometimes a value can be `None`.

Use `Optional` from the typing module.

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    return None
```

Equivalent syntax (Python 3.10+):

```python
def find_user(user_id: int) -> str | None:
    return None
```

---

# 5. List Type Hinting

Lists can contain specific element types.

Old syntax:

```python
from typing import List

numbers: List[int] = [1, 2, 3]
```

Modern Python (3.9+):

```python
numbers: list[int] = [1, 2, 3]
```

---

# 6. Dictionary Type Hinting

Dictionaries specify key and value types.

```python
data: dict[str, int] = {"a": 1, "b": 2}
```

Old syntax:

```python
from typing import Dict

data: Dict[str, int]
```

---

# 7. Tuple Type Hinting

Tuples can contain fixed types.

```python
point: tuple[int, int] = (10, 20)
```

Variable length tuple:

```python
values: tuple[int, ...] = (1, 2, 3, 4)
```

---

# 8. Set Type Hinting

```python
unique_ids: set[int] = {1, 2, 3}
```

---

# 9. Union Types

A variable can accept multiple types.

Old syntax:

```python
from typing import Union

value: Union[int, str]
```

Modern syntax:

```python
value: int | str
```

---

# 10. Any Type

When a variable can be anything.

```python
from typing import Any

data: Any = "hello"
```

---

# 11. Callable Type

Used when passing functions as parameters.

```python
from typing import Callable

def process(func: Callable[[int, int], int]) -> int:
    return func(2, 3)
```

Meaning:

```
Callable[[param_types], return_type]
```

---

# 12. Custom Types with TypeAlias

```python
from typing import TypeAlias

UserId: TypeAlias = int

user_id: UserId = 100
```

---

# 13. TypedDict (Typed Dictionaries)

Used when dictionaries have fixed structure.

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
```

Usage:

```python
user: User = {"name": "Alice", "age": 30}
```

---

# 14. Dataclasses with Type Hints

Type hints work very well with dataclasses.

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
```

---

# 15. Generic Types

Generic types allow reusable type structures.

```python
from typing import TypeVar

T = TypeVar("T")

def get_first(items: list[T]) -> T:
    return items[0]
```

---

# 16. Class Attribute Type Hinting

```python
class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
```

---

# 17. Literal Types

Restrict values to specific constants.

```python
from typing import Literal

status: Literal["success", "error"]
```

---

# 18. Final (Constant Values)

```python
from typing import Final

MAX_USERS: Final = 100
```

---

# Benefits of Type Hinting

- Better IDE support
- Early error detection
- Improved documentation
- Better collaboration
- Safer refactoring

---

# Example Code

Below is a simple example demonstrating **variable type hinting**.

```python
num: int = 100
lst: list[int] = [1, 2, 3, 4]
dt: dict[str, int] = {"key": 0}

print(num)
print(lst)
print(dt)
```

---

# Python Version

Recommended:

```
Python 3.9+
```

Modern Python versions support the simplified syntax:

```
list[int]
dict[str, int]
int | str
```

---

# Pytest JSON Test Report Generator

This project demonstrates how to generate and validate a **JSON test report using Python and Pytest**.

The implementation shows several important Python testing techniques including:

- JSON report generation
- File handling
- Modular design
- Pytest fixtures
- Automated validation of report structure
- Reusable test data
- Documentation of test workflow

This example simulates a simple **test reporting system** that creates a JSON file and verifies its structure using automated tests.

---

# Project Structure

```
project/
│
├── report.py
├── test_report.py
├── report.json
└── README.md
```

| File | Description |
|-----|-------------|
| `report.py` | Generates the JSON test report |
| `test_report.py` | Pytest test suite validating the report |
| `report.json` | Generated output report |
| `README.md` | Documentation |

---

# report.py – Report Generator

This module generates a JSON test report containing metadata about test execution.

## Code

```python
import json
from datetime import datetime


def generate_report():
    """
    Generate a JSON test report.

    This function creates a dictionary containing:
    - timestamp : the time when the report was generated
    - status    : test result (pass/fail)
    - summary   : test identifier in the format module.py::test_case

    The report is saved as 'report.json'.
    """

    # Create report data
    report_data = {
        "timestamp": datetime.now().isoformat(),
        "status": "pass",
        "summary": "module.py::test_case"
    }

    # Write the report data to a JSON file
    with open("report.json", "w") as file:
        json.dump(report_data, file, indent=4)

    print("Report successfully generated: report.json")
```

---

# Techniques Used in report.py

## 1. JSON Serialization

The project uses Python's built-in **json module** to convert Python dictionaries into JSON format.

```
json.dump()
```

Purpose:

- Converts Python objects → JSON
- Stores structured data in a file

Example:

```python
json.dump(report_data, file, indent=4)
```

The `indent=4` parameter improves readability.

Example output:

```json
{
    "timestamp": "2026-03-07T18:45:10.123456",
    "status": "pass",
    "summary": "module.py::test_case"
}
```

---

## 2. Datetime Handling

The report includes the exact time the report was generated.

```
datetime.now().isoformat()
```

This produces a **standard ISO 8601 timestamp**, which is commonly used in APIs and logging systems.

Example:

```
2026-03-07T18:45:10.123456
```

---

## 3. File Handling

The project uses Python’s context manager (`with` statement) to safely write files.

```python
with open("report.json", "w") as file:
```

Benefits:

- Automatically closes the file
- Prevents memory leaks
- Ensures safe file writing

---

# test_report.py – Automated Tests

This module uses **Pytest** to verify the generated JSON report.

## Code

```python
import json
import Pytest.report as report
import pytest


@pytest.fixture
def report_json():
    """
    Pytest fixture that generates the report and loads the JSON content.

    Steps performed:
    1. Calls the report generator function.
    2. Opens the generated report.json file.
    3. Loads the JSON content into a Python dictionary.
    4. Returns the dictionary so it can be reused by multiple tests.
    """

    # Generate the report file
    report.generate_report()

    # Load and return the JSON report data
    with open("report.json") as file:
        return json.load(file)


def test_report_json(report_json):
    """
    Test that the generated report JSON is a dictionary.

    This ensures the report structure is valid
    and correctly parsed from the JSON file.
    """

    # Verify the report structure
    assert isinstance(report_json, dict)


def test_report_fields(report_json):
    """
    Test that the generated report contains all required fields.

    Required fields:
    - timestamp : when the report was generated
    - status    : pass/fail result of the test
    - summary   : identifier of the executed test
    """

    # Verify required fields exist in the report
    assert "timestamp" in report_json
    assert "status" in report_json
    assert "summary" in report_json
```

---

# Techniques Used in test_report.py

## 1. Pytest Framework

Pytest is a powerful testing framework for Python.

Benefits:

- Simple syntax
- Automatic test discovery
- Powerful fixtures
- Rich plugin ecosystem

Tests are automatically detected when they follow this naming pattern:

```
test_*.py
```

---

# 2. Pytest Fixtures

The project uses a **fixture** to generate and load the JSON report.

```
@pytest.fixture
```

Purpose:

- Provide reusable test data
- Avoid repeating setup logic
- Improve test maintainability

Example:

```python
@pytest.fixture
def report_json():
```

This fixture:

1. Generates the report
2. Reads the JSON file
3. Returns a Python dictionary

All tests can reuse this data.

---

# 3. JSON Deserialization

The report file is loaded into Python using:

```
json.load()
```

Example:

```python
with open("report.json") as file:
    return json.load(file)
```

This converts JSON → Python dictionary.

---

# 4. Assertions

Assertions verify expected conditions.

Example:

```python
assert isinstance(report_json, dict)
```

This ensures:

- JSON was parsed successfully
- The report structure is valid

---

# 5. Field Validation

The test ensures the report contains required keys.

```python
assert "timestamp" in report_json
assert "status" in report_json
assert "summary" in report_json
```

This verifies the **report schema**.

---

# Testing Strategy

The testing process follows these steps:

```
Test Start
     │
     ▼
Fixture Generates Report
     │
     ▼
JSON File Created
     │
     ▼
JSON Loaded into Dictionary
     │
     ▼
Tests Validate Structure
     │
     ▼
Tests Validate Required Fields
     │
     ▼
Test Pass / Fail
```

---

# Running the Tests

Install pytest:

```
pip install pytest
```

Run tests:

```
pytest -v
```

Example output:

```
test_report.py::test_report_json PASSED
test_report.py::test_report_fields PASSED
```

---

# Example Generated Report

```
report.json
```

```json
{
    "timestamp": "2026-03-07T18:45:10.123456",
    "status": "pass",
    "summary": "module.py::test_case"
}
```

---

# Key Skills Demonstrated

This project demonstrates the following engineering skills:

- Python scripting
- JSON data processing
- Automated testing with Pytest
- Test fixtures
- File handling
- Structured test reporting
- Clean code documentation
- Modular software design

---

# Possible Future Improvements

Potential enhancements include:

- Dynamic test status detection
- Multiple test case reporting
- HTML report generation
- Integration with CI/CD pipelines
- Logging support
- Error handling for missing files

---

---

# Writing Tests with Pytest

Pytest is a popular Python testing framework used to write **simple, scalable, and maintainable automated tests**. It allows developers to verify that code behaves as expected.

Pytest automatically discovers and runs tests without requiring complex configuration.

---

# Pytest File Naming Convention

Pytest discovers tests based on **specific naming patterns**.

Test files must follow one of these formats:

```
test_*.py
*_test.py
```

Examples:

```
test_report.py
test_api.py
login_test.py
calculator_test.py
```

Recommended format:

```
test_<module_name>.py
```

Example:

```
report.py
test_report.py
```

This makes it easy to identify which test file corresponds to which module.

---

# Test Function Naming Convention

Each test function must begin with the prefix:

```
test_
```

Example:

```python
def test_addition():
    pass
```

This allows Pytest to automatically detect and execute the test.

---

# Basic Structure of a Pytest Test

A typical Pytest test includes three parts:

1. **Setup** – Prepare test data
2. **Execution** – Run the function being tested
3. **Assertion** – Verify the result

Example:

```python
def test_addition():
    result = 2 + 2
    assert result == 4
```

---

# Example Pytest Test File

Below is a simple example demonstrating how to test a Python function.

## calculator.py

```python
def add(a, b):
    return a + b
```

## test_calculator.py

```python
import calculator

def test_add():
    result = calculator.add(2, 3)
    assert result == 5


def test_add_negative_numbers():
    result = calculator.add(-2, -3)
    assert result == -5
```

---

# Using Fixtures in Pytest

Fixtures are reusable setup functions that prepare test data.

Example:

```python
import pytest

@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 30}


def test_sample_data(sample_data):
    assert sample_data["name"] == "Alice"
```

Benefits of fixtures:

- Reusable test setup
- Cleaner test code
- Reduced duplication

---

# Running Pytest

Install pytest if not already installed:

```
pip install pytest
```

Run tests in the project directory:

```
pytest
```

Verbose mode:

```
pytest -v
```

Example output:

```
test_report.py::test_report_json PASSED
test_report.py::test_report_fields PASSED
```

---

# Pytest Best Practices

Follow these guidelines when writing tests:

- Use clear test names
- Write small focused tests
- Avoid complex logic inside tests
- Use fixtures for reusable setup
- Keep tests independent
- Maintain consistent naming conventions

---

# Summary

When writing Pytest tests:

| Component | Convention |
|--------|--------|
| Test file | `test_*.py` |
| Test function | `test_*` |
| Fixtures | `@pytest.fixture` |
| Assertions | `assert` statements |

By following these conventions, Pytest can automatically discover and execute tests efficiently.
---

# Playwright Testing with Pytest (`pytest-playwright`)

Playwright provides an official Pytest plugin called **pytest-playwright** that integrates Playwright browser automation with the Pytest testing framework.

This plugin automatically provides useful fixtures such as:

- `page`
- `browser`
- `context`

These fixtures allow you to write browser tests without manually launching the browser.

---

# Installing the Playwright Pytest Plugin

Install the plugin using pip:

```bash
pip install pytest-playwright
```

Example installation output:

```
Successfully installed pytest-playwright-0.7.2
pytest-base-url-2.1.0
python-slugify-8.0.4
requests-2.32.5
```

After installation, Pytest automatically detects the plugin.

---

# Example Test: `test_app.py`

This test verifies that the **"GET STARTED"** link on the Playwright Python documentation page navigates to the correct URL.

```python
from playwright.sync_api import Page

def test_page_has_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="GET STARTED")

    link.click()

    assert page.url == "https://playwright.dev/python/docs/intro"
```

---

# Explanation of the Test

### Page Fixture

```python
page: Page
```

The `page` fixture is provided automatically by **pytest-playwright**.

It creates:

```
Browser
   ↓
Browser Context
   ↓
Page (Tab)
```

So the test can directly interact with a browser page.

---

### Navigate to Website

```python
page.goto("https://playwright.dev/python")
```

This opens the Playwright Python documentation website.

---

### Locate the Link

```python
link = page.get_by_role("link", name="GET STARTED")
```

Playwright uses **role-based locators** for reliable element selection.

Role-based locators are recommended because they use **accessibility attributes (ARIA)**.

---

### Click the Link

```python
link.click()
```

This simulates a user clicking the **GET STARTED** link.

---

### Verify Navigation

```python
assert page.url == "https://playwright.dev/python/docs/intro"
```

The assertion verifies that clicking the link navigates to the correct documentation page.

---

# Running the Test

Run the test using Pytest:

```bash
pytest test_app.py
```

Example output:

```
================================================= test session starts ==================================================
platform darwin -- Python 3.11.3
plugins: playwright-0.7.2
collected 1 item

test_app.py .                                                           [100%]

================================================== 1 passed ===================================================
```

---

# Running Tests in Headed Mode

By default, Playwright runs browsers in **headless mode**.

To see the browser UI:

```bash
pytest test_app.py --headed
```

Example output:

```
collected 1 item

test_app.py .                                                           [100%]
```

Now the browser window will appear while the test runs.

---

# Running Tests in Different Browsers

Playwright supports multiple browsers.

You can run the same test in:

- Chromium
- Firefox
- WebKit

Example:

```bash
pytest test_app.py --headed --browser=firefox
```

---

# Running Tests with Slow Motion

To visually observe browser actions, use **slow motion mode**.

```bash
pytest test_app.py --headed --browser=firefox --slowmo=500
```

This slows down actions by **500 milliseconds**.

---

# Example Terminal Session

Example workflow from the terminal:

```bash
pytest test_app.py
```

```
1 passed in 9.94s
```

Run in headed mode:

```bash
pytest test_app.py --headed
```

```
1 passed in 30.99s
```

Run with Firefox and slow motion:

```bash
pytest test_app.py --headed --browser=firefox --slowmo=500
```

```
1 passed
```

---

# Troubleshooting: "No Tests Ran"

If you see the error:

```
collected 0 items
ERROR: file or directory not found
```

Possible causes:

### 1. Running Pytest from the Wrong Directory

Ensure you are inside the project folder.

Check current directory:

```bash
pwd
```

Navigate to the project folder:

```bash
cd playwright-python-project
```

---

### 2. Test File Does Not Exist

Verify that the file exists:

```bash
ls
```

Expected output:

```
test_app.py
```

---

### 3. Incorrect Test Naming

Pytest only detects tests that follow these patterns:

```
test_*.py
*_test.py
```

Example valid names:

```
test_app.py
test_login.py
api_test.py
```

---

### 4. Test Function Naming

Functions must start with:

```
test_
```

Example:

```python
def test_page_has_get_started_link():
```

---

# Recommended Project Structure

```
playwright-python-project
│
├── tests
│   └── test_app.py
│
├── playwright
│
├── venv
│
└── README.md
```

---

# Key Skills Demonstrated

This example demonstrates several important automation testing concepts:

- Playwright browser automation
- Pytest test framework
- Role-based element locators
- Page navigation testing
- Cross-browser testing
- Headless vs headed execution
- Debugging Playwright tests

---

# Key Takeaways

✔ `pytest-playwright` integrates Playwright with Pytest  
✔ The `page` fixture automatically creates a browser page  
✔ Tests can run in multiple browsers  
✔ `--headed` shows the browser UI  
✔ `--slowmo` slows down automation for debugging  
✔ Pytest automatically discovers tests based on naming conventions

---
---

# Using `pytest.ini` to Configure Playwright Test Options

Instead of typing Playwright options every time you run tests, you can define **default test settings** using a `pytest.ini` configuration file.

This allows Pytest to automatically apply browser options whenever tests run.

---

# Example `pytest.ini`

Create a file called:

```
pytest.ini
```

Add the following configuration:

```ini
[pytest]
addopts = --headed --slowmo=500 --browser=firefox
```

---

# What This Configuration Does

This configuration tells Pytest to automatically run Playwright tests with:

| Option | Description |
|------|-------------|
| `--headed` | Runs the browser with UI instead of headless mode |
| `--slowmo=500` | Slows down each browser action by **500 ms** |
| `--browser=firefox` | Runs tests using the **Firefox browser** |

---

# Running Tests with Configuration

Once `pytest.ini` is configured, you can simply run:

```bash
pytest
```

Pytest will automatically apply the defined options.

Example output:

```
platform darwin -- Python 3.11
plugins: playwright-0.7.2
collected 1 item

test_app.py .                                                  [100%]

1 passed
```

The browser will open automatically because of the `--headed` option.

---

# Benefits of Using `pytest.ini`

Using a configuration file improves test workflows by:

✔ Avoiding repetitive command-line arguments  
✔ Standardizing test execution settings  
✔ Simplifying CI/CD integration  
✔ Making tests easier to run for other developers  

---

# Example Project Structure

```
playwright-python-project
│
├── pytest.ini
├── test_app.py
├── venv
└── README.md
```

---

# Overriding `pytest.ini` Options

Command-line options can override `pytest.ini` settings.

Example:

Run tests in Chromium instead of Firefox:

```bash
pytest --browser=chromium
```

Run tests in headless mode:

```bash
pytest --headless
```

---

# Key Takeaways

✔ `pytest.ini` defines **default Pytest configuration**  
✔ `addopts` automatically applies Playwright options  
✔ Makes test execution **simpler and consistent**  
✔ Command-line options can override these defaults

---
---

# Test Hooks and Fixtures in Pytest (Playwright)

When writing automated tests, we often need to perform **setup and teardown operations** before and after each test.

Examples:

- Opening a browser page
- Navigating to a website
- Cleaning up resources
- Closing the browser

Pytest provides **fixtures** that act as **test hooks** to manage these operations automatically.

Fixtures help avoid repeating setup logic across multiple tests.

---

# Example Code

```python
from playwright.sync_api import Page
import pytest

@pytest.fixture(autouse=True, scope="function")
def visit_playwright(page: Page):
    page.goto("https://playwright.dev/python")
    yield page
    page.close()
    print("\n[ Fixture ]: page closed!")

def test_page_has_docs_link(page: Page):
    link = page.get_by_role("link", name="Docs")
    assert link.is_visible()

def test_page_has_get_started_link(page: Page):
    link = page.get_by_role("link", name="GET STARTED")
    link.click()
    assert page.url == "https://playwright.dev/python/docs/intro"
```

---

# Understanding the Test Hook (Fixture)

The fixture defined here acts as a **setup and teardown hook**.

```python
@pytest.fixture(autouse=True, scope="function")
def visit_playwright(page: Page):
```

### autouse=True

This means the fixture runs **automatically for every test function**.

Without `autouse`, tests would need to explicitly request the fixture.

Example without autouse:

```python
def test_example(visit_playwright):
```

With `autouse=True`, the fixture is applied automatically.

---

### scope="function"

This means the fixture runs **once for every test function**.

Available fixture scopes:

| Scope | Description |
|------|-------------|
| function | Runs once per test |
| class | Runs once per test class |
| module | Runs once per file |
| session | Runs once for entire test session |

In this example:

```
Test 1
   ↓
Fixture setup
   ↓
Run test
   ↓
Fixture teardown

Test 2
   ↓
Fixture setup
   ↓
Run test
   ↓
Fixture teardown
```

---

# Setup Phase (Before Test)

The setup logic runs **before the test executes**.

```python
page.goto("https://playwright.dev/python")
```

This ensures every test starts on the **Playwright Python homepage**.

---

# Yield Statement

```python
yield page
```

`yield` splits the fixture into two parts:

```
Setup code
↓
yield
↓
Test runs
↓
Teardown code
```

Everything **before yield** runs before the test.

Everything **after yield** runs after the test.

---

# Teardown Phase (After Test)

After the test finishes, the fixture executes the teardown logic.

```python
page.close()
print("\n[ Fixture ]: page closed!")
```

This ensures:

- The page is properly closed
- Resources are cleaned up
- Debug information is printed

Example console output:

```
[ Fixture ]: page closed!
```

---

# Test 1: Verify Docs Link

```python
def test_page_has_docs_link(page: Page):
```

This test verifies that the **Docs link exists on the page**.

```python
link = page.get_by_role("link", name="Docs")
assert link.is_visible()
```

Steps performed:

1. Locate the **Docs** link
2. Check if it is visible
3. Pass the test if the link is present

---

# Test 2: Verify GET STARTED Navigation

```python
def test_page_has_get_started_link(page: Page):
```

This test verifies that clicking **GET STARTED** navigates to the correct page.

Steps performed:

```python
link = page.get_by_role("link", name="GET STARTED")
```

Locate the link.

```
link.click()
```

Click the link.

```
assert page.url == "https://playwright.dev/python/docs/intro"
```

Verify navigation succeeded.

---

# Test Execution Flow

The test execution lifecycle looks like this:

```
Test Session Start
       ↓
Fixture Setup
       ↓
Navigate to Playwright Website
       ↓
Run Test
       ↓
Fixture Teardown
       ↓
Close Page
       ↓
Next Test
```

---

# Running the Tests

Run the tests using:

```bash
pytest
```

Example output:

```
test_hooks.py::test_page_has_docs_link PASSED
test_hooks.py::test_page_has_get_started_link PASSED
```

Example with fixture output:

```
test_hooks.py::test_page_has_docs_link PASSED
[ Fixture ]: page closed!

test_hooks.py::test_page_has_get_started_link PASSED
[ Fixture ]: page closed!
```

---

# Why Fixtures Are Important

Fixtures help create **clean and maintainable test automation frameworks**.

Benefits:

✔ Avoid duplicated setup code  
✔ Automatically manage browser lifecycle  
✔ Ensure tests run in a predictable environment  
✔ Simplify test structure  

---

# Key Takeaways

✔ Pytest fixtures act as **test hooks**  
✔ `autouse=True` automatically applies fixtures to all tests  
✔ `scope="function"` runs fixture per test  
✔ `yield` separates setup and teardown logic  
✔ Fixtures improve test maintainability and reliability

---
---

# Taking Screenshots with Playwright

Screenshots are extremely useful in automation testing. They help capture the **state of the application during test execution** and are commonly used for:

- Debugging test failures
- Visual verification
- Test reporting
- Documentation
- Capturing UI changes

Playwright provides several ways to take screenshots, including:

- Page screenshots
- Element screenshots
- Clipped screenshots (specific screen areas)
- Full-page screenshots

---

# Example Test: Navigation and Screenshots

```python
from playwright.sync_api import Page

# Constants
BASE_URL = "https://playwright.dev/python"
DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_navigation_and_screenshots(page: Page):
    """
    Test navigation to the Playwright documentation page and demonstrate
    multiple ways of taking screenshots using Playwright.

    This test performs the following steps:
    1. Opens the Playwright Python homepage.
    2. Takes a screenshot of the visible viewport.
    3. Captures screenshots of specific elements.
    4. Navigates using the "GET STARTED" link.
    5. Captures a full-page screenshot of the documentation page.
    6. Verifies the navigation URL.
    """

    # Navigate to Playwright Python homepage
    page.goto(BASE_URL)

    # Screenshot Method 1: Capture visible page viewport
    page.screenshot(path="screenshots/homepage_viewport.png")

    # Locate "GET STARTED" link
    get_started_link = page.get_by_role("link", name="GET STARTED")

    # Screenshot Method 2: Capture specific element
    get_started_link.screenshot(path="screenshots/get_started_element.png")

    # Locate "Docs" navigation link
    docs_link = page.get_by_role("link", name="Docs")

    # Screenshot Method 3: Capture another element
    docs_link.screenshot(path="screenshots/docs_link.png")

    # Screenshot Method 4: Highlight area by bounding box screenshot
    box = docs_link.bounding_box()
    if box:
        page.screenshot(
            path="screenshots/docs_link_area.png",
            clip={
                "x": box["x"],
                "y": box["y"],
                "width": box["width"],
                "height": box["height"],
            },
        )

    # Click "GET STARTED" link
    get_started_link.click()

    # Screenshot Method 5: Capture full page screenshot
    page.screenshot(
        path="screenshots/docs_full_page.png",
        full_page=True
    )

    # Verify navigation
    assert page.url == DOCS_URL
```

---

# Screenshot Techniques Demonstrated

This test demonstrates **five different screenshot techniques**.

---

# 1. Viewport Screenshot

```python
page.screenshot(path="screenshots/homepage_viewport.png")
```

This captures **only the visible portion of the page** (the browser viewport).

Example output:

```
screenshots/homepage_viewport.png
```

This is useful for:

- UI verification
- Documentation screenshots
- Capturing current page state

---

# 2. Element Screenshot

Playwright allows taking screenshots of **specific elements**.

```python
get_started_link.screenshot(
    path="screenshots/get_started_element.png"
)
```

This captures **only the selected element**.

Example output:

```
screenshots/get_started_element.png
```

Advantages:

- Focused screenshots
- Cleaner debugging
- Useful for visual testing

---

# 3. Screenshot of Another Element

```python
docs_link.screenshot(
    path="screenshots/docs_link.png"
)
```

This captures the **Docs navigation link**.

Playwright automatically crops the screenshot to the element.

---

# 4. Bounding Box Screenshot (Clipped Area)

Sometimes you want to capture a **specific region of the page**.

This can be done using the element's bounding box.

```python
box = docs_link.bounding_box()
```

The bounding box returns:

```
{
    x: position from left
    y: position from top
    width: element width
    height: element height
}
```

Then we capture only that area:

```python
page.screenshot(
    path="screenshots/docs_link_area.png",
    clip={
        "x": box["x"],
        "y": box["y"],
        "width": box["width"],
        "height": box["height"],
    }
)
```

This allows capturing **custom regions of the page**.

---

# 5. Full Page Screenshot

```python
page.screenshot(
    path="screenshots/docs_full_page.png",
    full_page=True
)
```

This captures the **entire webpage**, including parts not visible in the viewport.

Example output:

```
screenshots/docs_full_page.png
```

Full-page screenshots are useful for:

- Visual regression testing
- Documentation
- Debugging layout issues

---

# Screenshot Output Structure

The screenshots are saved in the following folder:

```
project/
│
├── screenshots/
│   ├── homepage_viewport.png
│   ├── get_started_element.png
│   ├── docs_link.png
│   ├── docs_link_area.png
│   └── docs_full_page.png
│
├── test_screenshots.py
└── README.md
```

---

# Running the Test

Run the test using:

```bash
pytest test_screenshots.py
```

Example output:

```
collected 1 item

test_screenshots.py .                                              [100%]

1 passed
```

---

# Best Practices for Screenshots

When working with screenshots in automation:

✔ Store screenshots in a **separate directory**  
✔ Use **descriptive filenames**  
✔ Capture screenshots **on test failures**  
✔ Use element screenshots for **focused debugging**  

---

# Common Screenshot Options

| Option | Description |
|------|-------------|
| `path` | File path for screenshot |
| `full_page=True` | Capture entire webpage |
| `clip={}` | Capture specific screen area |
| `type="jpeg"` | Change image format |
| `quality=80` | Control JPEG quality |

Example:

```python
page.screenshot(path="image.jpg", type="jpeg", quality=80)
```

---

# Key Takeaways

✔ Playwright supports **multiple screenshot methods**  
✔ Screenshots can capture **entire pages or specific elements**  
✔ `full_page=True` captures the full webpage  
✔ `clip` allows capturing custom regions  
✔ Screenshots are essential for **debugging and visual testing**

---
---

# Recording Test Videos with Playwright

Playwright provides built-in support for **recording videos during test execution**.  
Video recording is extremely useful for debugging automation failures and reviewing browser behavior.

Recorded videos capture everything that happens during the test, including:

- Page navigation
- Element interactions
- Clicks and typing
- UI changes

This feature is commonly used in **CI/CD pipelines and automated testing frameworks**.

---

# Example Test with Video Recording

```python
from playwright.sync_api import Browser, Page
import pytest

# Constants
BASE_URL = "https://playwright.dev/python"
DOCS_URL = "https://playwright.dev/python/docs/intro"


@pytest.fixture()
def record_video(browser: Browser):
    context = browser.new_context(
        record_video_dir="video/"
    )

    page = context.new_page()

    yield page

    context.close()


def test_page_navigation_and_screenshots(record_video: Page):

    # Navigate to Playwright Python homepage
    record_video.goto(BASE_URL)

    # Toggle dark mode
    dark_mode_toggle_btn = record_video.locator("button.toggleButton_gllP")
    dark_mode_toggle_btn.click()

    # Locate navigation links
    get_started_link = record_video.get_by_role("link", name="GET STARTED")
    docs_link = record_video.get_by_role("link", name="Docs")

    # Click "GET STARTED"
    get_started_link.click()

    # Verify navigation
    assert record_video.url == DOCS_URL
```

---

# How Video Recording Works

Playwright records videos at the **browser context level**.

```python
context = browser.new_context(
    record_video_dir="video/"
)
```

This tells Playwright to:

```
Start recording video
↓
Save recording into "video/" folder
↓
Stop recording when the context closes
```

The video is automatically saved when:

```
context.close()
```

is executed.

---

# Fixture Explanation

The fixture used in this test automatically manages the browser page and video recording.

```python
@pytest.fixture()
def record_video(browser: Browser):
```

This fixture performs:

### Setup

```
Create browser context
Enable video recording
Open new page
```

### Test Execution

```
Test runs using the page object
```

### Teardown

```
Close browser context
Save video file
```

Using fixtures keeps tests **clean and reusable**.

---

# Video Output Directory

Recorded videos are saved inside the following folder:

```
project/
│
├── video/
│   └── test_page_navigation_and_screenshots.webm
│
├── test_video_recording.py
└── README.md
```

Playwright records videos in the **WebM format**.

Example file:

```
video/test_page_navigation_and_screenshots.webm
```

---

# Running the Test

Run the test normally with Pytest:

```bash
pytest test_video_recording.py
```

Example output:

```
collected 1 item

test_video_recording.py .                                    [100%]

1 passed
```

After execution, a video file will appear in the `video` directory.

---

# Why Video Recording Is Useful

Video recording helps when:

- Debugging failed tests
- Reviewing UI behavior
- Investigating flaky tests
- Monitoring test execution in CI pipelines

Instead of guessing what happened during a test, you can **watch the recorded video**.

---

# Custom Video Options

Playwright also supports additional video configuration.

Example:

```python
context = browser.new_context(
    record_video_dir="video/",
    record_video_size={"width": 1280, "height": 720}
)
```

Options available:

| Option | Description |
|------|-------------|
| `record_video_dir` | Directory where videos are stored |
| `record_video_size` | Resolution of the recorded video |

---

# Best Practices

When recording videos in automated tests:

✔ Record videos only for **debugging or CI pipelines**  
✔ Store videos in a **dedicated folder**  
✔ Clean old recordings regularly  
✔ Combine with **screenshots and logs** for full debugging context  

---

# Key Takeaways

✔ Playwright can automatically record test execution videos  
✔ Videos are recorded at the **browser context level**  
✔ Recordings are saved when the context closes  
✔ Videos help debug test failures and UI issues  
✔ Useful for **automation frameworks and CI/CD environments**

---
---

# Playwright Tracing (Debugging with Trace Viewer)

Playwright provides a powerful debugging feature called **Tracing**.  
Tracing records everything that happens during test execution, including:

- Page navigation
- User interactions
- DOM snapshots
- Network requests
- Console logs
- Screenshots
- Source code

The recorded trace can later be opened in the **Playwright Trace Viewer**, which provides a complete visual timeline of the test.

Tracing is extremely useful for:

- Debugging failed tests
- Investigating flaky tests
- Understanding automation behavior
- Reviewing CI/CD test runs

---

# Example Test with Playwright Tracing

```python
from playwright.sync_api import BrowserContext, Page
import pytest

# Constants
BASE_URL = "https://playwright.dev/python"
DOCS_URL = "https://playwright.dev/python/docs/intro"


@pytest.fixture(autouse=True)
def trace_test(context: BrowserContext):

    context.tracing.start(
        name="playwright",
        screenshots=True,
        snapshots=True,
        sources=True,
    )

    yield

    context.tracing.stop(path="traces/trace.zip")


def test_page_navigation_and_screenshots(page: Page):

    # Navigate to Playwright homepage
    page.goto(BASE_URL)

    # Locate navigation links
    get_started_link = page.get_by_role("link", name="GET STARTED")
    docs_link = page.get_by_role("link", name="Docs")

    # Click "GET STARTED"
    get_started_link.click()

    # Verify navigation
    assert page.url == DOCS_URL
```

---

# How Playwright Tracing Works

Tracing records the entire test execution timeline.

```
Test starts
↓
Tracing begins
↓
Browser actions recorded
↓
Screenshots captured
↓
DOM snapshots saved
↓
Trace file generated
```

At the end of the test, the trace file is saved as:

```
traces/trace.zip
```

---

# Tracing Configuration

Tracing is started using:

```python
context.tracing.start()
```

Configuration options used in this example:

```python
context.tracing.start(
    name="playwright",
    screenshots=True,
    snapshots=True,
    sources=True
)
```

---

# Trace Options Explained

| Option | Description |
|------|-------------|
| `screenshots=True` | Captures screenshots during test execution |
| `snapshots=True` | Records DOM snapshots for each action |
| `sources=True` | Includes test source code in the trace |

These options allow the trace viewer to reconstruct the **entire test state at every step**.

---

# Stopping the Trace

Tracing must be stopped to generate the trace file.

```python
context.tracing.stop(path="traces/trace.zip")
```

This saves the trace archive to:

```
traces/trace.zip
```

---

# Fixture Explanation

The tracing fixture runs automatically for every test.

```python
@pytest.fixture(autouse=True)
```

This ensures tracing is enabled without modifying individual tests.

### Setup Phase

```
Start tracing
```

### Test Execution

```
Run test normally
```

### Teardown Phase

```
Stop tracing
Save trace file
```

This pattern ensures **all tests are recorded automatically**.

---

# Project Folder Structure

```
project/
│
├── traces/
│   └── trace.zip
│
├── test_tracing.py
└── README.md
```

---

# Running the Test

Run the test normally using Pytest:

```bash
pytest
```

Example output:

```
collected 1 item

test_tracing.py .                                              [100%]

1 passed
```

After execution, the trace file will appear in:

```
traces/trace.zip
```

---

# Viewing the Trace

Playwright provides a built-in **Trace Viewer**.

Open the trace using:

```bash
playwright show-trace traces/trace.zip
```

This launches the interactive trace viewer in the browser.

---

# What the Trace Viewer Shows

The trace viewer provides a visual debugging interface including:

- Test timeline
- Action logs
- Screenshots
- DOM snapshots
- Network requests
- Source code

You can step through the test **action-by-action** to see exactly what happened.

---

# Why Tracing Is Powerful

Tracing provides far more debugging information than screenshots or logs alone.

Benefits include:

✔ Full test timeline visualization  
✔ Step-by-step execution replay  
✔ DOM snapshots for each action  
✔ Screenshot history  
✔ Network request inspection  

This makes Playwright tracing one of the **most powerful debugging tools in modern test automation**.

---

# Best Practices

When using tracing in automation frameworks:

✔ Enable tracing in **CI pipelines**  
✔ Store trace files for failed tests  
✔ Combine tracing with **screenshots and videos**  
✔ Clean up old traces periodically  

---

# Key Takeaways

✔ Playwright tracing records complete test execution  
✔ Traces include screenshots, DOM snapshots, and logs  
✔ Trace files are saved as `.zip` archives  
✔ `playwright show-trace` opens the interactive viewer  
✔ Tracing is one of the best tools for debugging automation tests

---
---

# Web-First Assertions in Playwright (Assertions on Page)

Playwright provides a powerful assertion system called **Web-First Assertions**.

Unlike traditional assertions that check conditions immediately, **Playwright assertions automatically wait for conditions to become true**.

This makes tests **more reliable and less flaky**, especially when dealing with dynamic web applications.

Web-first assertions are implemented using the `expect` API.

---

# Example Test: Page URL Assertion

```python
from playwright.sync_api import Page, expect

# Constants
BASE_URL = "https://playwright.dev/python"
DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_navigation_and_screenshots(page: Page):

    # Navigate to Playwright Python homepage
    page.goto(BASE_URL)

    # Locate "GET STARTED" link
    get_started_link = page.get_by_role("link", name="GET STARTED")

    # Locate "Docs" navigation link
    docs_link = page.get_by_role("link", name="Docs")

    # Click "GET STARTED" link
    get_started_link.click()

    # Verify navigation
    expect(page).to_have_url(DOCS_URL)
```

---

# What Are Web-First Assertions?

Web-first assertions automatically **wait for the expected condition** before failing.

Traditional assertion:

```python
assert page.url == DOCS_URL
```

Playwright assertion:

```python
expect(page).to_have_url(DOCS_URL)
```

Difference:

| Traditional Assertion | Playwright Web-First Assertion |
|---|---|
| Executes immediately | Automatically waits |
| Can fail if page loads slowly | Waits until condition becomes true |
| More flaky tests | More stable tests |

---

# How the Test Works

### 1. Navigate to Website

```python
page.goto(BASE_URL)
```

This opens the Playwright Python homepage.

---

### 2. Locate Page Elements

Playwright uses **role-based selectors**.

```python
get_started_link = page.get_by_role("link", name="GET STARTED")
docs_link = page.get_by_role("link", name="Docs")
```

Role-based locators are recommended because they are:

- stable
- accessible
- readable

---

### 3. Perform Interaction

```python
get_started_link.click()
```

This simulates a user clicking the **GET STARTED** link.

---

### 4. Verify Navigation with Web-First Assertion

```python
expect(page).to_have_url(DOCS_URL)
```

Playwright will:

```
Wait for the page to navigate
↓
Check the current URL
↓
Retry automatically if not yet matched
↓
Fail only after timeout
```

Default timeout is **5 seconds**.

---

# Why Web-First Assertions Are Important

Modern web applications are asynchronous.

Examples:

- AJAX requests
- dynamic content
- delayed rendering
- JavaScript frameworks (React, Angular, Vue)

Web-first assertions ensure tests wait for the correct state.

Benefits:

✔ More stable tests  
✔ Less flaky automation  
✔ Built-in waiting logic  
✔ Cleaner test code  

---

# Common Page Assertions

Playwright provides several useful page-level assertions.

| Assertion | Description |
|---|---|
| `expect(page).to_have_url()` | Verify page URL |
| `expect(page).to_have_title()` | Verify page title |
| `expect(page).to_have_title(re.compile())` | Title pattern match |

Example:

```python
expect(page).to_have_title("Playwright for Python")
```

---

# Example: Title Assertion

```python
expect(page).to_have_title("Playwright for Python")
```

This verifies that the page title matches the expected value.

---

# Timeout Behavior

Web-first assertions automatically retry until timeout.

Example:

```python
expect(page).to_have_url(DOCS_URL, timeout=10000)
```

This sets the timeout to **10 seconds**.

---

# Running the Test

Run the test using Pytest:

```bash
pytest test_assertions.py
```

Example output:

```
collected 1 item

test_assertions.py .                                      [100%]

1 passed
```

---

# Key Takeaways

✔ Playwright provides **Web-First Assertions**  
✔ Assertions automatically wait for conditions  
✔ `expect()` improves test stability  
✔ Less flaky automation tests  
✔ Recommended over traditional `assert` statements  

---
---

# Web-First Assertions on Elements (Locator Assertions)

Playwright provides **web-first assertions for elements** using the `expect()` API.

These assertions automatically **wait for the expected condition** to become true before failing. This makes tests more reliable when working with dynamic web applications.

Element assertions are typically used to verify:

- Visibility of elements
- Text content
- Attributes
- Input values
- Element state (enabled, disabled, checked)
- Element count
- CSS properties

All element assertions operate on **locators**.

---

# Example Test

```python
from playwright.sync_api import Page, expect

# Constants
BASE_URL = "https://playwright.dev/python"
DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_navigation_and_screenshots(page: Page):

    # Navigate to Playwright Python homepage
    page.goto(BASE_URL)

    # Locate elements
    get_started_link = page.get_by_role("link", name="GET STARTED")
    docs_link = page.get_by_role("link", name="Docs")

    # Element assertions
    expect(get_started_link).to_be_visible()
    expect(docs_link).to_be_visible()
```

---

# What Are Locator Assertions?

Locator assertions verify the **state or properties of elements** on a webpage.

Example:

```python
expect(locator).to_be_visible()
```

Playwright will:

```
Locate element
↓
Wait until visible
↓
Pass if visible
↓
Fail if timeout reached
```

Default timeout is **5 seconds**.

---

# Common Locator Assertions

Below are the most frequently used element assertions in Playwright.

---

# Visibility Assertions

### Element is visible

```python
expect(locator).to_be_visible()
```

Checks that the element is displayed on the page.

---

### Element is hidden

```python
expect(locator).to_be_hidden()
```

Verifies that the element is not visible.

---

# Element State Assertions

### Element is enabled

```python
expect(locator).to_be_enabled()
```

Used for buttons or inputs that should be clickable.

---

### Element is disabled

```python
expect(locator).to_be_disabled()
```

Checks that the element cannot be interacted with.

---

### Element is editable

```python
expect(locator).to_be_editable()
```

Ensures the element accepts user input.

---

### Element is checked (checkbox/radio)

```python
expect(locator).to_be_checked()
```

Verifies a checkbox or radio button is selected.

---

# Text Assertions

### Exact text match

```python
expect(locator).to_have_text("Playwright")
```

Verifies the element contains exactly the expected text.

---

### Partial text match

```python
expect(locator).to_contain_text("Playwright")
```

Verifies the text contains the expected substring.

---

### Multiple elements text

```python
expect(locator).to_have_text(["Text1", "Text2"])
```

Used when multiple elements match the locator.

---

# Attribute Assertions

Verify HTML attributes.

```python
expect(locator).to_have_attribute("href", "/docs/intro")
```

Example:

```
<a href="/docs/intro">GET STARTED</a>
```

---

# Value Assertions (Inputs)

Verify input field values.

```python
expect(locator).to_have_value("Hello")
```

Example:

```python
search_input = page.get_by_placeholder("Search")
expect(search_input).to_have_value("Playwright")
```

---

# CSS Assertions

Verify CSS styling.

```python
expect(locator).to_have_css("display", "block")
```

Example:

```python
expect(locator).to_have_css("color", "rgb(0, 0, 0)")
```

---

# Element Count Assertions

Verify number of matching elements.

```python
expect(locator).to_have_count(3)
```

Example:

```python
items = page.locator(".menu-item")
expect(items).to_have_count(5)
```

---

# Class Assertions

Verify CSS class names.

```python
expect(locator).to_have_class("active")
```

Example:

```python
expect(button).to_have_class("btn-primary")
```

---

# Focus Assertions

Verify element focus.

```python
expect(locator).to_be_focused()
```

Example:

```python
search_input.click()
expect(search_input).to_be_focused()
```

---

# Screenshot Assertion

Playwright can verify UI appearance using screenshot comparison.

```python
expect(locator).to_have_screenshot()
```

This is useful for **visual regression testing**.

---

# Timeout Customization

All assertions support custom timeouts.

Example:

```python
expect(locator).to_be_visible(timeout=10000)
```

This waits up to **10 seconds**.

---

# Running the Test

Run the test with Pytest:

```bash
pytest test_assertions.py
```

Example output:

```
collected 1 item

test_assertions.py .                         [100%]

1 passed
```

---

# Best Practices for Assertions

✔ Prefer **web-first assertions** over manual `assert`  
✔ Use **locators instead of raw selectors**  
✔ Keep assertions **simple and focused**  
✔ Verify both **UI state and behavior**  

---

# Key Takeaways

✔ Playwright provides powerful **element assertions**  
✔ Assertions automatically wait for expected conditions  
✔ Helps prevent flaky tests  
✔ Supports text, attributes, values, CSS, and visibility checks  
✔ Essential for building reliable automation frameworks

---
---

# Web-First Assertions on Element Text

In Playwright, text-based assertions allow you to verify that elements contain the expected text content.

Playwright provides powerful text assertions through the `expect()` API that automatically **wait for text to appear before failing the test**. This helps reduce flaky tests caused by dynamic content loading.

Text assertions are commonly used to verify:

- Navigation menus
- Page headings
- Dropdown options
- Button labels
- Dynamic UI messages

---

# Example Test

```python
from playwright.sync_api import Page, expect

# Constants
BASE_URL = "https://playwright.dev/python"
DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_navigation_and_screenshots(page: Page):

    # Navigate to Playwright Python homepage
    page.goto(BASE_URL)

    dropdown_menu = page.locator("ul.dropdown__menu")

    expect(dropdown_menu).to_contain_text("Python")
    expect(dropdown_menu).to_contain_text("Java")
    expect(dropdown_menu).to_contain_text("Node.js")
    expect(dropdown_menu).to_contain_text(".NET")
```

---

# What This Test Verifies

This test checks that the **language dropdown menu contains expected programming language options**.

The test verifies that the menu includes:

- Python
- Java
- Node.js
- .NET

Each assertion confirms that the specified text appears somewhere inside the dropdown element.

---

# How `to_contain_text()` Works

```python
expect(locator).to_contain_text("Python")
```

Playwright will:

```
Locate the element
↓
Wait until the text appears
↓
Verify that the element contains the text
↓
Fail only after timeout if not found
```

Default timeout: **5 seconds**

---

# Exact Text Assertion

To verify **exact text**, use `to_have_text()`.

Example:

```python
expect(locator).to_have_text("Python")
```

Difference:

| Assertion | Behavior |
|---|---|
| `to_contain_text()` | Checks if text exists anywhere inside element |
| `to_have_text()` | Checks for exact text match |

Example:

```python
expect(page.locator("h1")).to_have_text("Playwright")
```

---

# Partial Text Matching

`to_contain_text()` allows checking partial matches.

Example:

```python
expect(locator).to_contain_text("Play")
```

This will pass if the element contains:

```
Playwright
Play
Playing
```

---

# Regular Expression Text Matching

Playwright supports **regex-based text assertions**.

Example:

```python
import re

expect(locator).to_have_text(re.compile("Playwright"))
```

Example with case-insensitive match:

```python
expect(locator).to_have_text(re.compile("playwright", re.IGNORECASE))
```

---

# Assertions on Multiple Elements

If a locator matches multiple elements, Playwright can verify the text list.

Example:

```python
menu_items = page.locator("ul.dropdown__menu li")

expect(menu_items).to_have_text([
    "Python",
    "Java",
    "Node.js",
    ".NET"
])
```

This verifies the exact order of elements.

---

# Timeout Configuration

You can increase the waiting time for text assertions.

Example:

```python
expect(locator).to_contain_text("Python", timeout=10000)
```

This waits **10 seconds** before failing.

---

# Why Text Assertions Are Important

Text assertions are widely used in UI automation for verifying:

- Menu options
- Form labels
- Notifications
- Error messages
- Dynamic content

They ensure the **correct information is displayed to users**.

---

# Running the Test

Run the test with Pytest:

```bash
pytest test_text_assertions.py
```

Example output:

```
collected 1 item

test_text_assertions.py .                     [100%]

1 passed
```

---

# Best Practices

When verifying text in automation tests:

✔ Prefer `to_contain_text()` for flexible matching  
✔ Use `to_have_text()` for exact matches  
✔ Use regex for complex patterns  
✔ Keep assertions focused and readable  

---

# Key Takeaways

✔ Playwright provides powerful text assertions  
✔ Assertions automatically wait for expected text  
✔ Supports exact, partial, and regex text matching  
✔ Works for single elements and multiple elements  
✔ Helps verify UI content reliably

---
---

# Web-First Assertions on Element Attributes

Playwright allows you to verify **HTML attributes of elements** using web-first assertions.

Attributes provide important information about elements, such as:

- Links (`href`)
- Images (`src`)
- Input types (`type`)
- Accessibility labels (`aria-*`)
- CSS classes (`class`)
- Identifiers (`id`)

Playwright provides the assertion:

```
expect(locator).to_have_attribute()
```

This assertion automatically waits until the attribute value matches the expected value.

---

# Example Test

```python
from playwright.sync_api import Page, expect

# Constants
BASE_URL = "https://playwright.dev/python"
DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_navigation_and_screenshots(page: Page):

    # Navigate to Playwright Python homepage
    page.goto(BASE_URL)

    docs_link = page.get_by_role("link", name="DOCS")

    expect(docs_link).to_have_attribute(
        "href", "/python/docs/intro"
    )
```

---

# What This Test Verifies

This test checks that the **Docs navigation link** contains the correct `href` attribute.

Example HTML element:

```
<a href="/python/docs/intro">Docs</a>
```

The assertion verifies that:

```
href="/python/docs/intro"
```

is present.

---

# How `to_have_attribute()` Works

```python
expect(locator).to_have_attribute("href", "/python/docs/intro")
```

Playwright performs the following steps:

```
Locate element
↓
Wait until element exists
↓
Retrieve attribute value
↓
Compare with expected value
↓
Retry until timeout if mismatch
```

Default timeout: **5 seconds**

---

# Common Attribute Assertions

Below are common attribute checks used in UI automation.

---

# Verify Link URL

```python
expect(link).to_have_attribute("href", "/docs/intro")
```

Used to verify navigation links.

---

# Verify Image Source

```python
image = page.locator("img.logo")

expect(image).to_have_attribute("src", "/images/logo.png")
```

Ensures the correct image is displayed.

---

# Verify Input Type

```python
email_input = page.locator("input#email")

expect(email_input).to_have_attribute("type", "email")
```

Ensures the correct input type is used.

---

# Verify Element ID

```python
expect(locator).to_have_attribute("id", "main-menu")
```

Useful when validating page structure.

---

# Verify CSS Class

```python
expect(locator).to_have_attribute("class", "active")
```

Alternatively, Playwright provides a dedicated class assertion:

```python
expect(locator).to_have_class("active")
```

---

# Verify ARIA Attributes

Accessibility attributes can also be tested.

Example:

```python
expect(locator).to_have_attribute("aria-label", "Search")
```

These attributes improve accessibility for screen readers.

---

# Regex Attribute Matching

Playwright supports **regular expressions** for flexible matching.

Example:

```python
import re

expect(locator).to_have_attribute(
    "href",
    re.compile("/docs/")
)
```

This passes if the attribute contains `/docs/`.

---

# Timeout Configuration

Attribute assertions can use custom timeouts.

Example:

```python
expect(locator).to_have_attribute(
    "href",
    "/docs/intro",
    timeout=10000
)
```

This waits **10 seconds** before failing.

---

# Running the Test

Run the test using Pytest:

```bash
pytest test_attribute_assertions.py
```

Example output:

```
collected 1 item

test_attribute_assertions.py .          [100%]

1 passed
```

---

# Best Practices

When verifying element attributes:

✔ Use attribute assertions for **links and navigation validation**  
✔ Combine with **visibility assertions** for stronger tests  
✔ Prefer **regex matching for dynamic values**  
✔ Keep assertions clear and focused  

---

# Key Takeaways

✔ Playwright can verify element attributes using `to_have_attribute()`  
✔ Assertions automatically wait for the expected value  
✔ Works with links, images, inputs, and accessibility attributes  
✔ Supports exact matching and regex patterns  
✔ Essential for validating UI behavior and navigation

---
---

# Web-First Assertions on Input Fields

Playwright provides powerful assertions for verifying **input field behavior and values**.  
These assertions are useful when testing:

- Search fields
- Login forms
- Text inputs
- Dynamic form elements

Using Playwright's **web-first assertions**, tests automatically wait for the expected condition before failing.

Common input field assertions include:

- `to_be_editable()`
- `to_be_empty()`
- `to_have_value()`
- `to_be_visible()`
- `to_be_hidden()`

---

# Example Test

```python
from playwright.sync_api import Page, expect

# Constants
BASE_URL = "https://playwright.dev/python"
DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_get_started_link(page: Page):

    # Navigate to Playwright Python homepage
    page.goto(BASE_URL)

    input = page.get_by_placeholder("Search docs")

    # Input is hidden before clicking search
    expect(input).to_be_hidden()

    # Search button
    search_btn = page.get_by_role("button", name="Search")
    search_btn.click()

    # Search menu should appear
    expect(input).to_be_editable()
    expect(input).to_be_empty()

    text = "Assertions"

    input.fill(text)

    expect(input).to_have_value(text)
```

---

# What This Test Verifies

This test validates the behavior of the **Playwright documentation search input field**.

The test performs the following checks:

1. The search input field is initially **hidden**
2. Clicking the **Search button** opens the search input
3. The input becomes **editable**
4. The input is **initially empty**
5. The user enters text into the field
6. The entered value is verified

---

# Locating the Input Field

The input field is located using a **placeholder locator**.

```python
input = page.get_by_placeholder("Search docs")
```

This method identifies input elements using their placeholder text.

Example HTML:

```
<input placeholder="Search docs">
```

---

# Input Visibility Assertion

Before clicking the search button, the input field is hidden.

```python
expect(input).to_be_hidden()
```

This ensures the search input is not visible initially.

---

# Triggering the Search Menu

The search button is located using a **role locator**.

```python
search_btn = page.get_by_role("button", name="Search")
```

Clicking the button opens the search UI.

```python
search_btn.click()
```

---

# Editable Input Assertion

After clicking the search button, the input becomes editable.

```python
expect(input).to_be_editable()
```

This confirms the user can type into the input field.

---

# Empty Input Assertion

The input field should initially be empty.

```python
expect(input).to_be_empty()
```

This verifies the input field contains no text.

---

# Filling Text into Input

Playwright allows filling text using:

```python
input.fill(text)
```

Example:

```python
text = "Assertions"
input.fill(text)
```

---

# Verifying Input Value

After filling the text, the test verifies the value using:

```python
expect(input).to_have_value(text)
```

This ensures the input field contains the correct text.

---

# Additional Input Assertions

Playwright provides several useful assertions for input elements.

---

# Check Input Visibility

```python
expect(input).to_be_visible()
```

---

# Check Input is Disabled

```python
expect(input).to_be_disabled()
```

---

# Check Input is Enabled

```python
expect(input).to_be_enabled()
```

---

# Verify Partial Value

```python
expect(input).to_have_value("Assert")
```

---

# Regex Value Assertion

Playwright supports regular expression matching.

```python
import re

expect(input).to_have_value(re.compile("Assert"))
```

---

# Timeout Configuration

You can extend the waiting time for assertions.

Example:

```python
expect(input).to_have_value("Assertions", timeout=10000)
```

This waits **10 seconds** before failing.

---

# Running the Test

Run the test using Pytest:

```bash
pytest test_input_assertions.py
```

Example output:

```
collected 1 item

test_input_assertions.py .                    [100%]

1 passed
```

---

# Best Practices

When testing input fields:

✔ Verify **initial state of the input**  
✔ Check that input becomes **editable when expected**  
✔ Validate **input values after user interaction**  
✔ Use placeholder locators for better readability  

---

# Key Takeaways

✔ Playwright supports powerful **input field assertions**  
✔ Tests can verify input visibility, editability, and values  
✔ Assertions automatically wait for expected conditions  
✔ Useful for testing search fields, login forms, and user inputs

---
---

# Web-First Assertions for Checkboxes

Checkboxes are common UI components used in forms, settings pages, and configuration panels.  
Playwright provides built-in assertions to verify whether checkboxes are **checked or unchecked**.

These assertions are part of Playwright's **web-first assertions**, meaning they automatically wait until the expected state is reached before failing.

Common checkbox assertions include:

- `to_be_checked()`
- `not_to_be_checked()`

These assertions help verify the correct behavior of form inputs and user selections.

---

# Example Test

```python
from playwright.sync_api import Page, expect

# Constants
BASE_URL = "https://bootswatch.com/default"


def test_get_started_link(page: Page):

    # Navigate to the webpage
    page.goto(BASE_URL)

    default_checkbox = page.get_by_label("Default Checkbox")
    checked_checkbox = page.get_by_label("Checked checkbox")

    expect(checked_checkbox).to_be_checked()

    expect(default_checkbox).not_to_be_checked()
```

---

# What This Test Verifies

This test checks the default state of two checkboxes on the page.

The test verifies:

| Checkbox | Expected State |
|--------|--------|
| Checked checkbox | Checked |
| Default Checkbox | Not checked |

---

# Locating Checkboxes

Checkboxes are located using **label locators**.

```python
default_checkbox = page.get_by_label("Default Checkbox")
```

Example HTML structure:

```
<label>
    <input type="checkbox"> Default Checkbox
</label>
```

Using `get_by_label()` is recommended because it is:

✔ Accessible  
✔ Stable  
✔ Readable  

---

# Assertion: Checkbox is Checked

```python
expect(checked_checkbox).to_be_checked()
```

This verifies that the checkbox is selected.

Playwright automatically waits for the checkbox to become checked before failing.

---

# Assertion: Checkbox is Not Checked

```python
expect(default_checkbox).not_to_be_checked()
```

This ensures the checkbox is **not selected**.

The `not_` prefix negates the assertion.

---

# Checkbox Interaction Example

Checkboxes can be clicked and verified.

Example:

```python
checkbox = page.get_by_label("Default Checkbox")

checkbox.check()

expect(checkbox).to_be_checked()
```

---

# Unchecking a Checkbox

Playwright also allows unchecking checkboxes.

```python
checkbox.uncheck()

expect(checkbox).not_to_be_checked()
```

---

# Toggle Checkbox State

Sometimes a checkbox needs to be toggled.

Example:

```python
checkbox.click()

expect(checkbox).to_be_checked()
```

---

# Verifying Multiple Checkboxes

If multiple checkboxes exist, they can be verified individually.

Example:

```python
checkboxes = page.locator("input[type='checkbox']")

expect(checkboxes).to_have_count(3)
```

---

# Timeout Configuration

Checkbox assertions support custom timeout values.

Example:

```python
expect(checkbox).to_be_checked(timeout=10000)
```

This waits **10 seconds** before failing.

---

# Running the Test

Run the test with Pytest:

```bash
pytest test_checkbox_assertions.py
```

Example output:

```
collected 1 item

test_checkbox_assertions.py .                [100%]

1 passed
```

---

# Best Practices

When testing checkboxes:

✔ Use **label locators** instead of CSS selectors  
✔ Verify **default checkbox state**  
✔ Test both **checked and unchecked states**  
✔ Use Playwright's `check()` and `uncheck()` methods  

---

# Key Takeaways

✔ Playwright provides assertions for checkbox states  
✔ `to_be_checked()` verifies selected checkboxes  
✔ `not_to_be_checked()` verifies unselected checkboxes  
✔ Assertions automatically wait for the expected state  
✔ Useful for testing forms and user input validation

---
---

# Web-First Assertions for Option Menus (Select Dropdowns)

Dropdown menus are widely used in web applications for selecting options from a list.  
Playwright provides built-in assertions to verify the **selected value(s) of dropdown menus**.

These assertions are part of Playwright's **web-first assertion system**, meaning they automatically wait until the expected value appears before failing the test.

Dropdown assertions are commonly used to verify:

- Default selected options
- User-selected values
- Multi-select behavior
- Form input correctness

Playwright provides the following assertion methods for dropdown menus:

- `to_have_value()` → for single-select dropdowns  
- `to_have_values()` → for multi-select dropdowns  

---

# Example Test

```python
from playwright.sync_api import Page, expect

# Constants
BASE_URL = "https://bootswatch.com/default"


def test_app(page: Page):

    # Navigate to the webpage
    page.goto(BASE_URL)

    option_menu = page.get_by_label("Example select")

    expect(option_menu).to_have_value("1")

    multi_select_option_menu = page.get_by_label("Example multiple select")

    expect(multi_select_option_menu).to_have_values([])

    selected_options = ["2", "4"]

    multi_select_option_menu.select_option(selected_options)

    expect(multi_select_option_menu).to_have_values(selected_options)
```

---

# What This Test Verifies

This test validates the behavior of **single-select and multi-select dropdown menus**.

The test checks:

1. The **default selected option** in a single dropdown
2. The **initial state of a multi-select dropdown**
3. Selecting multiple options
4. Verifying the selected values

---

# Locating Dropdown Menus

Dropdown elements are located using **label-based locators**.

```python
option_menu = page.get_by_label("Example select")
```

Example HTML:

```
<label for="example-select">Example select</label>
<select id="example-select">
    <option value="1">Option 1</option>
</select>
```

Using `get_by_label()` improves:

✔ Accessibility  
✔ Test readability  
✔ Locator stability  

---

# Assertion: Single Select Dropdown

Single dropdowns contain **one selected value**.

```python
expect(option_menu).to_have_value("1")
```

This verifies that the selected option has the value `"1"`.

Example HTML:

```
<option value="1" selected>Option 1</option>
```

---

# Assertion: Multi-Select Dropdown

Multi-select dropdowns allow multiple values to be selected.

Example assertion:

```python
expect(multi_select_option_menu).to_have_values([])
```

This verifies that **no options are selected initially**.

---

# Selecting Multiple Options

Playwright allows selecting multiple options using:

```python
multi_select_option_menu.select_option(["2", "4"])
```

This selects options with values:

```
2
4
```

---

# Verify Selected Options

After selecting options, we verify them using:

```python
expect(multi_select_option_menu).to_have_values(["2", "4"])
```

This ensures the correct options are selected.

---

# Selecting Options by Label

Playwright can also select options by visible label.

Example:

```python
dropdown.select_option(label="Option 1")
```

---

# Selecting Options by Index

Example:

```python
dropdown.select_option(index=2)
```

This selects the third option in the list.

---

# Clearing Selected Options

For multi-select dropdowns, you can clear selections.

Example:

```python
dropdown.select_option([])
```

Then verify:

```python
expect(dropdown).to_have_values([])
```

---

# Timeout Configuration

Dropdown assertions support custom timeouts.

Example:

```python
expect(option_menu).to_have_value("1", timeout=10000)
```

This waits **10 seconds** before failing.

---

# Running the Test

Run the test with Pytest:

```bash
pytest test_dropdown_assertions.py
```

Example output:

```
collected 1 item

test_dropdown_assertions.py .            [100%]

1 passed
```

---

# Best Practices

When testing dropdown menus:

✔ Verify **default selected values**  
✔ Test **user interactions with dropdowns**  
✔ Validate **multi-select behavior**  
✔ Use `get_by_label()` for reliable locators  

---

# Key Takeaways

✔ Playwright supports assertions for dropdown menus  
✔ `to_have_value()` verifies single select dropdowns  
✔ `to_have_values()` verifies multi-select dropdowns  
✔ Tests can validate both default and selected values  
✔ Useful for testing forms and user selections

---
---

# UI Testing Playground – Overlapped Element Handling

The **UI Testing Playground** is a website designed specifically for practicing automation testing scenarios.

Website:

```
http://uitestingplayground.com
```

It contains several tricky UI situations that commonly appear in **automation testing interviews**, including:

- Dynamic IDs
- Overlapped elements
- Delayed AJAX responses
- Hidden elements
- Scrollable elements
- Shadow DOM
- Click interception issues

Automation engineers often use this site to demonstrate their ability to **handle complex UI behaviors**.

---

# Overlapped Element Scenario

One common automation challenge occurs when an element is **partially hidden or overlapped by another element**.

This can cause automation failures such as:

```
Element is not clickable
Element is not visible
Element is outside viewport
```

To interact with such elements, testers may need to:

- Scroll the page
- Hover over containers
- Use JavaScript scrolling
- Use Playwright mouse actions

---

# Example Test: Handling Overlapped Input Field

```python
from playwright.sync_api import Page, expect


def test_fill_input_field_with_overlapped_element(page: Page):

    # Navigate to UI Testing Playground
    page.goto("http://uitestingplayground.com/")

    # Open the Overlapped Element page
    overlapped_element_link = page.get_by_role("link", name="Overlapped Element")
    overlapped_element_link.click()

    # Locate the input field
    name_input = page.get_by_placeholder("Name")

    # Hover over the container element to bring it into focus
    scroll_container = name_input.locator("..")
    scroll_container.hover()

    # Scroll the page using mouse wheel
    page.mouse.wheel(0, 200)

    # Enter test data
    test_data = "python"
    name_input.fill(test_data)

    # Verify the input value
    expect(name_input).to_have_value(test_data)
```

---

# What This Test Demonstrates

This test demonstrates how to handle **overlapped UI elements** in automation.

Steps performed:

1. Open the UI Testing Playground homepage
2. Navigate to the **Overlapped Element** scenario
3. Locate the hidden input field
4. Scroll the page to reveal the input element
5. Enter text into the input field
6. Verify that the correct value was entered

---

# Locating the Input Field

The input field is located using a **placeholder locator**.

```python
name_input = page.get_by_placeholder("Name")
```

Example HTML:

```
<input placeholder="Name">
```

Placeholder locators are useful for identifying form inputs.

---

# Handling Overlapped Elements

The input field is inside a **scrollable container**.

To interact with it, we first locate the parent container:

```python
scroll_container = name_input.locator("..")
```

The `".."` locator selects the **parent element**.

---

# Hovering Over the Container

Hovering ensures the element receives focus.

```python
scroll_container.hover()
```

This mimics real user interaction.

---

# Scrolling the Page

Playwright allows simulating mouse scrolling.

```python
page.mouse.wheel(0, 200)
```

Parameters:

```
mouse.wheel(x, y)
```

| Parameter | Description |
|---|---|
| x | Horizontal scroll |
| y | Vertical scroll |

In this example:

```
Scroll down 200 pixels
```

---

# Filling the Input Field

Once the element is visible, we can enter text.

```python
name_input.fill("python")
```

This simulates user typing.

---

# Verifying the Input Value

Playwright verifies that the correct value was entered.

```python
expect(name_input).to_have_value("python")
```

Web-first assertions ensure the test waits until the value appears.

---

# Common Automation Problems with Overlapped Elements

Automation frameworks often fail when elements are:

- hidden
- overlapped
- outside the viewport
- blocked by floating headers

Typical error messages include:

```
Element not visible
Element not clickable
Timeout exceeded
```

Playwright solves these issues using:

- automatic waiting
- scrolling
- hover actions
- locator-based interaction

---

# Alternative Scrolling Methods

Playwright also supports other scrolling techniques.

### Scroll element into view

```python
locator.scroll_into_view_if_needed()
```

---

### JavaScript scroll

```python
page.evaluate("window.scrollBy(0, 200)")
```

---

### Keyboard scrolling

```python
page.keyboard.press("PageDown")
```

---

# Running the Test

Run the test with Pytest:

```
pytest test_overlapped_element.py
```

Example output:

```
collected 1 item

test_overlapped_element.py .                 [100%]

1 passed
```

---

# Why UI Testing Playground is Important

UI Testing Playground is commonly used in **automation interviews** because it tests the candidate's ability to handle:

- tricky UI behaviors
- dynamic elements
- asynchronous content
- scrolling issues
- locator strategies

Many automation engineers practice on this site to improve their **Playwright and Selenium debugging skills**.

---

# Key Takeaways

✔ UI Testing Playground is a popular automation practice website  
✔ Overlapped elements may require scrolling or hovering  
✔ Playwright mouse actions help reveal hidden elements  
✔ Web-first assertions verify the correct interaction  
✔ Handling complex UI behavior is a key automation testing skill

---
---

# UI Testing Playground – Handling AJAX Requests

Modern web applications frequently use **AJAX (Asynchronous JavaScript and XML)** to load data dynamically without refreshing the entire page.

In automation testing, AJAX can cause challenges because:

- Elements appear **after a delay**
- Content loads **asynchronously**
- The UI updates **after network requests**

If tests try to interact with elements **before the AJAX request finishes**, they may fail with errors such as:

```
Element not found
Timeout exceeded
Element not visible
```

Playwright solves this problem using **automatic waiting and web-first assertions**.

The **UI Testing Playground AJAX Data scenario** is commonly used in automation interviews to test how engineers handle delayed content.

Website:

```
http://uitestingplayground.com/ajax
```

---

# Example Test: Handling AJAX Data Loading

```python
from playwright.sync_api import Page, expect
import pytest


def test_ajax_data_loading(page: Page):

    # Navigate to UI Testing Playground
    page.goto("http://uitestingplayground.com/")

    # Open the AJAX Data scenario
    ajax_data_link = page.get_by_role("link", name="AJAX Data")
    ajax_data_link.click()

    # Button that triggers the AJAX request
    ajax_button = page.get_by_role("button", name="Button Triggering AJAX Request")

    ajax_button.click()

    # Confirmation text that appears after the AJAX request completes
    confirmation_text = page.locator("p.bg-success")

    # Wait until the element becomes visible
    confirmation_text.wait_for(state="visible")

    # Verify the element is visible
    expect(confirmation_text).to_be_visible()
```

---

# What This Test Demonstrates

This test demonstrates how to handle **delayed UI elements caused by AJAX requests**.

Steps performed:

1. Navigate to the **UI Testing Playground homepage**
2. Open the **AJAX Data example**
3. Click the button that triggers an AJAX request
4. Wait for the confirmation message to appear
5. Verify that the message becomes visible

---

# AJAX Behavior on This Page

When the button is clicked:

```
Button clicked
↓
AJAX request sent to server
↓
Server processes request
↓
Response returned after delay
↓
Confirmation message appears
```

This delay simulates real-world web applications where data loads asynchronously.

---

# Locating the AJAX Trigger Button

The button is located using a **role locator**.

```python
ajax_button = page.get_by_role(
    "button",
    name="Button Triggering AJAX Request"
)
```

This is a reliable and readable locator.

---

# Waiting for the AJAX Response

The confirmation message appears after the AJAX request completes.

```python
confirmation_text = page.locator("p.bg-success")
```

Example HTML:

```
<p class="bg-success">
    Data loaded with AJAX get request.
</p>
```

---

# Explicit Waiting

The test waits for the element to become visible.

```python
confirmation_text.wait_for(state="visible")
```

This ensures the test does not proceed until the UI updates.

Available states:

| State | Description |
|------|-------------|
| visible | Element appears on screen |
| hidden | Element becomes hidden |
| attached | Element added to DOM |
| detached | Element removed from DOM |

---

# Assertion

Finally, the test verifies the element is visible.

```python
expect(confirmation_text).to_be_visible()
```

Playwright's **web-first assertions automatically retry** until the condition becomes true.

---

# Alternative Waiting Strategies

Playwright provides multiple ways to handle AJAX delays.

---

# 1. Web-First Assertion (Recommended)

Playwright automatically waits:

```python
expect(confirmation_text).to_be_visible()
```

This is usually sufficient.

---

# 2. Locator Wait

Explicit waiting for element visibility:

```python
confirmation_text.wait_for(state="visible")
```

---

# 3. Wait for Network Response

You can wait for specific API responses.

Example:

```python
page.wait_for_response("**/ajax")
```

---

# 4. Wait for Selector

Example:

```python
page.wait_for_selector("p.bg-success")
```

---

# Running the Test

Run the test with Pytest:

```bash
pytest test_ajax_data.py
```

Example output:

```
collected 1 item

test_ajax_data.py .                      [100%]

1 passed
```

---

# Why AJAX Handling is Important

Most modern applications rely heavily on AJAX requests.

Automation engineers must handle:

- delayed elements
- asynchronous API responses
- dynamic UI updates
- loading spinners

Handling these correctly prevents **flaky automation tests**.

---

# Common Interview Question

Automation interviews often ask:

> How do you handle AJAX requests in Playwright?

Good answers include:

- Web-first assertions
- Waiting for selectors
- Waiting for network responses
- Locator state checks

---

# Key Takeaways

✔ AJAX loads data asynchronously without page refresh  
✔ Tests must wait for dynamic content to appear  
✔ Playwright provides automatic waiting mechanisms  
✔ Web-first assertions help prevent flaky tests  
✔ Proper waiting strategies are essential for reliable automation

---
---

# UI Testing Playground – Sample App (Login Form Automation)

The **Sample App** scenario in UI Testing Playground simulates a simple login workflow.  
It is commonly used in automation testing interviews to verify that candidates can automate:

- Form input fields
- User authentication workflows
- Button interactions
- Dynamic text verification

Website:

```
http://uitestingplayground.com/sampleapp
```

This scenario demonstrates how automation scripts interact with **username and password fields**, submit the form, and verify the login status message.

---

# Example Test: Automating Login and Verifying Success Message

```python
from playwright.sync_api import Page, expect


def test_sample_app_login(page: Page):

    # Navigate to UI Testing Playground
    page.goto("http://uitestingplayground.com/")

    # Open Sample App page
    sample_app_link = page.get_by_role("link", name="Sample App")
    sample_app_link.click()

    # Locate username and password fields
    username_input = page.get_by_placeholder("User Name")
    password_input = page.get_by_placeholder("********")

    username = "test"
    password = "pwd"

    username_input.fill(username)
    password_input.fill(password)

    # Click login button
    login_button = page.get_by_role("button", name="Log In")
    login_button.click()

    # Locate login status message
    login_status = page.locator("label#loginstatus")

    # Verify successful login message
    expect(login_status).to_have_text(f"Welcome, {username}!")
```

---

# What This Test Demonstrates

This test automates a **basic login workflow** and verifies that the application responds correctly.

Steps performed:

1. Open the UI Testing Playground homepage
2. Navigate to the **Sample App** page
3. Enter a username
4. Enter a password
5. Click the **Log In** button
6. Verify the login confirmation message

---

# Locating Input Fields

The test locates the username field using a **placeholder locator**.

```python
username_input = page.get_by_placeholder("User Name")
```

Example HTML:

```
<input placeholder="User Name">
```

The password field is located similarly.

```python
password_input = page.get_by_placeholder("********")
```

---

# Filling Form Inputs

Playwright allows filling text inputs using:

```python
input.fill(value)
```

Example:

```python
username_input.fill("test")
password_input.fill("pwd")
```

This simulates user typing.

---

# Clicking the Login Button

The login button is located using a **role locator**.

```python
login_button = page.get_by_role("button", name="Log In")
```

Role locators are recommended because they:

✔ Follow accessibility standards  
✔ Are more stable than CSS selectors  
✔ Improve test readability  

---

# Verifying the Login Result

After clicking the login button, the application displays a status message.

Example HTML:

```
<label id="loginstatus">Welcome, test!</label>
```

The test verifies the text using:

```python
expect(login_status).to_have_text(f"Welcome, {username}!")
```

Playwright automatically waits until the expected text appears.

---

# Why This Scenario is Important

This example demonstrates common automation tasks used in real applications:

- Login workflows
- Form validation
- User input automation
- UI text verification

Automation engineers frequently automate similar flows in:

- authentication systems
- admin panels
- web applications
- user portals

---

# Running the Test

Run the test with Pytest:

```bash
pytest test_sample_app.py
```

Example output:

```
collected 1 item

test_sample_app.py .                     [100%]

1 passed
```

---

# Best Practices for Login Automation

When automating login forms:

✔ Use **placeholder or label locators** for inputs  
✔ Verify **login success messages**  
✔ Use **web-first assertions** to avoid flaky tests  
✔ Keep test credentials in variables  

---

# Key Takeaways

✔ The Sample App demonstrates login automation  
✔ Playwright can interact with form inputs easily  
✔ Web-first assertions verify dynamic UI messages  
✔ This scenario is commonly used in automation interviews

---
---

# UI Testing Playground – Handling Dynamic Class Attributes

Modern web applications often generate **dynamic CSS classes**.  
These classes may change between page loads, deployments, or UI states.

Dynamic attributes make automation challenging because:

- Selectors may break frequently
- Class names may contain multiple values
- The order of classes may change
- Elements may share multiple class names

The **UI Testing Playground Dynamic Class scenario** demonstrates this problem.

Website:

```
http://uitestingplayground.com/classattr
```

This page contains a button whose **class attribute contains multiple dynamic values**.

Automation engineers must use **robust locator strategies** to reliably identify the element.

---

# Example Test: Handling Dynamic Class Attributes

```python
from playwright.sync_api import Page, expect


def test_dynamic_class_button_click(page: Page):

    page.goto("http://uitestingplayground.com/classattr")

    # Locate button using CSS class selector
    button = page.locator("button.btn-primary")

    # Alternative robust locator using XPath
    button = page.locator("//button[contains(@class, 'btn-primary')]")

    expect(button).to_be_visible()

    button.click()
```

---

# What This Test Demonstrates

This test demonstrates how to **reliably locate elements with dynamic class attributes**.

Steps performed:

1. Navigate to the **Dynamic Class Attribute page**
2. Locate the button using a class-based selector
3. Verify the button is visible
4. Click the button

---

# The Dynamic Class Problem

Example HTML from the page:

```
<button class="btn btn-primary btn-lg">
    Primary Button
</button>
```

Possible variations:

```
btn btn-primary btn-lg
btn btn-lg btn-primary
btn-primary btn btn-lg
```

Because the class attribute contains **multiple values**, exact matching may fail.

---

# CSS Selector Strategy

One approach is using a **CSS class selector**.

```python
button = page.locator("button.btn-primary")
```

This selects:

```
<button class="btn-primary">
```

or any element containing the class `btn-primary`.

Advantages:

✔ Simple  
✔ Fast  
✔ Readable  

---

# XPath Contains Strategy

Another reliable approach uses **XPath contains()**.

```python
button = page.locator("//button[contains(@class, 'btn-primary')]")
```

This matches elements where the class attribute **contains the specified value**.

Example:

```
class="btn btn-primary btn-lg"
```

---

# Why Dynamic Attributes Are Important in Interviews

Automation interviews often include questions like:

> How do you handle dynamic attributes?

Common strategies include:

- Using **partial matches**
- Using **contains() selectors**
- Using **role-based locators**
- Using **text-based locators**

---

# Alternative Playwright Locator Strategies

Playwright provides multiple reliable locator strategies.

---

# Role Locator (Recommended)

```python
button = page.get_by_role("button", name="Primary Button")
```

Advantages:

✔ Stable  
✔ Accessible  
✔ Recommended by Playwright  

---

# Text Locator

```python
button = page.get_by_text("Primary Button")
```

---

# Data Attribute Locator

Many production apps use testing attributes.

Example:

```
<button data-testid="primary-btn">
```

Locator:

```python
page.get_by_test_id("primary-btn")
```

---

# Running the Test

Run the test with Pytest:

```bash
pytest test_dynamic_class.py
```

Example output:

```
collected 1 item

test_dynamic_class.py .                 [100%]

1 passed
```

---

# Best Practices for Dynamic Attributes

When dealing with dynamic selectors:

✔ Avoid exact class matching  
✔ Prefer **role-based locators**  
✔ Use **contains() for partial matching**  
✔ Use **stable attributes when available**

---

# Key Takeaways

✔ Dynamic attributes are common in modern web apps  
✔ Exact selectors can break automation tests  
✔ Playwright provides multiple robust locator strategies  
✔ Partial matching and role locators improve test stability  
✔ Handling dynamic selectors is a common automation interview topic

---
---

# UI Testing Playground – Handling Dynamic IDs

Many modern web applications generate **dynamic IDs** for elements.  
These IDs change every time the page loads or the application is deployed.

Example:

```
id="button_12345"
id="button_67890"
id="button_98231"
```

This makes automation difficult because selectors based on **exact IDs will break**.

The **UI Testing Playground Dynamic ID scenario** demonstrates this problem and is frequently used in **automation testing interviews**.

Website:

```
http://uitestingplayground.com/dynamicid
```

Automation engineers must use **stable locator strategies** instead of relying on dynamic attributes.

---

# Example Test: Handling Dynamic IDs

```python
from playwright.sync_api import Page, expect

def test_dynamic_id_button_click(page: Page):

    page.goto("http://uitestingplayground.com/dynamicid")

    dynamic_id_button = page.get_by_role(
        "button",
        name="Button with Dynamic ID"
    )

    expect(dynamic_id_button).to_be_visible()

    dynamic_id_button.click()
```

---

# What This Test Demonstrates

This test shows how to **interact with elements that have dynamic IDs**.

Steps performed:

1. Open the **Dynamic ID page**
2. Locate the button using a stable locator
3. Verify the button is visible
4. Click the button

The test avoids using the element's ID because it **changes dynamically**.

---

# Example Dynamic HTML

Example element from the page:

```
<button id="button_12345">
    Button with Dynamic ID
</button>
```

After reload:

```
<button id="button_98231">
    Button with Dynamic ID
</button>
```

Since the ID changes, a selector like:

```
#button_12345
```

would fail.

---

# Why Dynamic IDs Are Problematic

Dynamic IDs cause common automation failures:

```
Element not found
Locator failed
Timeout exceeded
```

Automation engineers must use **stable attributes or text-based selectors** instead.

---

# Recommended Locator Strategy (Role Locator)

The best approach is using **Playwright role locators**.

```python
page.get_by_role("button", name="Button with Dynamic ID")
```

Advantages:

✔ Stable across page reloads  
✔ Uses accessibility roles  
✔ Easy to read and maintain  

---

# Alternative Locator Strategies

Playwright provides multiple ways to handle dynamic attributes.

---

# Text Locator

```python
button = page.get_by_text("Button with Dynamic ID")
```

This locates elements based on visible text.

---

# Partial Attribute Matching

If the ID has a stable prefix:

Example:

```
id="button_12345"
```

You can use:

```python
page.locator("[id^='button_']")
```

This means:

```
ID starts with "button_"
```

---

# XPath Contains Selector

Another approach uses XPath.

```python
page.locator("//button[contains(@id,'button_')]")
```

---

# Data Test Attributes (Best Practice in Real Projects)

Production applications often include testing attributes.

Example:

```
<button data-testid="dynamic-button">
```

Locator:

```python
page.get_by_test_id("dynamic-button")
```

This is the **most stable approach** in large automation frameworks.

---

# Running the Test

Run the test using Pytest:

```
pytest test_dynamic_id.py
```

Example output:

```
collected 1 item

test_dynamic_id.py .                [100%]

1 passed
```

---

# Why Dynamic ID Handling Is Important

Dynamic IDs are common in modern frameworks such as:

- React
- Angular
- Vue
- Next.js

Automation engineers must design **robust locators** that remain stable even when attributes change.

This skill is frequently tested in **Playwright and Selenium interviews**.

---

# Best Practices

When dealing with dynamic attributes:

✔ Avoid relying on IDs  
✔ Prefer **role-based locators**  
✔ Use **text-based selectors**  
✔ Use **data-testid attributes when available**

---

# Key Takeaways

✔ Dynamic IDs change between page loads  
✔ ID-based selectors can break automation tests  
✔ Role locators provide stable element identification  
✔ Playwright offers multiple robust locator strategies  
✔ Handling dynamic elements is a common automation interview scenario

---
---

# UI Testing Playground – Dynamic Table Validation

Dynamic tables are common in modern web applications such as:

- dashboards
- analytics tools
- monitoring systems
- admin panels

Automation engineers must be able to **read data from tables, identify rows and columns dynamically, and validate values correctly**.

The **UI Testing Playground Dynamic Table scenario** is designed to test this ability.

Website:

```
http://uitestingplayground.com/dynamictable
```

The page contains a table with CPU usage for different browsers.  
A label above the table displays the CPU value for **Chrome**, and the test must verify that this value matches the value inside the table.

---

# Example Test: Validating Dynamic Table Data

```python
from playwright.sync_api import Page
import pytest


def test_validate_dynamic_table_cpu_value(page: Page):

    page.goto("http://uitestingplayground.com/")

    dynamic_table_link = page.get_by_role("link", name="Dynamic Table")
    dynamic_table_link.click()

    label = page.locator("p.bg-warning").inner_text()

    percentage = label.split()[-1]

    column_headers = page.get_by_role("columnheader")

    cpu_column = None

    for index in range(column_headers.count()):
        column_header = column_headers.nth(index)

        if column_header.inner_text() == "CPU":
            cpu_column = index
            break

    assert cpu_column is not None

    chrome_row = page.get_by_role("row").filter(has_text="Chrome")

    chrome_cpu = chrome_row.get_by_role("cell").nth(cpu_column)

    assert percentage == chrome_cpu.inner_text()
```

---

# What This Test Demonstrates

This test verifies that the **CPU usage value displayed in the label matches the value inside the table for Chrome**.

Steps performed:

1. Navigate to UI Testing Playground
2. Open the **Dynamic Table** page
3. Extract CPU value from the label
4. Identify the **CPU column dynamically**
5. Locate the **Chrome row**
6. Extract CPU value from the table
7. Compare both values

---

# Understanding the Dynamic Table

Example UI:

```
Chrome CPU: 27%
```

Table:

| Browser | CPU | Memory |
|--------|----|----|
| Chrome | 27% | 90MB |
| Firefox | 12% | 70MB |
| Edge | 15% | 65MB |

The goal is to verify that:

```
Label CPU value == Chrome row CPU value
```

---

# Extracting the Label Value

The label containing the CPU percentage is located using:

```python
label = page.locator("p.bg-warning").inner_text()
```

Example text:

```
Chrome CPU: 27%
```

To extract the percentage:

```python
percentage = label.split()[-1]
```

This retrieves:

```
27%
```

---

# Finding the CPU Column Dynamically

Instead of hardcoding the column index, the test identifies the **CPU column dynamically**.

```python
column_headers = page.get_by_role("columnheader")
```

Loop through headers:

```python
for index in range(column_headers.count()):
```

Check the header text:

```python
if column_header.inner_text() == "CPU":
```

Once found:

```
cpu_column = index
```

This makes the test **resilient to column order changes**.

---

# Locating the Chrome Row

The Chrome row is located using text filtering.

```python
chrome_row = page.get_by_role("row").filter(has_text="Chrome")
```

This selects the row that contains the word **Chrome**.

---

# Extracting the CPU Value from the Table

Once the row is located, the CPU column value is extracted.

```python
chrome_cpu = chrome_row.get_by_role("cell").nth(cpu_column)
```

Example result:

```
27%
```

---

# Validating the Data

The test compares the label value with the table value.

```python
assert percentage == chrome_cpu.inner_text()
```

If both values match, the test passes.

---

# Why This Scenario is Important

Dynamic table handling is a **common real-world automation task**.

Automation engineers frequently need to:

- extract table data
- validate dynamic values
- compare UI elements
- verify dashboard metrics

This scenario tests **logical automation skills**, not just simple element interaction.

---

# Common Interview Question

Automation interviews often ask:

> How do you validate data in dynamic tables?

Good approaches include:

- locating headers dynamically
- identifying rows using text filters
- extracting column values programmatically
- comparing UI values

---

# Running the Test

Run the test with Pytest:

```bash
pytest test_dynamic_table.py
```

Example output:

```
collected 1 item

test_dynamic_table.py .           [100%]

1 passed
```

---

# Best Practices for Table Automation

When working with dynamic tables:

✔ Identify columns dynamically  
✔ Avoid hardcoding column indexes  
✔ Use text filters to locate rows  
✔ Extract table data programmatically  

---

# Key Takeaways

✔ Dynamic tables require programmatic data extraction  
✔ Column indexes should be determined dynamically  
✔ Row filtering simplifies table navigation  
✔ Automation tests can validate UI data against labels or other UI elements  

---
---

# UI Testing Playground – Hidden Layers (Click Interception)

Modern web applications often contain **overlapping elements or hidden layers** that block user interactions.

These layers may appear due to:

- modal dialogs
- floating headers
- animations
- dynamic overlays
- CSS positioning

In automation testing, this often leads to errors such as:

```
Element is not clickable
Element is obscured
Timeout exceeded
```

The **UI Testing Playground Hidden Layers scenario** demonstrates this problem.

Website:

```
http://uitestingplayground.com/hiddenlayers
```

This page contains a **green button** that becomes hidden after the first click because another layer covers it.

Automation engineers must detect and handle this situation correctly.

---

# Example Test: Handling Hidden Layers

```python
from playwright.sync_api import Page, TimeoutError
import pytest


def test_hidden_layers_click_behavior(page: Page):

    page.goto("http://uitestingplayground.com/hiddenlayers")

    green_btn = page.locator("button#greenButton")

    # First click works
    green_btn.click()

    # Second click should fail because the button becomes hidden
    with pytest.raises(TimeoutError):
        green_btn.click(timeout=2000)
```

---

# What This Test Demonstrates

This test verifies that the **green button becomes hidden after the first click**.

Steps performed:

1. Navigate to the Hidden Layers page
2. Locate the green button
3. Click the button successfully
4. Attempt to click the button again
5. Verify that the second click fails

---

# Understanding the Hidden Layer Behavior

Initial UI:

```
[ Green Button ]
```

After clicking:

```
[ Invisible Overlay ]
[ Green Button (hidden underneath) ]
```

The overlay **intercepts the click**, preventing the button from being clicked again.

---

# Why the Second Click Fails

Playwright waits for an element to be:

- visible
- stable
- not covered by another element

When the button becomes hidden behind another layer, Playwright throws a **TimeoutError**.

Example error:

```
TimeoutError: Element is not visible or is covered by another element
```

---

# Handling the Expected Failure

The test intentionally verifies that the second click fails.

```python
with pytest.raises(TimeoutError):
```

This tells Pytest:

```
Expect a TimeoutError
```

If the error occurs, the test **passes**.

If no error occurs, the test **fails**.

---

# Why This Scenario Is Important

Hidden layers are common in modern UI frameworks such as:

- React
- Angular
- Vue
- Bootstrap

Automation engineers frequently encounter issues like:

- click interception
- invisible overlays
- animation layers
- hidden elements

Handling these scenarios correctly is a **key automation testing skill**.

---

# Strategies to Handle Hidden Elements

Automation engineers often resolve hidden element issues using:

---

# 1. Wait for Element to Become Visible

```python
locator.wait_for(state="visible")
```

---

# 2. Scroll Element into View

```python
locator.scroll_into_view_if_needed()
```

---

# 3. Use Force Click (Not Recommended)

```python
locator.click(force=True)
```

This bypasses Playwright's safety checks.

---

# 4. Remove Blocking Layer

Sometimes the overlay must be closed first.

Example:

```
Close modal dialog
Then click target element
```

---

# Running the Test

Run the test with Pytest:

```
pytest test_hidden_layers.py
```

Example output:

```
collected 1 item

test_hidden_layers.py .           [100%]

1 passed
```

---

# Why Hidden Layers Are an Interview Topic

Automation interview questions often include:

> Why does Playwright fail to click an element even though it exists?

The correct explanation usually involves:

- overlapping elements
- hidden layers
- click interception
- visibility issues

Understanding this concept demonstrates **advanced debugging skills**.

---

# Key Takeaways

✔ Hidden layers can block user interactions  
✔ Playwright prevents clicking covered elements  
✔ Timeout errors may indicate click interception  
✔ Pytest can validate expected failures using `pytest.raises()`  
✔ Handling overlays is a common automation testing challenge

---
---

# UI Testing Playground – Load Delay (Handling Delayed Elements)

Many modern web applications load elements **after a delay** due to:

- server processing
- API calls
- JavaScript rendering
- lazy loading
- client-side frameworks (React, Angular, Vue)

If automation scripts attempt to interact with elements **before they appear**, tests may fail with errors such as:

```
Element not found
Element not visible
Timeout exceeded
```

The **UI Testing Playground Load Delay scenario** simulates this behavior by displaying a button **after a few seconds delay**.

Website:

```
http://uitestingplayground.com/loaddelay
```

Automation engineers must implement proper **waiting strategies** to handle delayed elements reliably.

---

# Example Test: Handling Delayed Button Appearance

```python
from playwright.sync_api import Page, expect


def test_load_delay_button(page: Page):

    page.goto("http://uitestingplayground.com/")

    load_delay_link = page.get_by_role("link", name="Load Delay")
    load_delay_link.click()

    button_after_delay = page.get_by_role(
        "button",
        name="Button Appearing After Delay"
    )

    button_after_delay.wait_for(state="visible")

    expect(button_after_delay).to_be_visible()

    button_after_delay.click()
```

---

# What This Test Demonstrates

This test verifies that automation can correctly interact with elements that **appear after a delay**.

Steps performed:

1. Open UI Testing Playground
2. Navigate to the **Load Delay page**
3. Wait for the delayed button to appear
4. Verify the button is visible
5. Click the button

---

# Understanding the Load Delay Behavior

When the page loads:

```
Page loads
↓
No button visible
↓
Delay (approx. 3 seconds)
↓
Button appears
```

Automation scripts must **wait until the button becomes visible**.

---

# Waiting for Delayed Elements

The test uses:

```python
button_after_delay.wait_for(state="visible")
```

This ensures Playwright waits until the button appears.

Available states:

| State | Description |
|------|-------------|
| visible | Element appears on the page |
| hidden | Element becomes hidden |
| attached | Element added to DOM |
| detached | Element removed from DOM |

---

# Web-First Assertion

Playwright also provides web-first assertions that automatically wait.

```python
expect(button_after_delay).to_be_visible()
```

This assertion:

```
Locate element
↓
Wait until visible
↓
Pass if visible
↓
Fail after timeout
```

---

# Alternative Waiting Strategies

Playwright supports several synchronization techniques.

---

# 1. Web-First Assertions (Recommended)

```python
expect(locator).to_be_visible()
```

Automatically waits.

---

# 2. Explicit Locator Wait

```python
locator.wait_for(state="visible")
```

---

# 3. Wait for Selector

```python
page.wait_for_selector("button")
```

---

# 4. Wait for Network Response

```python
page.wait_for_response("**/api")
```

Useful for API-driven UI updates.

---

# Why Delayed Elements Are Important

Handling delayed elements is essential in automation testing because modern applications often rely on:

- asynchronous APIs
- dynamic UI rendering
- loading animations
- background data fetching

Without proper waiting strategies, tests become **flaky and unreliable**.

---

# Common Interview Question

Automation interviews often ask:

> How do you handle elements that appear after a delay?

Good answers include:

- web-first assertions
- locator waiting
- waiting for selectors
- waiting for network responses

---

# Running the Test

Run the test using Pytest:

```bash
pytest test_load_delay.py
```

Example output:

```
collected 1 item

test_load_delay.py .                [100%]

1 passed
```

---

# Best Practices for Delayed Elements

When working with delayed UI elements:

✔ Use **web-first assertions**  
✔ Avoid fixed sleep delays  
✔ Prefer locator-based waiting  
✔ Ensure elements are visible before interacting  

---

# Key Takeaways

✔ Many web applications load elements asynchronously  
✔ Tests must wait for delayed UI components  
✔ Playwright provides powerful waiting mechanisms  
✔ Web-first assertions help prevent flaky tests  
✔ Handling delayed elements is a common automation interview topic

---
---

# UI Testing Playground – Mouse Over (Hover & Double Click Actions)

Modern web applications often use **mouse hover interactions** to reveal hidden elements such as:

- dropdown menus
- tooltips
- navigation links
- contextual actions

Automation engineers must be able to simulate these user interactions.

The **UI Testing Playground Mouse Over scenario** demonstrates how hover actions can trigger UI changes.

Website:

```
http://uitestingplayground.com/mouseover
```

This page contains an element that reveals an **active link** when hovered, and clicking the link increases a click counter.

---

# Example Test: Hover and Double Click Interaction

```python
from playwright.sync_api import Page, expect


def test_mouse_over_interaction(page: Page):

    page.goto("http://uitestingplayground.com/")

    # Navigate to the Mouse Over page
    mouse_over_link = page.get_by_role("link", name="Mouse Over")
    mouse_over_link.click()

    # Hover over the "Click me" element
    click_me_button = page.get_by_title("Click me")
    click_me_button.hover()

    # Locate the active link revealed after hover
    active_link = page.get_by_title("Active Link")

    # Double-click the active link
    active_link.click(click_count=2)

    # Verify click counter
    click_counter = page.locator("span#clickCount")

    expect(click_counter).to_have_text("2")
```

---

# What This Test Demonstrates

This test verifies that hover interactions trigger UI behavior and that multiple clicks are correctly counted.

Steps performed:

1. Open the **UI Testing Playground homepage**
2. Navigate to the **Mouse Over page**
3. Hover over the "Click me" element
4. Reveal the **Active Link**
5. Double-click the active link
6. Verify that the click counter increases

---

# Hover Interaction

The hover action simulates a user moving the mouse over an element.

```python
click_me_button.hover()
```

Hover actions are useful when elements only appear after mouse interaction.

Examples include:

- dropdown menus
- tooltip elements
- navigation flyouts

---

# Double Click Action

Playwright allows multiple clicks using the `click_count` parameter.

```python
active_link.click(click_count=2)
```

This simulates a **double-click**.

Equivalent actions:

| Action | Example |
|------|------|
| Single click | `locator.click()` |
| Double click | `locator.click(click_count=2)` |
| Triple click | `locator.click(click_count=3)` |

---

# Verifying Click Count

The page contains a counter that increments when the active link is clicked.

Locator:

```python
click_counter = page.locator("span#clickCount")
```

Example HTML:

```
<span id="clickCount">2</span>
```

Assertion:

```python
expect(click_counter).to_have_text("2")
```

This verifies the link was clicked twice.

---

# Why Hover Testing Is Important

Hover interactions are commonly used in:

- navigation menus
- dropdown components
- tooltips
- interactive dashboards

Automation engineers must verify these behaviors to ensure UI functionality works correctly.

---

# Alternative Mouse Actions in Playwright

Playwright supports many mouse interactions.

---

# Right Click

```python
locator.click(button="right")
```

---

# Double Click

```python
locator.dblclick()
```

---

# Drag and Drop

```python
source.drag_to(target)
```

---

# Manual Mouse Movement

```python
page.mouse.move(300, 400)
```

---

# Running the Test

Run the test with Pytest:

```
pytest test_mouse_over.py
```

Example output:

```
collected 1 item

test_mouse_over.py .                 [100%]

1 passed
```

---

# Best Practices for Hover Testing

When testing hover interactions:

✔ Use `hover()` to simulate user behavior  
✔ Verify UI elements appear after hover  
✔ Combine hover with click assertions  
✔ Use web-first assertions for reliability  

---

# Key Takeaways

✔ Hover interactions reveal hidden UI elements  
✔ Playwright supports hover using `locator.hover()`  
✔ Multi-click actions can be simulated with `click_count`  
✔ Hover testing is important for menus, tooltips, and dynamic UI components

---
---

# UI Testing Playground – Non-Breaking Space (Handling Special Characters in Locators)

Web applications sometimes contain **special whitespace characters** that look like normal spaces but are technically different.

One of the most common examples is the **Non-Breaking Space**.

Character:

```
\u00A0
```

This character prevents line breaks between words and is often used in HTML for formatting.

Example:

```
My Button
```

Although it visually appears as:

```
My Button
```

The two strings are **not identical**, which can cause automation locators to fail.

The **UI Testing Playground Non-Breaking Space scenario** demonstrates this issue.

Website:

```
http://uitestingplayground.com/nbsp
```

Automation engineers must understand how to correctly locate elements that contain special characters.

---

# Example Test: Handling Non-Breaking Space in Button Text

```python
from playwright.sync_api import Page


def test_non_breaking_space_button(page: Page):

    page.goto("http://uitestingplayground.com/")

    # Navigate to Non-Breaking Space example
    nbsp_link = page.get_by_role("link", name="Non-Breaking Space")
    nbsp_link.click()

    # Locate button using the Unicode non-breaking space
    page.locator("//button[text()='My\u00a0Button']").click(timeout=2000)
```

---

# What This Test Demonstrates

This test demonstrates how to locate elements whose text contains **special whitespace characters**.

Steps performed:

1. Navigate to UI Testing Playground
2. Open the **Non-Breaking Space example**
3. Locate the button containing the special whitespace character
4. Click the button successfully

---

# Understanding the Non-Breaking Space Problem

The button text appears as:

```
My Button
```

But the actual HTML contains:

```
My&nbsp;Button
```

Which translates to:

```
My\u00A0Button
```

Because of this, a locator like:

```
My Button
```

will **fail to match the element**.

---

# Correct Locator Using Unicode

To match the element correctly, the locator must include the Unicode character:

```python
page.locator("//button[text()='My\u00a0Button']")
```

Here:

```
\u00a0
```

represents the **non-breaking space character**.

---

# Why This Scenario Is Important

Automation engineers frequently encounter problems when:

- UI text contains hidden characters
- text includes non-breaking spaces
- text includes special Unicode symbols
- formatting changes unexpectedly

Without understanding these characters, locators may fail even though the element appears correct visually.

---

# Alternative Locator Strategies

Playwright provides several ways to handle special characters.

---

# 1. Using `contains()` XPath

```python
page.locator("//button[contains(text(),'My')]")
```

This ignores exact spacing.

---

# 2. Using Playwright Text Locator

```python
page.get_by_text("My Button")
```

Playwright's text engine often normalizes whitespace.

---

# 3. Using Role Locator (Recommended)

```python
page.get_by_role("button", name="My Button")
```

Role locators are usually **more stable than XPath**.

---

# Running the Test

Run the test with Pytest:

```bash
pytest test_non_breaking_space.py
```

Example output:

```
collected 1 item

test_non_breaking_space.py .         [100%]

1 passed
```

---

# Why This Scenario Appears in Interviews

Automation interviews sometimes include questions like:

> Why does a locator fail even though the text appears correct?

The answer may involve:

- non-breaking spaces
- hidden Unicode characters
- whitespace normalization
- HTML entities

Understanding these issues demonstrates **strong debugging skills in automation testing**.

---

# Key Takeaways

✔ Non-breaking spaces look like normal spaces but are different characters  
✔ They are represented by `\u00A0` in Unicode  
✔ Locators must sometimes include special characters to match elements  
✔ Role-based locators help avoid whitespace issues  
✔ Handling special characters is an important automation debugging skill

---
---

# UI Testing Playground – Progress Bar (Handling Dynamic UI Updates)

Many web applications use **progress indicators** to show the status of long-running operations such as:

- file uploads
- data processing
- API requests
- background tasks
- loading screens

Automation tests must correctly **monitor dynamic UI updates** and trigger actions at the right time.

The **UI Testing Playground Progress Bar scenario** demonstrates how automation can interact with a progress bar that updates continuously.

Website:

```
http://uitestingplayground.com/progressbar
```

In this scenario, the test must:

- start the progress bar
- monitor its value
- stop it when it reaches **75%**

---

# Example Test: Monitoring and Stopping Progress Bar

```python
from playwright.sync_api import Page


def test_stop_progress_bar_at_target(page: Page):

    page.goto("http://uitestingplayground.com/")

    progress_bar_link = page.get_by_role("link", name="Progress Bar")
    progress_bar_link.click()

    start_button = page.get_by_role("button", name="Start")
    stop_button = page.get_by_role("button", name="Stop")

    progress_bar = page.get_by_role("progressbar")

    start_button.click()

    # Poll the progress bar value
    while int(progress_bar.inner_text().replace("%", "")) < 75:
        pass

    stop_button.click()

    print(f"Progress bar stopped at {progress_bar.inner_text()}")
```

---

# What This Test Demonstrates

This test automates the process of **monitoring a progress bar and stopping it when a threshold is reached**.

Steps performed:

1. Navigate to UI Testing Playground
2. Open the **Progress Bar page**
3. Start the progress bar
4. Continuously monitor the progress value
5. Stop the progress when it reaches **75%**
6. Print the final progress value

---

# Understanding the Progress Bar

The progress bar displays values such as:

```
0%
15%
42%
67%
75%
90%
100%
```

The automation script must detect when the value reaches **75%** and immediately stop it.

---

# Extracting the Progress Value

The progress bar text looks like:

```
75%
```

To convert it into a number:

```python
progress_bar.inner_text().replace("%", "")
```

Example result:

```
"75"
```

Convert to integer:

```python
int("75")
```

Result:

```
75
```

---

# Polling the Progress Value

The test continuously checks the progress bar value.

```python
while int(progress_bar.inner_text().replace("%", "")) < 75:
    pass
```

This loop runs until the progress reaches the target threshold.

This technique is called **polling**.

---

# Why This Scenario Is Important

Automation engineers frequently encounter dynamic UI updates such as:

- loading indicators
- upload progress bars
- streaming data updates
- task completion indicators

Tests must be able to **observe UI changes and react accordingly**.

---

# Better Approach (Recommended in Production)

Busy loops like:

```python
while condition:
    pass
```

can consume CPU unnecessarily.

A better approach is using **Playwright waiting mechanisms**.

Example:

```python
page.wait_for_function(
    "() => parseInt(document.querySelector('[role=progressbar]').innerText) >= 75"
)
```

This waits efficiently until the condition becomes true.

---

# Running the Test

Run the test with Pytest:

```bash
pytest test_progress_bar.py
```

Example output:

```
collected 1 item

test_progress_bar.py .             [100%]

Progress bar stopped at 75%
```

---

# Why This Scenario Appears in Interviews

Automation interviews often ask:

> How would you handle a progress bar or dynamic UI value?

Expected answers include:

- polling the UI value
- waiting for a condition
- monitoring element text
- using Playwright wait functions

This scenario demonstrates **logical automation thinking**, not just simple element interaction.

---

# Best Practices for Dynamic UI Monitoring

When testing progress indicators:

✔ Avoid fixed delays like `sleep()`  
✔ Monitor UI values dynamically  
✔ Use Playwright wait functions when possible  
✔ Stop actions at defined thresholds  

---

# Key Takeaways

✔ Progress bars represent dynamic UI updates  
✔ Automation must monitor UI values continuously  
✔ Polling techniques can detect threshold values  
✔ Playwright wait functions provide efficient synchronization  
✔ Handling dynamic UI changes is a common automation interview topic

---
---

# UI Testing Playground – Scrollbars (Handling Elements Outside the Viewport)

In many web applications, some elements are **not immediately visible** because they are located outside the current viewport. These elements may require scrolling before they can be interacted with.

Common examples include:

- long pages
- hidden buttons
- elements inside scrollable containers
- lazy-loaded components

Automation tests must ensure that elements are **scrolled into view before interacting with them**.

The **UI Testing Playground Scrollbars scenario** demonstrates this behavior.

Website:

```
http://uitestingplayground.com/scrollbars
```

In this scenario, the **Hiding Button** is positioned outside the visible area and can only be accessed after scrolling.

---

# Example Test: Scrolling to Hidden Elements

```python
from playwright.sync_api import Page


def test_scroll_to_hidden_button(page: Page):

    page.goto("http://uitestingplayground.com/")

    # Navigate to the Scrollbars example
    scrollbars_link = page.get_by_role("link", name="Scrollbars")
    scrollbars_link.click()

    # Locate the hidden button
    hiding_button = page.get_by_role("button", name="Hiding Button")

    # Scroll the button into view
    hiding_button.scroll_into_view_if_needed()

    # Capture screenshot for verification
    page.screenshot(path="test-scrollbars.jpg")
```

---

# What This Test Demonstrates

This test verifies that automation can **locate and scroll to elements outside the visible area**.

Steps performed:

1. Open the **UI Testing Playground homepage**
2. Navigate to the **Scrollbars page**
3. Locate the hidden button
4. Scroll the page until the button becomes visible
5. Capture a screenshot of the page

---

# Why Elements Outside the Viewport Are a Problem

Automation scripts often fail when attempting to interact with elements that are not visible.

Typical errors include:

```
Element not visible
Element not clickable
Element outside viewport
```

Before interacting with such elements, automation frameworks must **scroll the element into view**.

---

# Scrolling an Element into View

Playwright provides a built-in method:

```python
locator.scroll_into_view_if_needed()
```

This method automatically scrolls the page until the element becomes visible.

Advantages:

✔ Automatically handles scrolling  
✔ Works for nested scroll containers  
✔ Prevents interaction failures  

---

# Taking Screenshots

The test captures a screenshot after scrolling.

```python
page.screenshot(path="test-scrollbars.jpg")
```

Screenshots are useful for:

- debugging automation
- visual validation
- test reporting
- CI/CD pipelines

Example output file:

```
test-scrollbars.jpg
```

---

# Alternative Scrolling Techniques

Playwright also supports other scrolling methods.

---

# Scroll Using JavaScript

```python
page.evaluate("window.scrollBy(0, 500)")
```

---

# Scroll Using Mouse Wheel

```python
page.mouse.wheel(0, 500)
```

---

# Scroll Page to Bottom

```python
page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
```

---

# Running the Test

Run the test using Pytest:

```bash
pytest test_scrollbars.py
```

Example output:

```
collected 1 item

test_scrollbars.py .                 [100%]

1 passed
```

---

# Why This Scenario Is Important

Handling elements outside the viewport is essential in automation testing because modern applications often contain:

- long scrolling pages
- hidden UI elements
- nested scroll containers
- dynamic content loading

Automation engineers must ensure that elements are **visible and accessible before interacting with them**.

---

# Best Practices for Scroll Automation

When working with scrollable pages:

✔ Use `scroll_into_view_if_needed()` before clicking  
✔ Avoid manual scrolling when possible  
✔ Capture screenshots for debugging  
✔ Ensure elements are visible before interacting  

---

# Key Takeaways

✔ Some UI elements are hidden outside the viewport  
✔ Automation scripts must scroll before interacting  
✔ Playwright provides `scroll_into_view_if_needed()` for this purpose  
✔ Screenshots help verify UI state and debug issues  

---
---

# UI Testing Playground – Text Input (Dynamic UI Update)

Modern web applications often change UI elements dynamically based on user input.

Examples include:

- dynamic button labels
- search results
- form validation messages
- live UI updates

Automation tests must verify that **user input correctly triggers UI updates**.

The **UI Testing Playground Text Input scenario** demonstrates this behavior.

Website:

```
http://uitestingplayground.com/textinput
```

In this example, typing text into an input field changes the **label of a button**.

---

# Example Test: Verifying Dynamic Button Text

```python
from playwright.sync_api import Page, expect


def test_text_input_updates_button_label(page: Page):

    page.goto("http://uitestingplayground.com/")

    # Navigate to Text Input page
    text_input_link = page.get_by_role("link", name="Text Input")
    text_input_link.click()

    # Locate input field
    input_field = page.get_by_label("Set New Button Name")

    query = "Awesome"

    # Enter text into input
    input_field.fill(query)

    # Locate button whose label changes
    dynamic_button = page.locator("button.btn-primary")

    # Click the button
    dynamic_button.click()

    # Verify button text changed
    expect(dynamic_button).to_have_text(query)
```

---

# What This Test Demonstrates

This test verifies that **user input correctly updates the button label**.

Steps performed:

1. Open the **UI Testing Playground homepage**
2. Navigate to the **Text Input page**
3. Enter text into the input field
4. Click the button
5. Verify that the button label updates with the entered text

---

# Understanding the Dynamic Behavior

Initial UI:

```
[Button That Should Change]
```

User input:

```
Awesome
```

After clicking the button:

```
[Awesome]
```

The button text dynamically changes based on the user input.

---

# Locating the Input Field

The input field is located using a **label locator**.

```python
input_field = page.get_by_label("Set New Button Name")
```

Example HTML:

```
<label>Set New Button Name</label>
<input type="text">
```

Using label locators improves:

✔ accessibility  
✔ test readability  
✔ locator stability  

---

# Filling Text in the Input Field

Playwright allows entering text using:

```python
input_field.fill("Awesome")
```

This simulates a user typing.

---

# Clicking the Dynamic Button

The button is located using a CSS locator.

```python
dynamic_button = page.locator("button.btn-primary")
```

The button text updates after clicking it.

---

# Verifying the Button Text

The test verifies the new button label.

```python
expect(dynamic_button).to_have_text(query)
```

Playwright automatically waits until the expected text appears.

---

# Why This Scenario Is Important

Dynamic UI updates are common in modern applications such as:

- React
- Angular
- Vue
- Next.js

Automation tests must confirm that **user interactions trigger the correct UI behavior**.

---

# Running the Test

Run the test using Pytest:

```bash
pytest test_text_input.py
```

Example output:

```
collected 1 item

test_text_input.py .                [100%]

1 passed
```

---

# Best Practices for Dynamic UI Testing

When testing dynamic UI updates:

✔ verify UI changes after user input  
✔ use web-first assertions for reliability  
✔ avoid fixed delays  
✔ validate visible text changes  

---

# Key Takeaways

✔ User input can dynamically change UI elements  
✔ Automation tests must verify UI updates after interactions  
✔ Playwright provides reliable text assertions  
✔ Dynamic UI validation is a common automation interview topic  

---
---

# UI Testing Playground – Click (Handling Real User Click Events)

In web automation testing, there is an important distinction between:

- **DOM click events**
- **real user interactions**

Some web applications are designed to **ignore synthetic DOM click events** and only respond to **real user actions**.

This can cause automation scripts to fail when using tools that trigger only DOM-level events.

The **UI Testing Playground Click scenario** demonstrates this behavior.

Website:

```
http://uitestingplayground.com/click
```

In this example, clicking the primary button triggers a UI update only when the click is recognized as a **real user interaction**.

---

# Example Test: Triggering Real Click Events

```python
from playwright.sync_api import Page, expect


def test_click_triggers_ui_change(page: Page):

    page.goto("http://uitestingplayground.com/")

    # Navigate to Click example
    click_example_link = page.get_by_role("link", name="Click")
    click_example_link.click()

    # Locate button that ignores DOM click
    primary_button = page.locator("button.btn-primary")

    # Click the button
    primary_button.click()

    # Verify new button appears
    success_button = page.locator("button.btn-success")

    expect(success_button).to_be_visible()
```

---

# What This Test Demonstrates

This test verifies that clicking the primary button **triggers a UI update**.

Steps performed:

1. Open the **UI Testing Playground homepage**
2. Navigate to the **Click example**
3. Click the primary button
4. Verify that a new success button appears

---

# Understanding the Click Behavior

Initial UI:

```
[Button That Ignores DOM Click Event]
```

After clicking:

```
[Button That Ignores DOM Click Event]
[Success Button Appears]
```

The appearance of the **success button** confirms that the click interaction worked correctly.

---

# Why DOM Click vs User Click Matters

Some automation frameworks trigger only **DOM click events**.

Example JavaScript:

```
element.click()
```

However, modern web applications sometimes require **actual user interaction events**, such as:

- mouse down
- mouse up
- pointer events
- focus events

Playwright simulates **real user interactions**, which helps avoid these issues.

---

# Playwright Click Advantages

Playwright's click behavior includes:

✔ scrolling element into view  
✔ waiting for element to be visible  
✔ verifying element is not covered  
✔ triggering real browser events  

This makes Playwright more reliable than traditional automation approaches.

---

# Locating the Buttons

Primary button locator:

```python
primary_button = page.locator("button.btn-primary")
```

Success button locator:

```python
success_button = page.locator("button.btn-success")
```

---

# Verifying the Result

The test confirms the success button appears.

```python
expect(success_button).to_be_visible()
```

This ensures the click interaction triggered the expected UI change.

---

# Running the Test

Run the test with Pytest:

```bash
pytest test_click_event.py
```

Example output:

```
collected 1 item

test_click_event.py .           [100%]

1 passed
```

---

# Why This Scenario Is Important

Some applications intentionally prevent automation by ignoring synthetic DOM clicks.

Automation engineers must understand how to:

- simulate real user interactions
- trigger proper browser events
- verify UI responses

This scenario helps demonstrate those skills.

---

# Best Practices for Click Interactions

When automating click behavior:

✔ use Playwright's built-in `click()` method  
✔ avoid manual JavaScript clicks when possible  
✔ ensure the element is visible before clicking  
✔ verify UI changes after interaction  

---

# Key Takeaways

✔ Some applications ignore synthetic DOM click events  
✔ Playwright simulates real user interactions  
✔ Proper click handling ensures reliable UI automation  
✔ Automation tests should verify UI changes after clicking  

---
---

# UI Testing Playground – Visibility (Understanding Different Hidden Element States)

In web automation testing, elements can become **hidden or inaccessible in multiple ways**.

Automation engineers must understand the difference between these states because they affect whether an element can be interacted with.

The **UI Testing Playground Visibility scenario** demonstrates several techniques used by web applications to hide elements.

Website:

```
http://uitestingplayground.com/visibility
```

After clicking the **Hide button**, several elements become hidden using different CSS and DOM techniques.

---

# Example Test: Validating Different Visibility States

```python
from playwright.sync_api import Page, expect, TimeoutError
import pytest


def test_visibility_states(page: Page):

    page.goto("http://uitestingplayground.com/")

    visibility_link = page.get_by_role("link", name="Visibility")
    visibility_link.click()

    hide_button = page.get_by_role("button", name="Hide")

    removed_button = page.get_by_role("button", name="Removed")
    zero_width_button = page.get_by_role("button", name="Zero Width")
    overlapped_button = page.get_by_role("button", name="Overlapped")
    opacity_button = page.get_by_role("button", name="Opacity 0")
    visibility_hidden_button = page.get_by_role("button", name="Visibility Hidden")
    display_none_button = page.get_by_role("button", name="Display None")
    offscreen_button = page.get_by_role("button", name="Offscreen")

    hide_button.click()

    expect(removed_button).to_be_hidden()

    expect(zero_width_button).to_have_css("width", "0px")

    with pytest.raises(TimeoutError):
        overlapped_button.click(timeout=2000)

    expect(opacity_button).to_have_css("opacity", "0")

    expect(visibility_hidden_button).to_be_hidden()

    expect(offscreen_button).not_to_be_in_viewport()
```

---

# What This Test Demonstrates

This test verifies multiple ways that UI elements can become hidden or inaccessible.

Steps performed:

1. Navigate to UI Testing Playground
2. Open the **Visibility page**
3. Click the **Hide button**
4. Verify different elements become hidden using different methods

---

# Different Visibility States in Web Applications

After clicking **Hide**, elements are hidden using various CSS and DOM techniques.

These techniques simulate real-world UI behaviors.

---

# Removed Element

The element is completely removed from the DOM.

Assertion:

```python
expect(removed_button).to_be_hidden()
```

This confirms the element no longer appears on the page.

---

# Zero Width Element

The element remains in the DOM but has a width of `0px`.

Assertion:

```python
expect(zero_width_button).to_have_css("width", "0px")
```

The element technically exists but cannot be interacted with.

---

# Overlapped Element

Another element covers the button, preventing clicks.

Example error:

```
Element is not clickable because another element receives the click
```

Test validation:

```python
with pytest.raises(TimeoutError):
    overlapped_button.click(timeout=2000)
```

---

# Opacity 0 Element

The element has:

```
opacity: 0
```

It is still in the DOM but fully transparent.

Assertion:

```python
expect(opacity_button).to_have_css("opacity", "0")
```

---

# Visibility Hidden Element

The element uses:

```
visibility: hidden
```

Assertion:

```python
expect(visibility_hidden_button).to_be_hidden()
```

---

# Display None Element

The element uses:

```
display: none
```

This removes the element from layout rendering.

Playwright detects it as hidden.

---

# Offscreen Element

The element is moved outside the visible viewport.

Assertion:

```python
expect(offscreen_button).not_to_be_in_viewport()
```

This confirms the element exists but is not visible on screen.

---

# Why This Scenario Is Important

Modern web applications hide elements in many different ways.

Automation engineers must understand how to detect these states to prevent test failures.

Common real-world scenarios include:

- modal overlays
- animation transitions
- responsive UI behavior
- hidden menu items

---

# Common Automation Failures

Tests often fail when interacting with hidden elements.

Typical errors include:

```
Element not visible
Element not clickable
Element outside viewport
Timeout exceeded
```

Understanding visibility states helps diagnose these issues.

---

# Running the Test

Run the test with Pytest:

```bash
pytest test_visibility_states.py
```

Example output:

```
collected 1 item

test_visibility_states.py .           [100%]

1 passed
```

---

# Best Practices for Visibility Testing

When testing UI visibility states:

✔ verify elements are visible before interacting  
✔ check CSS properties when debugging UI issues  
✔ detect elements hidden by overlays or animations  
✔ use Playwright visibility assertions  

---

# Key Takeaways

✔ Elements can be hidden in multiple ways in modern web applications  
✔ CSS properties like `opacity`, `display`, and `visibility` affect UI behavior  
✔ Playwright provides assertions for detecting visibility states  
✔ Understanding hidden element behavior is critical for reliable automation testing  

---
## UI Testing Playground – Automation Tests (Playwright + Python)

This module demonstrates automated UI testing using **Playwright with Python** against the testing platform:

https://uitestingplayground.com

The goal of this module is to showcase **Page Object Model (POM)** design, reusable automation architecture, and clean separation between **tests and page logic**.

This project is part of a broader **Playwright learning and framework development exercise**.

---

## Test Automation Stack

The following tools and technologies are used:

* Python 3.11+
* Playwright
* Pytest
* Page Object Model (POM)
* Playwright Locators
* Assertions with `expect()`

---

## Test Application

The automation targets the **Sample App login page**:

https://uitestingplayground.com/sampleapp

This application allows testing of:

* Successful login
* Failed login
* UI validation
* Text verification

---

## Implemented Test Scenarios

### 1. Successful Login

**Test Steps**

1. Navigate to Sample App
2. Enter valid username
3. Enter valid password
4. Click **Log In**

**Expected Result**

```
Welcome, <username>!
```

---

### 2. Failed Login

**Test Steps**

1. Navigate to Sample App
2. Enter valid username
3. Enter incorrect password
4. Click **Log In**

**Expected Result**

```
Invalid username/password
```

---

## Page Object Model (POM)

The Page Object Model pattern is used to separate:

* **UI locators**
* **User actions**
* **Test logic**

Benefits include:

* Better maintainability
* Cleaner test code
* Reusable page components
* Easier debugging

---

## Project Structure

```
playwright-python-project
│
├── model
│   ├── __init__.py
│   └── login_page.py
│
├── tests
│   └── test_app.py
│
├── conftest.py
├── pytest.ini
└── README.md
```

---

## Page Object Implementation

### `login_page.py`

```
from playwright.sync_api import Page


class LoginPage:

    URL = "http://uitestingplayground.com/sampleapp"

    def __init__(self, page: Page):
        self.page = page

        self.username_input = page.get_by_placeholder("User Name")
        self.password_input = page.get_by_placeholder("********")
        self.login_btn = page.get_by_role("button", name="Log In")
        self.label = page.locator("#loginstatus")

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()
```

---

## Test Implementation

### `test_app.py`

```
from playwright.sync_api import Page, expect
from model.login_page import LoginPage


def test_successful_login(page: Page):

    username = "test"
    password = "pwd"

    login_page = LoginPage(page)
    login_page.open()

    login_page.login(username, password)

    expect(login_page.label).to_have_text(f"Welcome, {username}!")


def test_failed_login(page: Page):

    username = "test"
    password = "wrongpwd"

    login_page = LoginPage(page)
    login_page.open()

    login_page.login(username, password)

    expect(login_page.label).to_have_text("Invalid username/password")
```

---

## Running the Tests

Install dependencies:

```
pip install playwright pytest
```

Install browser binaries:

```
playwright install
```

Run tests:

```
pytest
```

Run tests in headed mode:

```
pytest --headed
```

---

## Key Automation Concepts Demonstrated

This module demonstrates several important automation practices:

### Page Object Model

Separates test logic from UI interactions.

### Playwright Locators

Uses modern locator strategies such as:

```
get_by_role()
get_by_placeholder()
locator()
```

### Assertions

Assertions use Playwright's built-in **expect API**.

Example:

```
expect(locator).to_have_text()
```

---

## Future Enhancements

Planned improvements for this automation framework include:

* Base page class
* Reusable test fixtures
* Test data management
* Logging utilities
* Screenshot capture on failure
* CI/CD integration with GitHub Actions
* Allure reporting

---

## Learning Objective

This module helps build practical experience with:

* Playwright automation
* Python test frameworks
* Page Object Model design
* UI testing best practices

These skills are essential for **Automation QA Engineers and SDET roles**.

## Playwright Documentation Site – Automation Tests (POM Example)

This module demonstrates UI automation against the official Playwright documentation website:

https://playwright.dev/python

The goal of this test module is to practice **browser interaction, navigation, and search functionality** while implementing the **Page Object Model (POM)** pattern.

This example also highlights how Playwright handles:

* keyboard shortcuts
* dynamic search components
* locator-based assertions

---

## Test Scenarios Implemented

### 1. Navigate to Documentation

**Test Steps**

1. Open Playwright documentation homepage
2. Click the **Docs** navigation link

**Expected Result**

The documentation page loads successfully.

---

### 2. Search Documentation

**Test Steps**

1. Open Playwright documentation
2. Trigger documentation search
3. Enter search term **"assertions"**

**Expected Result**

Search dropdown displays results related to assertions.

Example expected content:

```text
List of assertions
```

---

## Page Object Model Implementation

The Playwright documentation interactions are encapsulated in a dedicated page object.

### `playwright_page.py`

```python
from playwright.sync_api import Page, Locator


class PlaywrightPage:

    URL = "https://playwright.dev/python"

    def __init__(self, page: Page):
        self.page = page

        self.docs_link = page.get_by_role("link", name="Docs")
        self.search_input = page.get_by_placeholder("Search docs")

    def open(self):
        self.page.goto(self.URL)

    def visit_docs(self):
        self.docs_link.click()

    def search(self, query: str):
        self.page.keyboard.press("Control+KeyK")
        self.search_input.fill(query)

    def search_results(self) -> Locator:
        return self.page.locator("div.DocSearch-Dropdown")
```

---

## Test Implementation

### `test_docs.py`

```python
from playwright.sync_api import Page, expect
from model.playwright_page import PlaywrightPage


def test_docs_link(page: Page):

    pw = PlaywrightPage(page)

    pw.open()
    pw.visit_docs()

    expect(page).to_have_url("https://playwright.dev/python/docs/intro")


def test_docs_search(page: Page):

    pw = PlaywrightPage(page)

    pw.open()
    pw.search("assertions")

    expect(pw.search_results()).to_contain_text("List of assertions")
```

---

## Project Structure (Including Docs Tests)

```text
playwright-python-project
│
├── model
│   ├── __init__.py
│   ├── login_page.py
│   └── playwright_page.py
│
├── tests
│   ├── test_app.py
│   └── test_docs.py
│
├── conftest.py
├── pytest.ini
└── README.md
```

---

## Automation Concepts Demonstrated

This module demonstrates several important Playwright automation capabilities.

### Keyboard Interaction

Triggering search using keyboard shortcuts:

```python
page.keyboard.press("Control+KeyK")
```

---

### Dynamic Component Testing

The search dropdown is dynamically rendered, so the test verifies its contents using a locator:

```python
expect(locator).to_contain_text()
```

---

### Role-Based Locators

Playwright allows semantic UI targeting using roles.

Example:

```python
page.get_by_role("link", name="Docs")
```

This approach improves **test readability and resilience**.

---

## Skills Demonstrated

Through this module the project demonstrates:

* Playwright browser automation
* Python-based test architecture
* Page Object Model design
* Dynamic UI testing
* Keyboard event automation
* Locator-based assertions

These patterns are commonly used in **modern UI automation frameworks** built by **SDET engineers**.
## Network Interception and Request/Response Handling with Playwright

This section demonstrates how Playwright can monitor, intercept, and modify network traffic during automated UI testing. Modern web applications rely heavily on APIs and asynchronous network calls, so having control over requests and responses is an essential capability for reliable test automation.

Playwright provides several powerful tools for this:

- Network event listeners
- Route handlers
- Request modification
- Response mocking
- Request blocking
- Request redirection

These capabilities allow automation engineers to simulate different backend behaviors and test complex scenarios without changing the application itself.

---

## Capturing Network Requests

Playwright allows tests to listen for outgoing HTTP requests using the `page.on("request")` event.

Example:

```python
def on_request(request: Request):
    print("Request made:")
    print("URL:", request.url)
    print("Method:", request.method)
    print("Headers:", request.headers)
```

This event listener captures every request the browser sends.

---

## Capturing Network Responses

Playwright also provides the `page.on("response")` event for listening to incoming server responses.

Example:

```python
def on_response(response: Response):
    print("Response received:")
    print("URL:", response.url)
    print("Status:", response.status)
    print("Content-Type:", response.headers.get("content-type"))
```

This allows tests to inspect response status codes and headers.

---

## Route Handlers for Network Interception

Route handlers allow tests to intercept network requests before they reach the server.

Example:

```python
page.route("**/*", on_route)
```

The double star (`**`) is a wildcard pattern that matches any number of path segments in a URL.

Route handlers can:

- block requests
- modify request headers
- mock responses
- redirect requests

---

## Blocking Resource Requests

Large resources such as images can slow down automated tests. Playwright allows these requests to be blocked.

Example:

```python
if request.resource_type == "image":
    route.abort()
```

Blocking images improves test speed and reduces unnecessary network traffic.

---

## Modifying Request Headers

Route handlers can modify outgoing requests before they are sent to the server.

Example:

```python
headers = request.headers.copy()
headers["X-Test-Automation"] = "Playwright-Python"

route.continue_(headers=headers)
```

This technique is useful for:

- injecting custom headers
- enabling feature flags
- simulating authenticated requests

---

## Mocking API Responses

Playwright can replace the server's response entirely with a mocked response.

Example:

```python
route.fulfill(
    status=200,
    content_type="application/json",
    body='{"message":"Mocked API response from Playwright"}'
)
```

Mocking responses is useful when:

- backend services are unavailable
- testing frontend behavior independently
- simulating error conditions

---

## Redirecting Network Requests

Requests can also be redirected to different endpoints.

Example:

```python
route.continue_(
    url="https://playwright.dev/python/docs/intro"
)
```

This allows tests to simulate:

- changed endpoints
- fallback services
- alternative resources

---

## Example Test: Network Interception

The following test demonstrates how to combine request monitoring, response monitoring, and route interception.

```python
from playwright.sync_api import Page, expect, Request, Response, Route


def on_request(request: Request):
    print("Request made:", request.url)


def on_response(response: Response):
    print("Response received:", response.status)


def on_route(route: Route):

    request = route.request

    if request.resource_type == "image":
        route.abort()
        return

    route.continue_()


def test_docs_link(page: Page):

    page.on("request", on_request)
    page.on("response", on_response)

    page.route("**/*", on_route)

    page.goto("https://playwright.dev/python")

    docs_link = page.get_by_role("link", name="Docs")
    docs_link.click()

    expect(page).to_have_url("https://playwright.dev/python/docs/intro")
```

---

## Key Playwright Networking Concepts

This section demonstrates several important Playwright networking capabilities:

- Listening to network requests
- Monitoring server responses
- Intercepting HTTP traffic
- Blocking unwanted resources
- Modifying request headers
- Mocking backend responses
- Redirecting network requests

These techniques allow automation engineers to create **more reliable and controlled UI tests** by managing network behavior directly within the test framework.
---

## Modifying HTTP Responses with Playwright

Playwright allows tests to intercept HTTP responses and modify their content before the browser receives them. This technique is useful for testing UI behavior under different backend responses without changing the server.

Typical use cases include:

- modifying HTML content dynamically
- simulating different UI states
- testing error handling
- mocking server responses

To modify a response, Playwright provides two important methods:

- `route.fetch()` – retrieves the original response from the server
- `route.fulfill()` – sends a modified response back to the browser

The typical workflow follows this pattern:

```
fetch → modify → fulfill
```

---

## Steps to Modify a Response

1. Intercept the request using `page.route()`.
2. Fetch the original server response using `route.fetch()`.
3. Extract the response body.
4. Modify the response content.
5. Return the modified response using `route.fulfill()`.

---

## Example: Modifying an HTML Heading

The following example intercepts a request to the UI Testing Playground sample app and modifies the `<h1>` heading before the page renders.

Original HTML:

```html
<h1>Welcome</h1>
```

Modified HTML:

```html
<h1>Welcome Automation Engineer</h1>
```

---

## Test Implementation

```python
from playwright.sync_api import Page, Route


def modify_response(route: Route):

    # Step 1: fetch original response
    response = route.fetch()

    # Step 2: read response body
    html = response.text()

    # Step 3: modify HTML
    modified_html = html.replace(
        "<h1>Welcome</h1>",
        "<h1>Welcome Automation Engineer</h1>"
    )

    # Step 4: send modified response
    route.fulfill(
        response=response,
        body=modified_html
    )


def test_modify_heading(page: Page):

    page.route("**/sampleapp", modify_response)

    page.goto("http://uitestingplayground.com/sampleapp")
```

---

## Explanation of Key Methods

### `route.fetch()`

This method sends the intercepted request to the server and retrieves the original response.

Example:

```python
response = route.fetch()
```

It allows the test to inspect or modify the server response before the browser receives it.

---

### `route.fulfill()`

This method sends a custom response back to the browser.

Example:

```python
route.fulfill(
    response=response,
    body=modified_html
)
```

It can modify:

- response body
- status code
- headers
- content type

---

## Request Flow When Modifying Responses

```
Browser requests page
        ↓
Playwright intercepts request
        ↓
route.fetch() retrieves original server response
        ↓
Test modifies response content
        ↓
route.fulfill() returns modified response
        ↓
Browser renders modified page
```

---

## Benefits of Response Modification

Response interception provides several advantages in test automation:

- simulate backend conditions without changing the server
- test UI behavior under different responses
- reproduce rare edge cases
- isolate frontend testing from backend dependencies

These capabilities make Playwright particularly powerful for **advanced UI and full-stack testing scenarios**.
---

## Modifying POST Request Data with Playwright

In addition to modifying responses, Playwright also allows tests to intercept and modify **outgoing HTTP requests**, including POST requests.

This is useful for testing scenarios such as:

- altering form submission data
- testing validation rules
- simulating invalid user input
- injecting test parameters
- security and edge-case testing

When intercepting POST requests, Playwright provides access to the request body through the `request` object.

Common properties used:

- `request.method`
- `request.post_data`
- `request.post_data_json`

To modify a request, the test intercepts the request and forwards a modified version using:

```
route.continue_()
```

---

## Accessing POST Request Data

POST data is usually sent as a string. For example:

```
username=test&password=123
```

You can access the raw POST body using:

```python
request.post_data
```

Example:

```python
from playwright.sync_api import Route

def modify_post_request(route: Route):

    request = route.request

    if request.method == "POST":

        body = request.post_data
        print("Original POST data:", body)

        modified_body = body.replace("username=test", "username=automation_user")

        route.continue_(post_data=modified_body)

    else:
        route.continue_()
```

---

## Modifying JSON POST Data

If the request body is JSON (`application/json`), Playwright provides a helper property:

```python
request.post_data_json
```

Example:

```python
import json
from playwright.sync_api import Route

def modify_json_post(route: Route):

    request = route.request

    if request.method == "POST":

        data = request.post_data_json

        data["username"] = "qa_engineer"

        modified_body = json.dumps(data)

        route.continue_(post_data=modified_body)

    else:
        route.continue_()
```

---

## Request Flow When Modifying POST Data

```
Browser submits POST request
        ↓
Playwright intercepts request
        ↓
Test reads request.post_data
        ↓
Test modifies request body
        ↓
route.continue_(post_data=modified_body)
        ↓
Server receives modified request
```

---

## Key Methods and Properties

| Method / Property | Purpose |
|------------------|--------|
| `page.route()` | Intercepts network requests |
| `route.request` | Access the intercepted request |
| `request.post_data` | Retrieve raw POST body |
| `request.post_data_json` | Retrieve JSON POST body |
| `route.continue_()` | Send modified request to server |

---

## Why Modify POST Requests?

Modifying POST data allows automation engineers to test complex scenarios such as:

- invalid form submissions
- security edge cases
- backend validation behavior
- API contract testing
- unexpected input handling

This technique is commonly used in **advanced automation frameworks and security testing workflows**.
---

## Understanding `route.fetch()` vs `route.fulfill()`

When modifying HTTP responses in Playwright, two important methods are commonly used:

- `route.fetch()`
- `route.fulfill()`

These methods serve different purposes but are often used together when intercepting and modifying responses.

---

### `route.fetch()`

`route.fetch()` sends the intercepted request to the server and retrieves the original response.

Example:

```python
response = route.fetch()
```

This allows the test to:

- obtain the original server response
- inspect response headers
- inspect response body
- inspect response status codes

Example usage:

```python
response = route.fetch()
html = response.text()
```

This step retrieves the original HTML page before modification.

---

### `route.fulfill()`

`route.fulfill()` sends a response back to the browser.

Example:

```python
route.fulfill(
    status=200,
    body="Custom response"
)
```

This allows the test to return:

- modified responses
- mocked API responses
- custom HTTP status codes
- modified headers

---

### Typical Response Modification Pattern

Most response modification workflows follow this pattern:

```
route.fetch() → modify response → route.fulfill()
```

Example:

```python
response = route.fetch()

html = response.text()

modified_html = html.replace("Welcome", "Welcome Automation Engineer")

route.fulfill(
    response=response,
    body=modified_html
)
```

---

### Comparison Table

| Method | Purpose |
|------|------|
| `route.fetch()` | Retrieve the original response from the server |
| `route.fulfill()` | Send a custom or modified response to the browser |

---

### When to Use Each Method

Use `route.fetch()` when you want to:

- keep the original server response
- inspect response data
- modify only part of the response

Use `route.fulfill()` when you want to:

- mock responses
- simulate API behavior
- send custom responses to the browser

---

## API Testing with Playwright (`APIRequestContext`)

Playwright is not limited to UI automation. It also provides powerful API testing capabilities through the `APIRequestContext`.

This allows tests to send HTTP requests directly without opening a browser.

Benefits of Playwright API testing include:

- faster execution
- backend validation
- API contract testing
- integration testing
- combining UI and API tests

---

### Creating an API Request Context

An API request context can be created using the Playwright `request` object.

Example:

```python
import pytest
from playwright.sync_api import Playwright, APIRequestContext


@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:

    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com"
    )

    yield api_context

    api_context.dispose()
```

This fixture creates a reusable API client for tests.

---

### Example API Test

The following example sends a search request to the DummyJSON API.

```python
def test_users_search(api_context: APIRequestContext):

    query = "John"

    response = api_context.get(
        "/users/search",
        params={"q": query}
    )

    assert response.status == 200

    users_data = response.json()

    print("Users found:", users_data["total"])

    for user in users_data["users"]:
        print("Checking user:", user["firstName"])
```

---

### Validating API Responses

Playwright allows easy validation of responses:

```python
assert response.status == 200
```

Access JSON data:

```python
data = response.json()
```

Example response structure:

```
{
  "users": [],
  "total": 3,
  "skip": 0,
  "limit": 30
}
```

---

### Why Combine API and UI Testing?

Combining UI and API testing provides several advantages:

- verify backend functionality independently
- reduce UI test complexity
- validate API responses before UI rendering
- speed up test execution

Many modern test frameworks combine **UI tests and API tests within the same Playwright test suite**.

---

## Summary

In this section we covered several advanced Playwright capabilities:

- Network request monitoring
- Network response monitoring
- Request interception
- Blocking resource requests
- Modifying HTTP requests
- Modifying HTTP responses
- Mocking API responses
- API testing using `APIRequestContext`

These techniques allow automation engineers to build **robust, reliable, and flexible test automation frameworks** capable of testing both frontend and backend systems.
---

## Basic API Validation Using Playwright

Playwright can also be used to validate API responses while running UI tests. Since modern web applications rely heavily on APIs, verifying backend responses is an important part of test automation.

In this example, we send a request to the **DummyJSON API** and validate the returned user data.

API endpoint used:

```
https://dummyjson.com/users/1
```

This endpoint returns information about a specific user.

---

## Example Test: Validate API Response Data

The following test sends a request to retrieve user information and verifies that the expected fields exist in the response.

```python
from playwright.sync_api import *
import json


def test_users_api(page: Page):

    response = page.goto("https://dummyjson.com/users/1")

    user_data = response.json()

    print(user_data)

    assert "firstName" in user_data
    assert "lastName" in user_data

    assert user_data["firstName"] == "Emily"
    assert user_data["lastName"] == "Johnson"
```

---

## Explanation of the Test

### Sending the Request

The test navigates to the API endpoint using:

```python
response = page.goto("https://dummyjson.com/users/1")
```

This returns a response object containing the server response.

---

### Reading JSON Response Data

The JSON body is extracted using:

```python
user_data = response.json()
```

This converts the response into a Python dictionary.

---

### Validating Response Fields

The test verifies that required fields exist in the response.

```python
assert "firstName" in user_data
assert "lastName" in user_data
```

---

### Validating Field Values

The test also confirms the expected values for the user.

```python
assert user_data["firstName"] == "Emily"
assert user_data["lastName"] == "Johnson"
```

---

## Example API Response

Example response returned by the DummyJSON API:

```
{
  "id": 1,
  "firstName": "Emily",
  "lastName": "Johnson",
  "email": "emily.johnson@x.dummyjson.com",
  "age": 28
}
```

---

## Why Validate API Responses?

Validating API responses helps ensure:

- backend services return expected data
- APIs follow the expected contract
- UI tests rely on correct backend data
- integration between frontend and backend works correctly

Many automation frameworks combine **UI tests and API validations** within the same test suite to improve reliability and coverage.
---

## API Testing Using Playwright `APIRequestContext`

Playwright provides a powerful API testing capability through `APIRequestContext`.  
This allows tests to send HTTP requests directly to backend services without opening a browser.

API testing is useful for:

- validating backend responses
- testing REST APIs
- verifying API contracts
- speeding up tests by bypassing the UI
- combining API and UI tests within the same framework

---

## Creating an API Request Context

Playwright allows tests to create an API client using:

```python
playwright.request.new_context()
```

This creates a reusable HTTP client for sending API requests.

Example:

```python
api_context = playwright.request.new_context(
    base_url="https://dummyjson.com"
)
```

Setting a `base_url` simplifies API calls by allowing relative endpoints.

---

## Example API Test

The following test sends a GET request to retrieve user data and validates the response.

```python
from playwright.sync_api import *
import json


def test_users_api(playwright: Playwright):

    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com"
    )

    response = api_context.get("/users/1")

    user_data = response.json()

    print(user_data)

    assert "firstName" in user_data
    assert "lastName" in user_data

    assert user_data["firstName"] == "Emily"
    assert user_data["lastName"] == "Johnson"
```

---

## Explanation of the Test

### Creating the API Client

The test starts by creating an API request context.

```python
api_context = playwright.request.new_context(
    base_url="https://dummyjson.com"
)
```

This allows all requests to be sent relative to the base URL.

---

### Sending a GET Request

The test retrieves user data using:

```python
response = api_context.get("/users/1")
```

This sends an HTTP GET request to:

```
https://dummyjson.com/users/1
```

---

### Parsing the JSON Response

The JSON response is converted into a Python dictionary using:

```python
user_data = response.json()
```

---

### Validating Response Data

The test verifies both the existence of fields and their values.

```python
assert "firstName" in user_data
assert "lastName" in user_data
```

Then it confirms the expected user values.

```python
assert user_data["firstName"] == "Emily"
assert user_data["lastName"] == "Johnson"
```

---

## Example API Response

Example response returned by the DummyJSON API:

```
{
  "id": 1,
  "firstName": "Emily",
  "lastName": "Johnson",
  "email": "emily.johnson@x.dummyjson.com",
  "age": 28
}
```

---

## Benefits of API Testing with Playwright

Using `APIRequestContext` provides several advantages:

- faster execution compared to UI tests
- ability to validate backend services directly
- easy integration with existing Playwright test frameworks
- ability to combine API and UI validations in the same test suite

Many modern automation frameworks use **Playwright for both UI testing and API testing** within a unified testing strategy.
---

## API Search Testing Using Playwright and Pytest Fixtures

In addition to simple API validation, Playwright can also test **search endpoints and query parameters**.  
This example demonstrates how to use **Pytest fixtures together with Playwright's `APIRequestContext`** to test a search API.

The test sends a query request to the DummyJSON API and verifies that the returned results contain the expected search term.

API endpoint used:

```
https://dummyjson.com/users/search?q=John
```

---

## Creating a Reusable API Fixture

Pytest fixtures allow tests to reuse setup logic such as creating an API client.

Example:

```python
import pytest
from playwright.sync_api import Playwright, APIRequestContext


@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:

    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com"
    )

    yield api_context

    api_context.dispose()
```

This fixture creates a reusable API request context that can be used across multiple tests.

---

## Example Test: Search Users API

The following test searches for users containing the term **"John"** and validates the results.

```python
from playwright.sync_api import *
import pytest


@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:

    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com"
    )

    yield api_context

    api_context.dispose()


def test_users_search(api_context: APIRequestContext):

    query = "John"

    response = api_context.get(f"/users/search?q={query}")

    assert response.status == 200

    users_data = response.json()

    print("Users found:", users_data["total"])

    for user in users_data["users"]:

        print("Checking user:", user["firstName"], user["lastName"])

        full_text = (
            user["firstName"]
            + user["lastName"]
            + user["maidenName"]
            + user["email"]
            + user["username"]
        ).lower()

        assert query.lower() in full_text
```

---

## Explanation of the Test

### Sending a Search Request

The test sends a GET request with a query parameter:

```python
response = api_context.get(f"/users/search?q={query}")
```

This sends a request to:

```
https://dummyjson.com/users/search?q=John
```

---

### Validating Response Status

The test first verifies the request was successful.

```python
assert response.status == 200
```

---

### Parsing the JSON Response

The JSON response is converted into a Python dictionary:

```python
users_data = response.json()
```

The response contains:

```
{
  "users": [],
  "total": 3,
  "skip": 0,
  "limit": 30
}
```

---

### Validating Search Results

The test checks that the search query appears somewhere in the user's information.

```python
full_text = (
    user["firstName"]
    + user["lastName"]
    + user["maidenName"]
    + user["email"]
    + user["username"]
).lower()

assert query.lower() in full_text
```

This ensures the query is present in at least one of the searchable fields.

---

## Why Test Search APIs?

Testing search APIs helps ensure:

- query parameters work correctly
- APIs return relevant results
- search functionality behaves as expected
- backend search logic is functioning properly

Search endpoints are common in applications such as:

- e-commerce platforms
- user management systems
- product catalogs
- content management systems