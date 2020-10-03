import pandas as pd
import csv

with open('final_1.csv', 'r') as file:
    reader = csv.DictReader(file)
    for h in reader.fieldnames:
        print(h)

data = pd.read_csv('final_1.csv')

x = data.groupby('county_code')['income'].quantile([0.33])
x.reset_index()[['county_code', 'income']].to_csv('aggregate_percentiles.csv')
