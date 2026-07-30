import requests
from dotenv import load_dotenv
import os
import json
import pandas as pd
import time

load_dotenv('.env', override=True)
API_KEY = os.getenv('ELSEVIER_API_KEY')

# ###### file loading ######

excel_file = pd.read_excel('b4_g8_edited.xlsx') #############################################
eid = excel_file['eid']
# print(eid)

results = []

for index, e_eid in enumerate(eid):
    url1 = f"https://api.elsevier.com/content/abstract/eid/{e_eid}?view=FULL"
    # print(url1)
    headers = {
        "X-ELS-APIKey" : API_KEY,
        "Accept": "application/json"}
    response1 = requests.get(url1, headers=headers)
    data = response1.json()
    results.append(data)

    time.sleep(0.2)
    print(index)
    print(url1)
    print(response1.status_code)

with open("b4_g8_keyword.json", "w") as outfile: ##############################################
    json.dump(results, outfile, indent=4)

###### API json convert to excel file ######

open_json = json.load(open('b4_g8_keyword.json',"r", encoding = 'utf-8')) #####################################
# keyword_list = open_json[698]['abstracts-retrieval-response']['item']['bibrecord']['head']['citation-info']

# if isinstance(keyword_list, dict):
#     print(type(keyword_list))
#     keyword_list = list(keyword_list)
#     print(type(keyword_list))

row_data = []

for idx in range(len(open_json)):
    # print(idx)
    title = open_json[idx]['abstracts-retrieval-response']["coredata"].get('dc:title')
    doi = open_json[idx]['abstracts-retrieval-response']["coredata"].get('prism:doi')
    eid = open_json[idx]['abstracts-retrieval-response']["coredata"].get('eid')
    keyword_list = open_json[idx]['abstracts-retrieval-response']['item']['bibrecord']['head']['citation-info'].get('author-keywords',{}).get('author-keyword',[])
    if isinstance(keyword_list, dict):
        keyword_list = [keyword_list]
    for idx_1 in range(len(keyword_list)):
        # print(idx_1)
        key = keyword_list[idx_1]['$']
        row = {
            "title" : title,
            "keyword" : key,
            "doi" : doi,
            "eid" : eid
        }

        row_data.append(row)

df = pd.DataFrame(row_data)
df.to_excel('b4_g8_keyword.xlsx', index=False) ##################################
print("complete")