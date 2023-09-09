import requests

url = "https://gabetest.terzocloud.com/api/v1/companies/fields"

payload = {}
headers = {
  'access-token': 'lkJJjivuNZki3VS5UhE3XcRTgqrTOfsfmnJA',
  'Accept': 'application/json',
  'Cookie': 'XSRF-TOKEN=82b43255-87b2-4540-bb07-4cc1a1313969'
}

company_fields = requests.request("GET", url, headers=headers, data=payload)

print(company_fields)

url = "https://gabetest.terzocloud.com/api/v1/companies/2002722/update"

payload = "  {\n    \"custom_fields\": {\n      \"cf_cyber_security_risk_rating\": \"High\"\n    }\n  }\n"
headers = {
  'access-token': 'lkJJjivuNZki3VS5UhE3XcRTgqrTOfsfmnJA',
  'Accept': 'application/json',
  'Content-Type': 'text/plain',
  'Cookie': 'XSRF-TOKEN=82b43255-87b2-4540-bb07-4cc1a1313969'
}

update_custom_field = requests.request("PATCH", url, headers=headers, data=payload)

print(update_custom_field.text)
