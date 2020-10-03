import pandas as pd 

## Read in data
df = pd.read_csv("Unemployment.csv",encoding= 'unicode_escape',skiprows=7)
## Rename FIPStxt to FIPS
df.rename(columns={'FIPStxt':'FIPS'},inplace = True)
##new data frames for 2018 and 2019
df_2018 = df[['FIPS','Unemployment_rate_2018']]
df_2019 = df[['FIPS','Unemployment_rate_2019']]
## Save dataframes
df_2018.to_csv("unemployment_rate_2018.csv")
df_2019.to_csv("unemployment_rate_2019.csv")