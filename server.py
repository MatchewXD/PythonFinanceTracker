import plaid
import json
from plaid.api import plaid_api
import plaid.exceptions
from plaid.model.asset_report_get_request import AssetReportGetRequest
from plaid.model.institutions_get_request import InstitutionsGetRequest
from plaid.model.country_code import CountryCode
from plaid_secrets import client_id, secret

PLAID_ENV = 'Sandbox'

configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': client_id,
        'secret': secret,
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

# Error Handling ----------------------------------------------------
# try:
#     request = AssetReportGetRequest(
#         asset_report_token=asset_report_token,
#     )
#     return client.asset_report_get(request)
# except plaid.ApiException as e:
#     response = json.loads(e.body)
#     if response['error_code'] == 'ITEM_LOGIN_REQUESTED':
# -------------------------------------------------------------------


# Creating a Link Token ---------------------------------------------
def create_link_token():
    try:
        request = LinkTokenCreateRequest(
            user = LinkTokenCreateRequestUser(
                client_user_id = 'unique_user_id'
            )
            client_name = 'Flow Grapher',
            products = ['transactions'],
            country_codes = ['US'],
            language = 'en',
            webhook = 'https://your-webhook-url.com'
        )

        response = client.link_token_create(request)
        return response['link_token']
    except plaid.ApiException as e:
        print(f"error creating link token: {e}")
        return None

link_token = create_link_token()
print(f"Link token: {link_token}")
# -------------------------------------------------------


# print([e for e in CountryCode])
# request = InstitutionsGetRequest(
#     country_codes=[CountryCode.US],  # Using the enum directly
#     count=10,
#     offset=0,
# )

# try:
#     response = client.institutions_get(request)
#     print(response)
# except plaid.ApiException as e:
#     print(e)
#     print(json.loads(e.body))
