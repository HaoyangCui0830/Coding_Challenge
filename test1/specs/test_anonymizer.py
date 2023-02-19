import unittest
import sys
from unittest.mock import patch

class Mockfaker:
    class Faker:
        def first_name(self):
            return 'John'
        
        def last_name(self):
            return 'Doe'

        def address(self):
            return '123 Main St Apt 4 Anytown, USA'

sys.modules['faker'] = Mockfaker()
from src.anonymizer import Anonymizer

class TestAnonymizer(unittest.TestCase):
    def setUp(self):
        self.anonymizer = Anonymizer()
        self.faker = Mockfaker.Faker()

    def test_first_name(self):
        with patch.object(self.faker, 'first_name') as mock_first_name:
            mock_first_name.return_value = 'John'
            self.assertEqual(self.anonymizer.first_name(), 'John')

    def test_last_name(self):
        with patch.object(self.faker, 'last_name') as mock_last_name:
            mock_last_name.return_value = 'Doe'
            self.assertEqual(self.anonymizer.last_name(), 'Doe')

    def test_address(self):
        with patch.object(self.faker, 'address') as mock_address:
            mock_address.return_value = '123 Main St\nApt 4\nAnytown, USA'
            self.assertEqual(self.anonymizer.address(), '123 Main St Apt 4 Anytown, USA')
