import requests
from dotenv import load_dotenv
import os
import json
import pandas as pd
import time

load_dotenv('.env', override=True)
API_KEY = os.getenv('ELSEVIER_API_KEY')

###### file loading ######

excel_file = pd.read_excel('b4_g8_edited.xlsx')
eid = excel_file['eid']
# print(eid)

results = []

for index, e_eid in enumerate(eid):
    url1 = f"https://api.elsevier.com/content/abstract/eid/{e_eid}"
    # print(url1)
    headers = {
        "X-ELS-APIKey" : API_KEY,
        "Accept": "application/json"}
    response1 = requests.get(url1, headers=headers)
    data = response1.json()
    results.append(data)

    time.sleep(1)
    print(index)
    print(url1)
    print(response1.status_code)

with open("b4_g8_abs.json", "w") as outfile:
    json.dump(results, outfile, indent=4)

###### API json convert to excel file ######

open_json = json.load(open('b4_g8_abs.json',"r", encoding = 'utf-8'))

row_data = []

for idx in range(len(open_json)):
    abstract = open_json[idx]['abstracts-retrieval-response']["coredata"].get('dc:description')
    eid = open_json[idx]['abstracts-retrieval-response']["coredata"].get('eid')
    doi = open_json[idx]['abstracts-retrieval-response']["coredata"].get('prism:doi')
    title = open_json[idx]['abstracts-retrieval-response']["coredata"].get('dc:title')
    cover_date = open_json[idx]['abstracts-retrieval-response']["coredata"].get('prism:coverDate')
    publisher = open_json[idx]['abstracts-retrieval-response']["coredata"].get('prism:publicationName')

    row = {
        "title" : title,
        "abstract" : abstract,
        "doi" : doi,
        "eid" : eid,
        "cover date" : cover_date,
        "journal" : publisher,
    }

    row_data.append(row)

df = pd.DataFrame(row_data)
df.to_excel('b4_g8_abs_data.xlsx', index=False)
print("complete")
# print(open_json[9]['abstracts-retrieval-response']["coredata"]['prism:publicationName'])