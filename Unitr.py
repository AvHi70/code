import unittest
from Interface import *


class TestInterface(unittest.TestCase):
    def test_search(self):
        search_entry.insert(0, 'Abhishek')
        entry_filter.set('First name')

        test_array = [('Abhishek', 'Chaudhary', 190019, 'Kota', '9865780341', 'Bachlor'),
                      ('Suraj', 'Mainali', 5642310,  'Budhanilakantha', '98726462', 'Bsc'),
                      ('Utsav', 'Shrestha', 1234561, 'Basbari', '98726462', 'Nursing'),
                      ('Grishma', 'Newa', 123456, 'Asan', '9861773624', 'Bsc')]

        expected_result = [('Abhishek', 'Chaudhary', 190019, 'Kota', '9865780341', 'Bachlor')]

        my_list = self.search(test_array)
        self.assertEqual(my_list, expected_result)

    def test_sort(self):
        test_sort.set('ID No.')
        array_test = [('Abhishek', 'Chaudhary', 190019, 'Kota', '9865780341', 'Bachlor'),
                      ('Suraj', 'Mainali',5642310,  'Budhanilakantha', '98726462', 'Bsc'),
                      ('Utsav', 'Shrestha', 1234561, 'Basbari', '98726462', 'Nursing'),
                      ('Grishma', 'Newa', 123456, 'Asan', '9861773624', 'Bsc')]

        expected_result = [('Abhishek', 'Chaudhary', 190019, 'Kota', '9865780341', 'Bachlor'),
                           ('Grishma', 'Newa', 123456, 'Asan', '9861773624', 'Bsc'),
                           ('Suraj', 'Mainali',5642310,  'Budhanilakantha', '98726462', 'Bsc'),
                           ('Utsav', 'Shrestha', 1234561, 'Basbari', '98726462', 'Nursing')]
        quick_sort(array_test, 0, len(array_test) - 1)
        self.assertEqual(array_test, expected_result)


Interface = Tk()
Interface.main()
