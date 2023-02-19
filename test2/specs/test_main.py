import unittest
from src.main import parse_fixed_width_file

class TestParseFixedWidthFile(unittest.TestCase):
    def test_parse_fixed_width_file(self):
        spec = {
            "ColumnNames": [
                "f1",
                "f2",
                "f3",
                "f4",
                "f5",
                "f6",
                "f7",
                "f8",
                "f9",
                "f10"
            ],
            "Offsets": [
                "5",
                "12",
                "3",
                "2",
                "13",
                "7",
                "10",
                "13",
                "20",
                "13"
            ],
            "FixedWidthEncoding": "windows-1252",
            "IncludeHeader": "True",
            "DelimitedEncoding": "utf-8"
        }
        expected_output = "f1,f2,f3,f4,f5,f6,f7,f8,f9,f10\n"
        parse_fixed_width_file('specs/input_file_with_header', 'specs/output_file_with_header', spec)
        with open('specs/output_file_with_header') as f:
            output = f.read()
        self.assertEqual(output, expected_output)

    def test_parse_fixed_width_file_include_header_false(self):
        spec = {
            "ColumnNames": [
                "f1",
                "f2",
                "f3",
                "f4",
                "f5",
                "f6",
                "f7",
                "f8",
                "f9",
                "f10"
            ],
            "Offsets": [
                "5",
                "12",
                "3",
                "2",
                "13",
                "7",
                "10",
                "13",
                "20",
                "13"
            ],
            "FixedWidthEncoding": "windows-1252",
            "IncludeHeader": "False",
            "DelimitedEncoding": "utf-8"
        }
        expected_output = "12345,abcdefghijkl,789,01,234567890123a,bcd1234,567   1234,56789012345,,\n"
        parse_fixed_width_file('specs/input_file_no_header', 'specs/output_file_no_header', spec)
        with open('specs/output_file_no_header') as f:
            output = f.read()
        self.assertEqual(output, expected_output)

    def test_parse_fixed_width_file_different_delimited_encoding(self):
        spec = {
            "ColumnNames": [
                "f1",
                "f2",
                "f3",
                "f4",
                "f5",
                "f6",
                "f7",
                "f8",
                "f9",
                "f10"
            ],
            "Offsets": [
                "5",
                "12",
                "3",
                "2",
                "13",
                "7",
                "10",
                "13",
                "20",
                "13"
            ],
            "FixedWidthEncoding": "windows-1252",
            "IncludeHeader": "True",
            "DelimitedEncoding": "iso-8859-1"
        }
        expected_output = "f1,f2,f3,f4,f5,f6,f7,f8,f9,f10\n"
        parse_fixed_width_file('specs/input_file_coding', 'specs/output_file_coding', spec)
        with open('specs/output_file_coding') as f:
            output = f.read()
        self.assertEqual(output, expected_output)
