import csv


def create_master(year: str):
    with open('finance_data_' + year + '.csv', 'r') as finance:

        finance_reader = csv.DictReader(finance)

        with open('hs_grad_rate.csv', 'r') as hs:

            hs_reader = csv.DictReader(hs)

            with open('unemployment_rate_' + year + '.csv', 'r') as unemployment:

                unemployment_reader = csv.DictReader(unemployment)

                with open('master_' + year + '.csv', 'w+') as write:

                    writer = csv.writer(write)
                    writer.writerow(finance_reader.fieldnames
                                    + ['grad_rate', 'unemployment_rate'])

                    hs_row = next(hs_reader)
                    unemployment_row = next(unemployment_reader)

                    for row in finance_reader:
                        county_code = int(float(row['county_code']))
                        if county_code > 56045:
                            break

                        if county_code == int(hs_row['FIPS']):
                            writer.writerow(
                                (row['county_code'], row['income'], row['loan_amount'], hs_row['hs_grad_rate'],
                                 unemployment_row['Unemployment_rate_' + year]))

                        hs_row = next(hs_reader)
                        unemployment_row = next(unemployment_reader)


create_master('2018')
create_master('2019')
