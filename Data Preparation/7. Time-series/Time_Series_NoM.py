import pandas as pd

file_name = 'blue2'

file = pd.read_excel(f'E:/Python_VS_code/2nd try/NoM/NoM_results/{file_name}_NoM_data.xlsx')

date = pd.to_datetime(file['date'])

file['year-month'] = date.dt.strftime('%Y-%m')

# time_series = file.groupby('year-month')['total_NoM'].sum().reset_index()


# df = pd.DataFrame(time_series)
# df.to_excel(f'E:/Python_VS_code/2nd try/NoM/Time_Series/{file_name}_time_series.xlsx', index= False)

