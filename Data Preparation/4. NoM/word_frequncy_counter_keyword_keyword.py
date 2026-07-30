import re
import pandas as pd

file_name = "b2_g3"
file = pd.read_excel(f"E:/Python_VS_code/2nd try/keyword/keyword_source/{file_name}_keyword.xlsx") 

# for idx in range(len(file)):
#     abstract = file['abstract'][idx]
#     if pd.isna(abstract):
#         continue
#     else: 

# abstract = file[file['abstract'].isna()].index

# print(file['abstract'][528])

keyword1 = r'\b(?:(?:physical|spintronic|magnetic|nanomagnetic|nanomagnet|MTJ|MRAM|device|hardware)\s+reservoir(?:\s+computing)?|reservoir\s+computing)\b'
keyword2 = r'\breservoir\s+(?:networks?|dynamics)\b'
keyword3 = r'\bdynamical\s+systems?\b|\b(?:nonlinear|magnetization|spin|transient|relaxation)\s+dynamics\b'
keyword4 = r'\b(?:fading|short[-–— ]term)\s+memory\b'
keyword5 = r'\btemporal\s+processing\b|\btime[-–— ]series\s+processing\b'
keyword = [keyword1, keyword2, keyword3, keyword4, keyword5]


def word_frequency_counter (keyword, file):
     mentioned_results = []
     for idx in range(len(file)):
         abstract = file['keyword'][idx]
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
                        "text" : abstract
                    }
                    mentioned_results.append(row)
     return mentioned_results

WFC = word_frequency_counter(keyword, file)

# print(WFC)

df = pd.DataFrame(WFC)
df.to_excel(f"E:/Python_VS_code/2nd try/keyword/keyword_results/{file_name}_keyword_results.xlsx", index = False) 
print("complete")
