import csv


with open('trimmed_filter_no_income_zeros.csv', 'r') as file:
    reader = csv.DictReader(file)
    with open('final_1.csv', 'w+') as result:
        writer = csv.writer(result)
        writer.writerow(reader.fieldnames)
        for row in reader:
            if 'NA' not in row.values() and 'Exempt' not in row.values():
                writer.writerow(row.values())
