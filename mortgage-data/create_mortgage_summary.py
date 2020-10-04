import pandas as pd


# This file uses the finalized mortgage data sets to create a summary of the data.
def create_mortgage_summary(year: str):
    data = pd.read_csv('finalized_mortgage_data_' + year + '.csv')
    group = data.groupby('county_code')['income', 'loan_amount'].median()
    group.reset_index().to_csv('mortgage_summary_' + year + '.csv',
                               columns=('county_code', 'income', 'loan_amount'),
                               index=False)


create_mortgage_summary('2018')
create_mortgage_summary('2019')
