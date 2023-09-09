import csv
import requests
import concurrent.futures

MAX_THREADS = 5  # Adjust based on your machine and the API's rate limits

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
    return response.text

def import_from_csv(filename):
    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)
        # Skip the header
        next(reader, None)
        return [row for row in reader]

def worker(row):
    company_id, company_name, risk_rating = row
    response = update_company(int(company_id), risk_rating)
    return f"Updated company {company_id}: {response}"

if __name__ == "__main__":
    company_rows = import_from_csv("updated_companies.csv")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        results = list(executor.map(worker, company_rows))
    
    for result in results:
        print(result)

