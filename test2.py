# Python3 Quick start example: list envelopes in the user's account
# Copyright (c) 2018 by DocuSign, Inc.
# License: The MIT License -- https://opensource.org/licenses/MIT

import base64, os
from docusign_esign import ApiClient, EnvelopesApi
import pendulum # pip install pendulum
import pprint

# Settings
# Fill in these constants
#
# Obtain an OAuth access token from https://developers.docusign.com/oauth-token-generator
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjY4MTg1ZmYxLTRlNTEtNGNlOS1hZjFjLTY4OTgxMjIwMzMxNyJ9.eyJUb2tlblR5cGUiOjUsIklzc3VlSW5zdGFudCI6MTU3MDY4MDE3MywiZXhwIjoxNTcwNzA4OTczLCJVc2VySWQiOiI2MjgwNGZhNC01ZmU1LTRlZmItODYwYS05NzMyNTE3OTgxMWEiLCJzaXRlaWQiOjEsInNjcCI6WyJzaWduYXR1cmUiLCJjbGljay5tYW5hZ2UiLCJvcmdhbml6YXRpb25fcmVhZCIsImdyb3VwX3JlYWQiLCJwZXJtaXNzaW9uX3JlYWQiLCJ1c2VyX3JlYWQiLCJ1c2VyX3dyaXRlIiwiYWNjb3VudF9yZWFkIiwiZG9tYWluX3JlYWQiLCJpZGVudGl0eV9wcm92aWRlcl9yZWFkIiwiZHRyLnJvb21zLnJlYWQiLCJkdHIucm9vbXMud3JpdGUiLCJkdHIuZG9jdW1lbnRzLnJlYWQiLCJkdHIuZG9jdW1lbnRzLndyaXRlIiwiZHRyLnByb2ZpbGUucmVhZCIsImR0ci5wcm9maWxlLndyaXRlIiwiZHRyLmNvbXBhbnkucmVhZCIsImR0ci5jb21wYW55LndyaXRlIl0sImF1ZCI6ImYwZjI3ZjBlLTg1N2QtNGE3MS1hNGRhLTMyY2VjYWUzYTk3OCIsImlzcyI6Imh0dHBzOi8vYWNjb3VudC1kLmRvY3VzaWduLmNvbS8iLCJzdWIiOiI2MjgwNGZhNC01ZmU1LTRlZmItODYwYS05NzMyNTE3OTgxMWEiLCJhbXIiOlsiaW50ZXJhY3RpdmUiXSwiYXV0aF90aW1lIjoxNTcwNjgwMTcxLCJwd2lkIjoiNTJiYTNmYWQtODFiZS00OTg5LWE2ZGYtNThkNjJkYTViMGFjIn0.jTky2ehQITVUbbwgkpmtN6TmxOgs14LZgiIE8atXaueoPzndQjWhSXOyWvSXefz1QhIlZNQQcak9SwQtsDSH-frTeYgZxDHXpC2GN_Ex6Tvtvf3QoeuFtl4zy3PsN1qdZF32JlkkvPIxZzlErBrmkKYtKY5iRVDgY86U_3KbANS5G3ndrxxthixzoFy_a41OzJCMjxvozuZrUm30T0gPIqoWXlJ4lo168rqB9BU7dnxTtw18M2582qP-nqYr2Y4RxZHqTaizm-VnHxUJ45INlEFmdG3CTFlIeY8yjbOt12hGOoA2k8SkoK1eu60iGPgx-U34iBrfZz9-oLc9auY3CQ'
# Obtain your accountId from demo.docusign.com -- the account id is shown in the drop down on the
# Obtain your accountId from demo.docusign.com -- the account id is shown in the drop down on the
# upper right corner of the screen by your picture or the default picture.
account_id = '9114215';
base_path = 'https://demo.docusign.net/restapi'

def list_envelopes():
    """
    Lists the user's envelopes created in the last 10 days
    """

    #
    # Step 1. Prepare the options object
    #
    from_date = pendulum.now().subtract(days=10).to_iso8601_string()
    #
    # Step 2. Get and display the results
    #
    api_client = ApiClient()
    api_client.host = base_path
    api_client.set_default_header("Authorization", "Bearer " + access_token)

    envelope_api = EnvelopesApi(api_client)
    results = envelope_api.list_status_changes(account_id, from_date = from_date)
    return results

# Mainline
results = list_envelopes()
print("\nEnvelopes:\n")
pprint.pprint(results, indent=4, width=80)
