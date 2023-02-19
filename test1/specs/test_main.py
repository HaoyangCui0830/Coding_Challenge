import csv, sys
from io import StringIO
from unittest.mock import Mock


class Mockanonymizer:
    class Anonymizer:
        def first_name(self):
            return 'John'
        
        def last_name(self):
            return 'Doe'

        def address(self):
            return '123 Main St Apt 4 Anytown, USA'

sys.modules['anonymizer'] = Mockanonymizer()
from src.main import anonymize_customer_csv
from src.anonymizer import Anonymizer

def test_anonymize_customer_csv():
    # Create a sample input CSV string
    input_csv_str = '''first_name,last_name,address,date_of_birth
John,Doe,123 Main St,1990-01-01
Jane,Smith,456 Oak Ave,1980-02-02
'''

    # Create a mock Anonymizer instance
    anonymizer = Anonymizer()

    # Create a StringIO object to use as the output file
    input_file = StringIO(input_csv_str)
    input_file.filename = 'specs/test_csv.csv'
    output_file = StringIO()
    output_file.filename = 'specs/test_csv_output.csv'

    # Call the anonymize_customer_csv function with the input and output file objects and the mock Anonymizer
    anonymize_customer_csv(input_file.filename, output_file.filename, anonymizer)

    # Read the output file and verify that the rows have been anonymized

    with open(output_file.filename, mode='r', newline='') as f:
        reader = csv.DictReader(f)

        for row in reader:
            assert row['first_name'] == 'John'
            assert row['last_name'] == 'Doe'
            assert row['address'] == '123 Main St Apt 4 Anytown, USA'
            assert row['date_of_birth'] == '1985-05-10'


