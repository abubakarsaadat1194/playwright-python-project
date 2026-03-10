import os
import pytest
import pytest_html
from datetime import datetime


# Create screenshot directory if it doesn't exist
os.makedirs("reports/screenshots", exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        extra = getattr(report, "extra", [])

        page = item.funcargs.get("page", None)

        if page:

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"reports/screenshots/{item.name}_{timestamp}.png"

            page.screenshot(path=screenshot_path)

            extra.append(pytest_html.extras.image(screenshot_path))

        report.extra = extra