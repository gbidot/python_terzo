import csv
import requests

def update_company(company_id, risk_rating):
    url = f"https://gabetest.terzocloud.com/api/v1/companies/{company_id}/update"
    payload = {
        "custom_fields": {
            "cf_cyber_security_risk_rating": risk_rating
        }
    }
    headers = {
        'access-token': 'lkJJjivuNZki3VS5UhE3XcRTgqrTOfsfmnJA',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Cookie': 'XSRF-TOKEN=82b43255-87b2-4540-bb07-4cc1a1313969'
    }

    response = requests.patch(url, headers=headers, json=payload)

    if response.status_code == 200:
        return f"Successfully updated company {company_id} with risk rating: {risk_rating}"
    else:
        return f"Failed to update company {company_id}. Response: {response.text}"

def import_from_csv(filename):
    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)
        # Skip the header
        next(reader, None)
        return [row for row in reader]

if __name__ == "__main__":
    company_rows = import_from_csv("updated_companies.csv")
    for row in company_rows:
        company_id, company_name, risk_rating = row
        if risk_rating not in ["Lower", "Medium", "High", ""]:
            print(f"Unexpected rating value for company {company_id}: {risk_rating}")
            continue

        response_message = update_company(int(company_id), risk_rating)
        print(response_message)
