import csv


# File that cleans up raw CSV mortgage data.
def print_headers(d_reader: csv.DictReader):
    """Prints the headers of a given CSV dictionary reader."""
    headers = d_reader.fieldnames
    for header in headers:
        print(header)


def write_to_file(year: str):
    """Cleans up raw mortgage data and outputs it to a pooled CSV."""
    with open('source/year_' + year + '.csv', 'r') as source:
        with open('cleaned_mortgage_data_' + year + '.csv', 'w+') as result:
            reader = csv.DictReader(source)
            writer = csv.writer(result)

            writer.writerow(('activity_year', 'county_code', 'income', 'loan_to_value_ratio',
                             'loan_purpose', 'interest_rate', 'loan_term',
                             'debt_to_income_ratio', 'loan_amount',
                             'action_taken', 'hoepa_status'))

            # Go thorough each line and add it to the eventual CSV only if the loan purpose is 1,
            # there are no 'NA' or exempt values in any row, and the income is greater than zero.
            for line in reader:
                relevant_values = map(line.get, ('activity_year', 'county_code', 'income', 'loan_to_value_ratio',
                                                 'loan_purpose', 'interest_rate', 'loan_term',
                                                 'debt_to_income_ratio', 'loan_amount',
                                                 'action_taken', 'hoepa_status'))
                if line['loan_purpose'] == '1' and 'NA' not in relevant_values and int(line['income']) > 0 and \
                        line['loan_to_value_ratio'] != "Exempt":
                    writer.writerow(map(line.get, ('activity_year', 'county_code', 'income', 'loan_to_value_ratio',
                                                   'loan_purpose', 'interest_rate', 'loan_term',
                                                   'debt_to_income_ratio', 'loan_amount',
                                                   'action_taken', 'hoepa_status')))


write_to_file('2018')
write_to_file('2019')
