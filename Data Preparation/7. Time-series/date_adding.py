import pandas as pd

file_name = 'b2_g9'

standard = pd.read_excel('E:/Python_VS_code/2nd try/sorting/date_adding_date.xlsx')
file = pd.read_excel(f'E:/Python_VS_code/2nd try/sorting/date_adding_source/{file_name}_time_series.xlsx')

matched_df = pd.merge(standard, file, on='year-month', how = 'left')

matched_df= matched_df.fillna(0)

matched_file = pd.DataFrame(matched_df)
save_file = matched_file.to_excel(f'E:/Python_VS_code/2nd try/sorting/date_adding_results/{file_name}_time_results.xlsx', index = False)