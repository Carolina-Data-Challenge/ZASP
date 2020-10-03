import csv
from typing import Iterable


def print_headers(d_reader: csv.DictReader):
    headers = d_reader.fieldnames
    for header in headers:
        print(header)


def write_to_file(file: str, d_reader: csv.DictReader, a: Iterable[str],
                  overwrite: bool = False):
    with open(file, 'w+' if overwrite else 'a+') as result:
        writer = csv.writer(result)

        # Add column headers.
        if overwrite:
            writer.writerow(a)

        for row in d_reader:
            writer.writerow(map(row.get, a))


with open('year_2018.csv', 'r') as original:
    reader = csv.DictReader(original)
    print_headers(reader)
    write_to_file('trimmed.csv', reader, ('activity_year', 'county_code', 'income', 'loan_to_value_ratio',
                                          'loan_purpose', 'interest_rate', 'loan_term',
                                          'debt_to_income_ratio', 'loan_amount',
                                          'action_taken', 'hoepa_status'),
                  True)

with open('year_2019.csv', 'r') as original:
    reader = csv.DictReader(original)
    print_headers(reader)
    write_to_file('trimmed.csv', reader, ('activity_year', 'county_code', 'income', 'loan_to_value_ratio',
                                          'loan_purpose', 'interest_rate', 'loan_term',
                                          'debt_to_income_ratio', 'loan_amount',
                                          'action_taken', 'hoepa_status'))
