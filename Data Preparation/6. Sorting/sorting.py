import pandas as pd

############## Count ############

file_name = 'b4_g8'

file_abs = pd.read_excel(f'E:/Python_VS_code/2nd try/sorting/sorting_source/{file_name}_abs_NoM.xlsx')
file_title = pd.read_excel(f'E:/Python_VS_code/2nd try/sorting/sorting_source/{file_name}_title_results.xlsx')
file_keyword = pd.read_excel(f'E:/Python_VS_code/2nd try/sorting/sorting_source/{file_name}_keyword_results.xlsx')
# title = file.drop_duplicates(subset=['title'], keep='first')

mentioned_abs = file_abs['title'].value_counts()
mentioned_title = file_title['title'].value_counts()
mentioned_keyword = file_keyword['title'].value_counts()

total_mentioned = mentioned_abs.add(mentioned_title, fill_value = 0).add(mentioned_keyword, fill_value = 0)

# print(total_mentioned)


# print("abs")
# print(mentioned_abs)
# print("title")
# print(mentioned_title)
# print("keyword")
# print(mentioned_keyword)


#######################################

# add_file = pd.read_excel('E:/Python_VS_code/2nd try/test/source/b1_g1_date_data.xlsx')

date_file = pd.read_excel(f'E:/Python_VS_code/2nd try/sorting/sorting_source/{file_name}_date_data.xlsx')

# ############# Add data ################
date_file['abs_NoM'] = date_file['title'].map(mentioned_abs)
date_file['title_NoM'] = date_file['title'].map(mentioned_title)
date_file['keyword_NoM'] = date_file['title'].map(mentioned_keyword)
date_file['total_NoM'] = date_file['title'].map(total_mentioned)

date_file.to_excel(f'E:/Python_VS_code/2nd try/sorting/sorting_results/{file_name}_NoM_results.xlsx', index=False)
print("Complete")
