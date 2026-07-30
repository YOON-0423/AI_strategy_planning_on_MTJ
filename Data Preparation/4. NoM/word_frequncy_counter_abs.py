import re
import pandas as pd

file = pd.read_excel('b4_g8_abs_data_edited.xlsx')

# for idx in range(len(file)):
#     abstract = file['abstract'][idx]
#     if pd.isna(abstract):
#         continue
#     else: 

# abstract = file[file['abstract'].isna()].index

# print(file['abstract'][528])

keyword1 = r'\bdevelopmental[-–— ](?:learning|principles?|neural[-–— ]networks?|AI|artificial[-–— ]intelligence)\b|\bneurodevelopmental\b|\bbrain[-–— ]development\b|\bbrain[-–— ]inspired[-–— ]development\b'
keyword2 = r'\bself[-–— ]organizing[-–— ]neural[-–— ]networks?\b'
keyword3 = r'\b(?:growing|evolving)[-–— ]neural[-–— ]networks?\b|\b(?:adaptive|network|neural|synaptic)[-–— ]growth\b|\bsynaptogenesis\b|\bsynapse[-–— ]formation\b'
keyword4 = r'\b(?:neural|synaptic)[-–— ]maturation\b'
keyword5 = r'\b(?:developmental|activity[-–— ]dependent)[-–— ]plasticity\b'
keyword6 = r'\b(?:synaptic|neural|developmental)[-–— ]pruning\b'
keyword7 = r'\badaptive[-–— ]resource[-–— ]allocation\b'

keyword = [
    keyword1,
    keyword2,
    keyword3,
    keyword4,
    keyword5,
    keyword6,
    keyword7
]

def word_frequency_counter (keyword, file):
     mentioned_results = []
     for idx in range(len(file)):
         abstract = file['abstract'][idx]
         title = file['title'][idx]
         if pd.isna(abstract):
             continue
         else:
            for key in keyword:
                match_results = re.finditer(key, abstract, flags = re.IGNORECASE)
                mat_results = list(match_results)
                for match in mat_results:
                    pattern_name = match_results
                    pattern = key
                    match_word = match.group()
                    str_word = match.start()
                    end_word = match.end()
                    row = {
                        "title" : title,
                        "pattern name" : pattern_name,
                        "pattern" : pattern,
                        "match word" : match_word,
                        "start" : str_word,
                        "end" : end_word,
                        "text" : abstract[str_word : end_word+20]
                    }
                    mentioned_results.append(row)
     return mentioned_results

WFC = word_frequency_counter(keyword, file)

# print(WFC)

df = pd.DataFrame(WFC)
df.to_excel("b4_g8_NoM.xlsx", index = False)
