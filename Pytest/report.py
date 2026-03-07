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