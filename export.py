import time
import csv
import requests

def get_all_companies():
    base_url = "https://gabetest.terzocloud.com/api/v1/companies"
    params = {
        'name': '',
        'department': '',
        'business_units': '',
        'owner': '',
        'sort_by': '',
        'asc': '',
        'cf_name': '',
    }
    headers = {
        'access-token': 'lkJJjivuNZki3VS5UhE3XcRTgqrTOfsfmnJA',
        'Accept': 'application/json',
        'Cookie': 'XSRF-TOKEN=82b43255-87b2-4540-bb07-4cc1a1313969'
    }
    
    all_companies = []
    page = 0
    
    while True:
        params['page'] = page
        response = requests.get(base_url, params=params, headers=headers, timeout=10)
        data = response.json()
        
        # Check if the key "data" exists in the response
        if "data" not in data or not data["data"]["content"]:
            break
        
        # Append companies from current page to the all_companies list
        all_companies.extend(data["data"]["content"])
        
        # Move on to the next page
        page += 1

    return all_companies

def export_to_csv(companies, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'cf_cyber_security_risk_rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for company in companies:
            if isinstance(company, dict):  # ensure company is a dictionary
                rating = company['custom_fields'].get('cf_cyber_security_risk_rating', '')
                if rating not in ["Lower", "Medium", "High", ""]:
                    print(f"Unexpected rating value for company {company['id']}: {rating}")
                    continue
                writer.writerow({'id': company['id'], 'name': company['name'], 'cf_cyber_security_risk_rating': rating})
            else:
                print(f"Unexpected entry in companies list: {company}")

if __name__ == "__main__":
    start_time = time.time()

    companies = get_all_companies()
    export_to_csv(companies, 'companies.csv')

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Script executed in {elapsed_time:.2f} seconds")