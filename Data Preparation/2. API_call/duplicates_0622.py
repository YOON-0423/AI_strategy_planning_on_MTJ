import pandas as pd

df = pd.read_excel('E:/Python_VS_code/2nd try/blue4_abs_data.xlsx')

df.drop_duplicates(subset = ['title'], keep = 'first', inplace = True)
df.to_excel("blue4_abs_data_edited.xlsx", index = False)
print("complete")