import pandas as pd


def create_master_csv(year: str):
    mortgage = pd.read_csv('mortgage-data/mortgage_summary_' + year + '.csv')
    high_school = pd.read_csv('high-school-graduation-data/hs_grad_rate.csv')
    unemployment = pd.read_csv('unemployment-data/unemployment_rate_' + year + '.csv')

    master = pd.merge(mortgage, high_school)
    master = pd.merge(master, unemployment)
    master.rename(columns={'unemployment_rate_' + year: 'unemployment_rate'}, inplace=True)

    master['employment_rate'] = 100 - master['unemployment_rate']
    master['hs_grad_rate'] = master['hs_grad_rate'] * 100.0
    master['county_code'] = master['county_code'].transform(lambda x: str(x).zfill(5))

    pmt = master['loan_amount'] / 360.0
    qualifying_income = pmt * 4 * 12
    master['affordability_index'] = master['income'] / qualifying_income * 100 * 1000

    master['zasp_index'] = 0.5 * master['affordability_index'] + 0.25 * master['employment_rate'] + 0.25 * master[
        'hs_grad_rate']

    master.to_csv('master_' + year + '.csv', index=False)


create_master_csv('2018')
create_master_csv('2019')
