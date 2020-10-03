import csv


def print_headers(d_reader: csv.DictReader):
    headers = d_reader.fieldnames
    for header in headers:
        print(header)


# Open the original data.
with open('year_2018.csv', 'r') as original:
    # Create reader from original data.
    reader = csv.DictReader(original)

    # Print headers.
    print_headers(reader)

    # Open CSV to create trimmed data.
    with open('year_2018_trimmed.csv', 'w') as result:
        writer = csv.writer(result)
        for row in reader:
            # Change this line to include whatever fields
            # you want.
            writer.writerow((row['county_code'], row['income']))
