# pylint: disable=all
import csv
import json
import os
import re
from datetime import datetime, timedelta

import pandas as pd
import pytz
import requests
import win32com.client as win32
from openpyxl import Workbook
from requests.auth import HTTPBasicAuth


def send_email_with_excel(file_path):
    # Authentication credentials
    username = "Suguna.V@cognizant.com"
    password = ""
    # password = os.getenv("JIRA_API_PASSWORD")  # Read the password from an environment variable

    # Create an Outlook application object
    outlook = win32.Dispatch("Outlook.Application")
    new_mail = outlook.CreateItem(0)
    # new_mail.To = "suguna.v@cognizant.com"
    recipients = ["SenthoorSeruvan.D@cognizant.com"]
    new_mail.To = "; ".join(recipients)
    new_mail.Subject = "test"
    # formatted_body = email_body.replace(hyperlink_word, f'<a href="{hyperlink_url}">{hyperlink_word}</a>')
    new_mail.HTMLBody = "test"

    # Attach the original Excel sheet
    attachment_path = file_path
    print("Attaching file:", attachment_path)
    attachment = new_mail.Attachments.Add(Source=attachment_path)

    # Send the email
    new_mail.Send()
    print("Email sent successfully!")
