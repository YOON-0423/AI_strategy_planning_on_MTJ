################### data loading #####################

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_name = 'b2_g9'

file = pd.read_excel(f'E:/Python_VS_code/2nd try/Smoothing/Smoothing_source/{file_name}_time_results.xlsx')

date = pd.to_datetime(file['year-month'])
file['year-month'] = date.dt.strftime('%Y-%m')


x_data = file['year-month']
y_data = file['total_NoM']

######################### Double Exponential Smoothing Method ##########################

alpha = 0.1 # Level coefficient
beta = 0.2  # Trend coefficient

D_t = y_data # Original data
L_t = []     # Level data
T_t = []     # Trend data
D_hat_t = [] # Forecasting data

L_t.append(D_t[0])
T_t.append(0)
D_hat_t.append(D_t[0])

for idx in range(1, len(D_t)):
    result_L = alpha*D_t[idx] + (1-alpha)*(L_t[idx-1] + T_t[idx-1])
    L_t.append(result_L)

    result_T = beta*(L_t[idx] - L_t[idx-1]) + (1-beta)*T_t[idx-1]
    T_t.append(result_T)
    D_hat_t.append(result_L + result_T)

# print(L_t)
# print('-'*50)
# print(T_t)
# print('-'*50)
# print(len(D_hat_t))

file['level'] = L_t
file['trend'] = T_t
file['forecast'] = D_hat_t

x_results = file['year-month']

y_results_L = L_t
y_results_T = T_t
y_results_D = D_hat_t

# fig, (ax1, ax2, ax3) = plt.subplots(1,3)
# ax1.plot(x_results, y_results_L, label = 'level')
# ax1.legend()
# ax2.plot(x_results, y_results_T, label = 'trend')
# ax2.legend()
# ax3.plot(x_results, y_results_D, label = 'forecast')
# ax3.legend()

# plt.tight_layout()
# plt.show()

df = pd.DataFrame(file)
# df.to_excel(f'E:/Python_VS_code/2nd try/Smoothing/Smoothing_results/test_blue1_smoothing_p{alpha}_{beta}.xlsx',index = False)
df.to_excel(f'E:/Python_VS_code/2nd try/Smoothing/Smoothing_results/2nd_try/{file_name}_smoothing_results.xlsx',index = False)