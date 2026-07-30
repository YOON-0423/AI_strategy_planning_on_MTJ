import re
import pandas as pd

file_name = "b4_g8"
file = pd.read_excel(f"E:/Python_VS_code/2nd try/title/title_source/{file_name}_abs_data_edited.xlsx")

keyword1 = r'\bdevelopmental[-–— ](?:learning|principles?|neural[-–— ]networks?|AI|artificial[-–— ]intelligence)\b|\bneurodevelopmental\b|\bbrain[-–— ]development\b|\bbrain[-–— ]inspired[-–— ]development\b'
keyword2 = r'\bself[-–— ]organizing[-–— ]neural[-–— ]networks?\b'
keyword3 = r'\b(?:growing|evolving)[-–— ]neural[-–— ]networks?\b|\b(?:adaptive|network|neural|synaptic)[-–— ]growth\b|\bsynaptogenesis\b|\bsynapse[-–— ]formation\b'
keyword4 = r'\b(?:neural|synaptic)[-–— ]maturation\b'
keyword5 = r'\b(?:developmental|activity[-–— ]dependent)[-–— ]plasticity\b'
keyword6 = r'\b(?:synaptic|neural|developmental)[-–— ]pruning\b'
keyword7 = r'\badaptive[-–— ]resource[-–— ]allocation\b'
keyword = [keyword1,keyword2,keyword3,keyword4,keyword5,keyword6,keyword7]

def word_frequency_counter (keyword, file):
     mentioned_results = []
     for idx in range(len(file)):
         title = file['title'][idx]
         for key in keyword:
            match_results = re.finditer(key, title, flags = re.IGNORECASE)
            mat_results = list(match_results)
            for match in mat_results:
                pattern_name = match_results
                pattern = key
                match_word = match.group()
                row = {
                "title" : title,
                "pattern name" : pattern_name,
                "pattern" : pattern,
                "match word" : match_word,
                "text" : title
                }
                mentioned_results.append(row)
     return mentioned_results

WFC = word_frequency_counter(keyword, file)

df = pd.DataFrame(WFC)
df.to_excel(f"E:/Python_VS_code/2nd try/title/title_results/{file_name}_title_results.xlsx", index = False) 
print("complete")

