from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import path
import base64, os

base_path = 'https://demo.docusign.net/restapi'

signer_email = 'budget.me.hackathon@gmail.com' #borrower
signer_name = 'Bob'
signer_client_id = 'c41a6535-7f9c-43a1-846b-8eae2504e4eb'

signer2_email = 'kevinamehta@hotmail.com' #creditor
signer2_name = 'Kevin'
signer2_client_id = '45c73045-6a34-4c02-86dc-4e2ce199322a'
file_name_path = '/Users/kebin/Documents/Personal Projects/BudgetMe/demo_documents/World_Wide_Corp_lorem.pdf'

ds_acess_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjY4MTg1ZmYxLTRlNTEtNGNlOS1hZjFjLTY4OTgxMjIwMzMxNyJ9.eyJUb2tlblR5cGUiOjUsIklzc3VlSW5zdGFudCI6MTU3MDcxMjEzNCwiZXhwIjoxNTcwNzQwOTM0LCJVc2VySWQiOiI2MjgwNGZhNC01ZmU1LTRlZmItODYwYS05NzMyNTE3OTgxMWEiLCJzaXRlaWQiOjEsInNjcCI6WyJzaWduYXR1cmUiLCJjbGljay5tYW5hZ2UiLCJvcmdhbml6YXRpb25fcmVhZCIsImdyb3VwX3JlYWQiLCJwZXJtaXNzaW9uX3JlYWQiLCJ1c2VyX3JlYWQiLCJ1c2VyX3dyaXRlIiwiYWNjb3VudF9yZWFkIiwiZG9tYWluX3JlYWQiLCJpZGVudGl0eV9wcm92aWRlcl9yZWFkIiwiZHRyLnJvb21zLnJlYWQiLCJkdHIucm9vbXMud3JpdGUiLCJkdHIuZG9jdW1lbnRzLnJlYWQiLCJkdHIuZG9jdW1lbnRzLndyaXRlIiwiZHRyLnByb2ZpbGUucmVhZCIsImR0ci5wcm9maWxlLndyaXRlIiwiZHRyLmNvbXBhbnkucmVhZCIsImR0ci5jb21wYW55LndyaXRlIl0sImF1ZCI6ImYwZjI3ZjBlLTg1N2QtNGE3MS1hNGRhLTMyY2VjYWUzYTk3OCIsImlzcyI6Imh0dHBzOi8vYWNjb3VudC1kLmRvY3VzaWduLmNvbS8iLCJzdWIiOiI2MjgwNGZhNC01ZmU1LTRlZmItODYwYS05NzMyNTE3OTgxMWEiLCJhdXRoX3RpbWUiOjE1NzA3MDE1MzIsInB3aWQiOiI1MmJhM2ZhZC04MWJlLTQ5ODktYTZkZi01OGQ2MmRhNWIwYWMifQ.JbSt6b1pGVKLYjVCpXXvvtYIscO5vSmoiNgvPU7lnpwuylBW23ZLmUMNW1-ZWjcKj86DX-59s7Zuu9gXN_yGwGO8EDUzNb3I2PHa4FvsfrIqqRTaLJ1gBC0DKURWbV9O06WLSd-Y4AC8U8PFnQqU2lotgQg4Dj6oJYV3KxV4KNT86c76X0lYpGeqVNjP4W9ZCRBVKN7WP3vgwuqmTGeZ_JWT0X_0kDshtjhhZZbQHN1wEQBaaXV1sRY9ochZAa2ncV4FxH2rZnDR4REzANEzVy1thwwsvGTU6cJcaqx38gRPP-ibP0HZplPJczaPfb68Bho7ouVR4q0588dmYMLDzw'

ds_return_url = 'https://www.google.com'

# Settings
# Fill in these constants
#
# Obtain your accountId from demo.docusign.com -- the account id is shown in the drop down on the
# upper right corner of the screen by your picture or the default picture.
account_id = '9114215'
# Recipient Information:
signer_name = 'John Signer'
signer_email = 'budget.me.hackathon@gmail.com'
# The document you wish to send. Path is relative to the root directory of this repo.
file_name_path = 'demo_documents/World_Wide_Corp_lorem.pdf'
# The url of this web application
base_url = 'http://localhost:8000'
client_user_id = '123' # Used to indicate that the signer will use an embedded
                       # Signing Ceremony. Represents the signer's userId within
                       # your application.
authentication_method = 'None' # How is this application authenticating
                               # the signer? See the `authenticationMethod' definition
                               # https://developers.docusign.com/esign-rest-api/reference/Envelopes/EnvelopeViews/createRecipient

# The API base_path
base_path = 'https://demo.docusign.net/restapi'

# Set FLASK_ENV to development if it is not already set

# Constants
APP_PATH = os.path.dirname(os.path.abspath(__file__))
def docusign(response):
    """
    The document <file_name> will be signed by <signer_name> via an
    embedded signing ceremony.
    """

    #
    # Step 1. The envelope definition is created.
    #         One signHere tab is added.
    #         The document path supplied is relative to the working directory
    #
    # Create the component objects for the envelope definition...
    with open(os.path.join(APP_PATH, file_name_path), "rb") as file:
        content_bytes = file.read()
    base64_file_content = base64.b64encode(content_bytes).decode('ascii')

    document = Document( # create the DocuSign document object
        document_base64 = base64_file_content,
        name = 'Example document', # can be different from actual file name
        file_extension = 'pdf', # many different document types are accepted
        document_id = 1 # a label used to reference the doc
    )

    # Create the signer recipient model
    signer = Signer( # The signer
        email = signer_email, name = signer_name, recipient_id = "1", routing_order = "1",
        client_user_id = client_user_id, # Setting the client_user_id marks the signer as embedded
    )

    sign_here = SignHere( # DocuSign SignHere field/tab
        document_id = '1', page_number = '1', recipient_id = '1', tab_label = 'SignHereTab',
        x_position = '195', y_position = '147')

    # Add the tabs model (including the sign_here tab) to the signer
    signer.tabs = Tabs(sign_here_tabs = [sign_here]) # The Tabs object wants arrays of the different field/tab types

    # Next, create the top level envelope definition and populate it.
    envelope_definition = EnvelopeDefinition(
        email_subject = "Please sign this document sent from the Python SDK",
        documents = [document], # The order in the docs array determines the order in the envelope
        recipients = Recipients(signers = [signer]), # The Recipients object wants arrays for each recipient type
        status = "sent" # requests that the envelope be created and sent.
    )
 #
    #  Step 2. Create/send the envelope.
    #
    api_client = ApiClient()
    api_client.host = base_path
    api_client.set_default_header("Authorization", "Bearer " + access_token)

    envelope_api = EnvelopesApi(api_client)
    results = envelope_api.create_envelope(account_id, envelope_definition=envelope_definition)

    #
    # Step 3. The envelope has been created.
    #         Request a Recipient View URL (the Signing Ceremony URL)
    #
    envelope_id = results.envelope_id
    recipient_view_request = RecipientViewRequest(
        authentication_method = authentication_method, client_user_id = client_user_id,
        recipient_id = '1', return_url = base_url + '/dsreturn',
        user_name = signer_name, email = signer_email
    )

    results = envelope_api.create_recipient_view(account_id, envelope_id,
        recipient_view_request = recipient_view_request)

    #
    # Step 4. The Recipient View URL (the Signing Ceremony URL) has been received.
    #         Redirect the user's browser to it.
    #
    return results.url
