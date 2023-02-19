import csv
import random
import string

from anonymizer import Anonymizer

def anonymize_customer_csv(input_filename, output_filename, anonymizer):
    with open(input_filename, mode='r') as input_file, open(output_filename, mode='w', newline='') as output_file:
        reader = csv.DictReader(input_file)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        
        # Replace first name, last name, and address with random strings
        for row in reader:
            row['first_name'] = anonymizer.first_name()
            row['last_name'] = anonymizer.last_name()
            row['address'] = anonymizer.address()
            row['date_of_birth'] = row['date_of_birth']
            writer.writerow(row)

anonymizer = Anonymizer()
# Anonymize the first_name, last_name, and address columns in the CSV file
anonymize_customer_csv('input.csv', 'output/anonymized_data.csv', anonymizer)

