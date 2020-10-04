import pandas as pd


# File that creates aggregates of the data, grouped by county code and aggregated
# by 33rd percentile income in that county.
def create_aggregate(year: str):
    data = pd.read_csv('cleaned_mortgage_data_' + year + '.csv')
    outcome = data.groupby('county_code')['income'].quantile([0.33])
    outcome.reset_index()[['county_code', 'income']] \
        .to_csv('aggregate_percentiles_' + year + '.csv', index=False)


create_aggregate('2018')
create_aggregate('2019')
