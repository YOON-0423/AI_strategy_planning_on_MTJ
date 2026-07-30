import pandas as pd

file_name = 'blue4'

file = pd.read_excel(f'E:/Python_VS_code/2nd try/NoM/NoM_source/{file_name}_NoM_results.xlsx')

title = file['title']

data = file[file['total_NoM'].notna()]

df = pd.DataFrame(data)
df.to_excel(f'E:/Python_VS_code/2nd try/NoM/NoM_results/{file_name}_NoM_data.xlsx',index=False)
print(f"{file_name} complete")