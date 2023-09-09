import time
import csv
import requests

def get_all_companies():
    base_url = "https://gabetest.terzocloud.com/api/v1/companies"
    params = {
        "name": "",
        "department": "",
        "business_units": "",
        "owner": "",
        "sort_by": "",
        "asc": "",
        "cf_name": "",
        "pageable": ""
    }
    headers = {
        'access-token': 'lkJJjivuNZki3VS5UhE3XcRTgqrTOfsfmnJA',
        'Accept': 'application/json',
        'Cookie': 'XSRF-TOKEN=82b43255-87b2-4540-bb07-4cc1a1313969'
    }

    all_companies = []
    page = 0
    while True:
        params["page"] = page
        response = requests.get(base_url, headers=headers, params=params, timeout=10)
        data = response.json()
        
        if "data" not in data:
            print(f"Warning: Key 'data' not found in response for page {page}. Response: {data}")
            break

        if "content" not in data["data"] or not data["data"]["content"]:
            print(f"Warning: Key 'content' not found inside 'data' for page {page}. Response: {data}")
            break
        
        all_companies.extend(data["data"]["content"])
        page += 1

    return all_companies

def export_to_csv(companies, filename):
    all_keys = set().union(*(company.keys() for company in companies))
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=all_keys)
        writer.writeheader()
        
        for company in companies:
            if isinstance(company, dict):
                writer.writerow(company)
            else:
                print(f"Unexpected entry in companies list: {company}")

if __name__ == "__main__":
    start_time = time.time()

    companies = get_all_companies()
    export_to_csv(companies, 'companies.csv')
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Script executed in {elapsed_time:.2f} seconds")
