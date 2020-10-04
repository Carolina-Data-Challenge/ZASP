import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

## Get in two data frames
unemployment_2019_df = pd.read_csv("unemployment_rate_2019.csv")
graduation_rate_df = pd.read_csv("hs_grad_rate.csv")
graduation_rate_df = graduation_rate_df[['FIPS', 'hs_grad_rate']]

## Combine data frames
combined_df = pd.merge(unemployment_2019_df, graduation_rate_df, on='FIPS')
combined_df = combined_df[['FIPS', 'Unemployment_rate_2019', 'hs_grad_rate']]
# Multiply percent by 100
combined_df['hs_grad_rate'] = combined_df['hs_grad_rate'].apply(lambda x: x * 100)
# Get employment rate instead of unemployment
combined_df['Unemployment_rate_2019'] = combined_df['Unemployment_rate_2019'].apply(lambda x: 100 - x)
# rename
combined_df = combined_df.rename(columns={"Unemployment_rate_2019": "Employment Rate"})

## Create plot
sns.regplot(x='Employment Rate', y="hs_grad_rate", data=combined_df)
# Titles
plt.xlabel("Employment Rate")
plt.ylabel("HS Graduation Rate")
plt.title("Employment Rate vs HS Graduation Rate in US counties (2019)")
plt.show()
