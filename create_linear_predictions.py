import pandas as pd

data_2018 = pd.read_csv('master_2018.csv')
data_2019 = pd.read_csv('master_2019.csv')

data_2019.rename(columns={'zasp_index': 'zasp_i'}, inplace=True)
merged = pd.merge(data_2018, data_2019, on='county_code')

merged['county_code'] = merged['county_code'].transform(lambda x: str(x).replace('.0', '').zfill(5))
merged['zasp_index'] = merged['zasp_i'] + (merged['zasp_i'] - merged['zasp_index'])
merged.to_csv('master_linear_pred_2020.csv', index=False)