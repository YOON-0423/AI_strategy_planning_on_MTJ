import requests
from dotenv import load_dotenv
import os
import json
import pandas as pd
import time


load_dotenv('.env', override=True)
API_KEY = os.getenv("open_alex_API_KEY")
# print(len(API_KEY))

file = pd.read_excel('b4_g8_abs_data_edited.xlsx')

# doi = file['doi']
# print(doi.isnull().sum()) # Number of NaN

results = []
for idx in range(len(file)):
    title = file['title'][idx]
    doi = file['doi'][idx]

    if doi == doi: # doi exist
        url = f"https://api.openalex.org/works/doi:{doi}"
        print(url)
        params = {
            "api_key": API_KEY,
            "select": "id,doi,display_name,publication_year,publication_date"
                }
        response = requests.get(url, params=params, timeout=30)
        status_code = response.status_code
        print(status_code)
        if response.status_code == 200:
            data = response.json()
            date = data.get("publication_date")
            row ={
                "title" : title,
                "doi" : doi,
                "date" : date,
                "status code" : status_code
                }
            results.append(row)
        else:
            row = {
                "title": title,
                "doi" : doi,
                "status code" : status_code
                }
            results.append(row)
        time.sleep(0.5)
    else: # doi == NaN
        row = {
            "title" : title
        }
        results.append(row)

df = pd.DataFrame(results)
df.to_excel('b4_g8_date_data.xlsx',index= False)



