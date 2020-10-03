import pandas as pd

data1 = pd.read_csv('finance_data_2018.csv')
data2 = pd.read_csv('hs_grad_rate.csv')
data3 = pd.read_csv('unemployment_rate_2018.csv')


common = pd.merge(data1, data2)
common = pd.merge(common, data3)
common.to_csv('master_2018.csv', index=False)