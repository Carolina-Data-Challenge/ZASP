import pandas as pd
import csv

data = pd.read_csv('final_1.csv')
data = data.sort_values(by=['county_code', 'income'])
data.to_csv('sorted_data.csv')

# Open the CSV file with raw data.
with open('sorted_data.csv', 'r') as data:

    data_reader = csv.DictReader(data)

    # Open the CSV file with aggregate of income by 33rd percentile.
    with open('aggregate_percentiles.csv', 'r') as percentiles:

        percentile_reader = csv.DictReader(percentiles)

        # Open a new CSV file to write the final data to.
        with open('sorted_discarded_data.csv', 'w+') as discarded_data:

            writer = csv.writer(discarded_data)
            writer.writerow(data_reader.fieldnames)

            data_row = next(data_reader)

            for percentile in percentile_reader:
                while data_row['county_code'] == percentile['county_code']:
                    if float(data_row['income']) <= float(percentile['income']):
                        writer.writerow(data_row.values())
                    data_row = next(data_reader)
