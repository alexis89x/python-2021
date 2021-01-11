import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_fail(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis ERROR')

if __name__ == '__main__':
    unittest.main()

# Assert Equal, Not Equal, True, False, In, NotIn