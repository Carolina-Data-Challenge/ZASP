import pandas as pd
import csv


# File that filters out any data in the main pool with incomes less than
# those calculated by the aggregates.
def filter_aggregates(year: str):
    data = pd.read_csv('cleaned_mortgage_data_' + year + '.csv')
    data = data.sort_values(by=['county_code', 'income'])
    data.to_csv('sorted_mortgage_data_' + year + '.csv', index=False)

    with open('sorted_mortgage_data_' + year + '.csv', 'r') as data:
        data_reader = csv.DictReader(data)
        with open('aggregate_percentiles_' + year + '.csv', 'r') as percentiles:
            percentile_reader = csv.DictReader(percentiles)
            with open('finalized_mortgage_data_' + year + '.csv', 'w+') as final:
                writer = csv.writer(final)
                writer.writerow(data_reader.fieldnames)

                data_row = next(data_reader)

                for percentile in percentile_reader:
                    while data_row['county_code'] == percentile['county_code']:
                        if float(data_row['income']) <= float(percentile['income']):
                            writer.writerow(data_row.values())
                        try:
                            data_row = next(data_reader)
                        except StopIteration as e:
                            break


filter_aggregates('2018')
filter_aggregates('2019')
