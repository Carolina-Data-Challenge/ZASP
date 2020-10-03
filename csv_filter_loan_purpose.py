import csv


with open('trimmed.csv', 'r') as file:
    reader = csv.DictReader(file)
    with open('trimmed_filtered.csv', 'w+') as result:
        writer = csv.writer(result)
        writer.writerow(reader.fieldnames)
        for row in reader:
            if row['loan_purpose'] == '1':
                writer.writerow(row.values())
