import pandas as pd

# Read data which is sorted and has the upper 66% of incomes discarded.
data = pd.read_csv('sorted_discarded_data.csv')

# Create values for checking whether we are in 2018 or 2019.
is_2018 = data['activity_year'] == 2018
is_2019 = data['activity_year'] == 2019

# Get individual data-frames for 2018 and 2019.
data_2018 = data[is_2018]
data_2019 = data[is_2019]

# Create groupings and aggregate by median.
group_2018 = data_2018.groupby('county_code')['income', 'loan_amount'].median()
group_2019 = data_2019.groupby('county_code')['income', 'loan_amount'].median()

# Output to individual CSV files.
group_2018.reset_index().to_csv('finance_data_2018.csv',
                                columns=('county_code', 'income', 'loan_amount'),
                                index=False)
group_2019.reset_index().to_csv('finance_data_2019.csv',
                                columns=('county_code', 'income', 'loan_amount'),
                                index=False)
