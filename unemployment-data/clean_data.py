import pandas as pd

# Read in data
df = pd.read_csv("source/Unemployment.csv", encoding='unicode_escape', skiprows=7)

# Rename columns to match our conventions
df.rename(columns={'FIPStxt': 'county_code', 'Unemployment_rate_2018': 'unemployment_rate_2018',
                   'Unemployment_rate_2019': 'unemployment_rate_2019'}, inplace=True)

# New data frames for 2018 and 2019
df_2018 = df[['county_code', 'unemployment_rate_2018']]
df_2019 = df[['county_code', 'unemployment_rate_2019']]

# Save dataframes
df_2018.to_csv("unemployment_rate_2018.csv", index=False)
df_2019.to_csv("unemployment_rate_2019.csv", index=False)
