import csv


with open('trimmed_filtered.csv', 'r') as file:
    reader = csv.DictReader(file)
    with open('trimmed_filter_no_income_zeros.csv', 'w+') as result:
        writer = csv.writer(result)
        writer.writerow(reader.fieldnames)
        for row in reader:
            if row['income'] != '0':
                writer.writerow(row.values())
