import requests
import pandas as pd
from requests.auth import HTTPBasicAuth

def export_jira_test_cases(email, api_token, jira_url, project_key, output_file):
    url = f"{jira_url}/rest/api/3/search/jql"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    jql = f'project = {project_key} AND issuetype = "Test Case" AND created >= -30d'
    payload = {
        "queries": [
            {
                "query": jql,
                "maxResults": 100,
                "fields": ["summary", "description"]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload, auth=HTTPBasicAuth(email, api_token))

    if response.status_code == 200:
        all_issues = []
        for result in response.json().get("results", []):
            all_issues.extend(result.get("issues", []))
        records = []
        for issue in all_issues:
            key = issue.get("key")
            fields = issue.get("fields", {})
            summary = fields.get("summary", "")
            description = fields.get("description", "")
            records.append({
                "Issue Key": key,
                "Summary": summary,
                "Description": description
            })

        df = pd.DataFrame(records)
        df.to_excel(output_file, index=False)
        print(f"✅ Exported {len(records)} test cases to {output_file}")
    else:
        print(f"❌ Failed to fetch issues: {response.status_code} - {response.text}")

def export_qmetry_test_cases(email, api_token, jira_url, project_id, output_file):
    url = f"{jira_url}/rest/qtm4j/2.0/testcase/search"
    headers = {
        "Accept": "application/json"
    }
    params = {
        "projectId": project_id,
        "maxResults": 100
    }

    response = requests.get(url, headers=headers, params=params, auth=HTTPBasicAuth(email, api_token))

    if response.status_code == 200:
        testcases = response.json().get("data", [])
        records = []
        for tc in testcases:
            records.append({
                "Test Case Key": tc.get("key"),
                "Summary": tc.get("summary"),
                "Description": tc.get("description")
            })
        df = pd.DataFrame(records)
        df.to_excel(output_file, index=False)
        print(f"✅ Exported {len(records)} QMetry test cases to {output_file}")
    else:
        print(f"❌ Failed to fetch QMetry test cases: {response.status_code} - {response.text}")

export_jira_test_cases(
    email="senthoorseruvan.d@cognizant.com",
    api_token="ATATT3xFfGF0KZj_I8-jrvTQTMkRpm2mu-rdHqzVHEiPbxaygH3yGtg2aLRZjFCiesDuPBnRFogReRAQnJRrC1Wv6y0YgA9WESFviC4gH28FS0hpPN5b4HyrYfmKZzjJg6dAFy5iwqrowXlCq3ljAqJ5SbjUYpEQ0JnSfCUaRrKmSh3PJ2aAKug=128DF491",
    jira_url="https://americold.atlassian.net",
    project_key="AMCC",
    output_file="output.xlsx"
)

export_qmetry_test_cases(
    email="senthoorseruvan.d@cognizant.com",
    api_token="ATATT3xFfGF0KZj_I8-jrvTQTMkRpm2mu-rdHqzVHEiPbxaygH3yGtg2aLRZjFCiesDuPBnRFogReRAQnJRrC1Wv6y0YgA9WESFviC4gH28FS0hpPN5b4HyrYfmKZzjJg6dAFy5iwqrowXlCq3ljAqJ5SbjUYpEQ0JnSfCUaRrKmSh3PJ2aAKug=128DF491",
    jira_url="https://americold.atlassian.net",
    project_id="10524",
    output_file="qmetry_testcases.xlsx"
)