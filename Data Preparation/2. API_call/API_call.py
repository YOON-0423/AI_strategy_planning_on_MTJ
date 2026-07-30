###### API request

import requests
from dotenv import load_dotenv
import os
import json
import pandas as pd
import re
import time

# #print(os.getcwd())

load_dotenv('.env', override=True)
API_KEY = os.getenv("ELSEVIER_API_KEY")
# # #print(len(API_KEY))

queries = {"tech_id" : "magnetic tunnel junction", "query" : 'TITLE-ABS-KEY(("magnetic tunnel junction*" OR "MTJ" OR "MTJ-based" OR "spintronic*" OR "spintronic device*" OR "spintronic synapse*" OR "spintronic neuron*" OR "MRAM" OR "magnetic random access memory" OR "spin-orbit torque" OR "SOT" OR "spin-transfer torque" OR "STT" OR "voltage-controlled magnetic anisotropy" OR "VCMA") AND ("developmental learning" OR "developmental principle*" OR "developmental neural network*" OR "developmental AI" OR "developmental artificial intelligence" OR "neurodevelopmental" OR "brain development" OR "brain-inspired development" OR "brain inspired development" OR "self-organizing" OR "self organizing" OR "self-organization" OR "self organization" OR "self-organizing neural network*" OR "self organizing neural network*" OR "growing neural network*" OR "evolving neural network*" OR "adaptive growth" OR "network growth" OR "neural growth" OR "synaptic growth" OR "synaptogenesis" OR "synapse formation" OR "structural plasticity" OR "network plasticity" OR "maturation" OR "neural maturation" OR "synaptic maturation" OR "developmental plasticity" OR "activity-dependent plasticity" OR "activity dependent plasticity" OR "homeostatic plasticity" OR "metaplasticity" OR "pruning" OR "synaptic pruning" OR "neural pruning" OR "developmental pruning" OR "resource allocation" OR "adaptive resource allocation") AND ("low-power" OR "low power" OR "energy-efficient" OR "energy efficient" OR "power-efficient" OR "power efficient" OR "energy-constrained" OR "energy constrained" OR "on-device learning" OR "on device learning" OR "on-chip learning" OR "on chip learning" OR "online learning" OR "continual learning" OR "incremental learning" OR "adaptive learning" OR "edge AI" OR "edge intelligence" OR "neuromorphic*" OR "neural network*" OR "spiking neural network*" OR "SNN" OR "hardware accelerator*"))'}

url = "https://api.elsevier.com/content/search/scopus"

headers = {"X-ELS-APIKey": API_KEY, "Accept": "application/json"}

start_list = range(0, 19, 25)
all_results = []

# for idx in start_list:
#     params = {"query": queries["query"],
#           "count": 25,
#           "start": idx,
#           "view" : "FULL"
#           }
    
#     response = requests.get(url, headers=headers, params=params) # default: #count=25, start=0
#     data = response.json()
#     all_results.append(data)
#     time.sleep(3)
#     print("idx :" f"{idx}")
#     print(response.status_code)

params = {"query": queries["query"],
         "count": 25,
         "start": 0
         }
    
response = requests.get(url, headers=headers, params=params) # default: count=25, start=0
data = response.json()
all_results.append(data)
time.sleep(2)
print(response.status_code)


with open("keyword_test.json", "w", encoding="utf-8") as outfile:
    json.dump(all_results, outfile, ensure_ascii=False, indent=4)


# ##### API json convert to excel file

results = json.load(open('b2_g7.json', "r", encoding = 'utf-8'))

total_results = results[0]["search-results"]['opensearch:totalResults']
print(total_results)
start_idx = results[0]["search-results"]['opensearch:startIndex']
item_page = results[0]["search-results"]['opensearch:itemsPerPage']

row = []

for idx in range(len(results)):
    total_results = results[idx]["search-results"]['opensearch:totalResults']
    start_idx = results[idx]["search-results"]['opensearch:startIndex']
    item_page = results[idx]["search-results"]['opensearch:itemsPerPage']
    entries = results[idx]["search-results"]['entry']
    
    for e_idx in range(len(entries)):

        title_norm = entries[e_idx].get("dc:title").lower()
        authors = entries[e_idx].get('dc:creator')
        cover_ddate = entries[e_idx].get("prism:coverDisplayDate") # Journal publication date  
        cover_date = entries[e_idx].get("prism:coverDate") # Journal publication date, no difference with cover_ddate
        doi = entries[e_idx].get("prism:doi")
        eid = entries[e_idx].get('eid') #Electronic Identifier
        journal = entries[e_idx].get('prism:publicationName')

        query_name = queries["query"]
        tech_id = queries["tech_id"]

        rows ={
            "title" : title_norm,
            "authors" : authors,
            "coverDisplaydate" : cover_ddate,
            "coverDate" : cover_date,
            "doi" : doi,
            "query" : query_name,
            "tech_id" : tech_id,
            "start_index" : start_idx,
            "eid" : eid,
            "journal" : journal
        }

        row.append(rows)

df = pd.DataFrame(row)
df.to_excel("b2_g7.xlsx",index=False)

df.drop_duplicates(subset = ['title'], keep = 'first')
df.to_excel("b2_g7_edited.xlsx", index = False)
print("complete")

######