import pandas as pd

data_2018 = pd.read_csv('master_2018.csv')
data_2019 = pd.read_csv('master_2019.csv')


def lerp(x, y):
    return y + (y - x)


lerped_2020_df = pd.DataFrame(
    columns=['county_code', 'income', 'loan_amount', 'county_name', 'state', 'hs_grad_rate', 'unemployment_rate',
             'employment_rate', 'affordability_index', 'zasp_index'])

lerped_2020_df['county_code'] = data_2018['county_code']
lerped_2020_df['income'] = lerp(data_2018['income'], data_2019['income'])
lerped_2020_df['loan_amount'] = lerp(data_2018['loan_amount'], data_2019['loan_amount'])
lerped_2020_df['county_name'] = data_2018['county_name']
lerped_2020_df['state'] = data_2018['state']
lerped_2020_df['hs_grad_rate'] = lerp(data_2018['hs_grad_rate'], data_2019['hs_grad_rate'])
lerped_2020_df['unemployment_rate'] = lerp(data_2018['unemployment_rate'], data_2019['unemployment_rate'])
lerped_2020_df['employment_rate'] = lerp(data_2018['employment_rate'], data_2019['employment_rate'])
lerped_2020_df['affordability_index'] = lerp(data_2018['affordability_index'], data_2019['affordability_index'])

lerped_2020_df['county_code'] = lerped_2020_df['county_code'].transform(lambda x: str(x).replace('.0', '').zfill(5))
lerped_2020_df['affordability_index'] = lerped_2020_df['affordability_index'].transform(lambda x: min(x, 100))
lerped_2020_df['employment_rate'] = lerped_2020_df['employment_rate'].transform(lambda x: min(x, 100))
lerped_2020_df['hs_grad_rate'] = lerped_2020_df['hs_grad_rate'].transform(lambda x: min(x, 100))

lerped_2020_df['zasp_index'] = 0.5 * lerped_2020_df['affordability_index'] + 0.25 * lerped_2020_df[
    'hs_grad_rate'] + 0.25 * lerped_2020_df['employment_rate']

lerped_2020_df.to_csv('master_linear_pred_2020.csv', index=False)
