import json
import pytest
import report


@pytest.fixture
def report_json(scope="session"):
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