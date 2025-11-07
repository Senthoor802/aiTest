# pylint: disable=all
import json
import os
from datetime import datetime

import pandas as pd


def convert_allure_results_to_excel(path):
    """
    Converts Allure JSON results to an Excel file.
    """

    allure_folder = (
        "reports/report_dates/20251103_14-59-12/allure-results"
    )

    data = []

    for file_name in os.listdir(allure_folder):
        if file_name.endswith(".json") and "result" in file_name:
            with open(
                os.path.join(allure_folder, file_name), "r", encoding="utf-8"
            ) as file:
                try:
                    test = json.load(file)
                    full_name = test.get("name", "")

                    parts = full_name.strip().split(" ", 1)
                    test_id = parts[0] if len(parts) > 0 else ""
                    test_name = parts[1] if len(parts) > 1 else ""

                    # Suite name comes from 'labels' with name == 'suite'
                    suite_name = ""
                    for label in test.get("labels", []):
                        if label.get("name") == "feature":
                            suite_name = label.get("value")
                            break

                    data.append(
                        {
                            "Suite Name": suite_name,
                            "Test ID": test_id,
                            "Test Case Name": test_name,
                            "Status": test.get("status", ""),
                            "Error": test.get("statusDetails", {}).get("message", ""),
                        }
                    )
                except AssertionError as e:
                    print(f"Couldn't process {file_name}: {e}")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"allure_report_{timestamp}.csv"
    df = pd.DataFrame(data)
    file = df.to_excel(f"allure_test_report{filename}.xlsx", index=False)
    print("Report generated successfully!")

    return f"allure_test_report{filename}.xlsx"


# convert_allure_results_to_excel("i")
