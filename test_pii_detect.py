import unittest
<<<<<<< HEAD
from pii_detect import find_city_state, find_account_number


class Comp410TestPII(unittest.TestCase):
    def test_find_city_state(self):
        # Test a single city and state
        result_list = find_city_state('I live in Houston, TX')
        self.assertEqual(result_list[0], 'Houston, TX')

        # Test two cities and states
        result_list = find_city_state('I have lived in Houston, TX and Dallas, TX')
        self.assertEqual(result_list[0], 'Houston, TX')
        self.assertEqual(result_list[1], 'Dallas, TX')

        # Test beginning of string
        result_list = find_city_state('Houston, TX is a great city')
        self.assertEqual(result_list[0], 'Houston, TX')

        # Test middle of string
        result_list = find_city_state('I lived in Houston, TX for 10 years')
        self.assertEqual(result_list[0], 'Houston, TX')

        # Test an invalid case where the state is not capitalized
        result_list = find_city_state('I live in houston, TX')
        # result_list should be empty
        self.assertFalse(result_list)

        # Test a two-word city
        result_list = find_city_state('I live in New York, NY')
        self.assertEqual(result_list[0], 'New York, NY')

        # Test an invalid state abbreviation
        # TODO - it is currently not a requirement to support invalid state abbreviations
        # result_list = find_city_state('I live in Houston, AA')
        # result_list should be empty
        # self.assertFalse(result_list)

    def test_find_account_number(self):
        # Test a single account number
        result_list = find_account_number('My account number is 1234567890')
        self.assertEqual(result_list[0], '1234567890')

        # Test account number at start of string
        result_list = find_account_number('1234567890 is my account number')
        self.assertEqual(result_list[0], '1234567890')

        # Test account number in middle of string
        result_list = find_account_number('My account 1234567890 is not active')
        self.assertEqual(result_list[0], '1234567890')

        # Test account number at end of string
        result_list = find_account_number('My account number is 1234567890')

        # Test multiple account numbers
        result_list = find_account_number('My account numbers are 1234567890 and 0987654321')
        self.assertEqual(result_list[0], '1234567890')
        self.assertEqual(result_list[1], '0987654321')

        # Test account number with dashes
        result_list = find_account_number('My account number is 123-456-7890')
        # Dashes are not supported
        self.assertFalse(result_list)

=======
import re
from pii_detect import show_aggie_pride


class Comp410TestCase(unittest.TestCase):
    def test_show_aggie_pride(self):
        # show_aggie_pride() returns a list of slogans
        result_list = show_aggie_pride()

        # make sure a list is returned
        self.assertIsInstance(result_list, list)

        # make sure there is at least one aggie in the list
        has_aggie = False
        for slogan in result_list:
            if 'Aggie' in slogan:
                has_aggie = True
                break
        self.assertTrue(has_aggie, 'No Aggie slogans found')

        # make sure the list has the expected number of slogans
        self.assertEqual(15, len(result_list), 'Unexpected number of slogans')

    def test_starts_with_test(self):
        # In order to run as a test case the method name must start with test
        # This test checks to make sure all defines within this file start with test
        # This is a common mistake that can cause tests to be skipped
        with open('test_pii_detect.py') as f:
            for line in f:
                # make sure everything that looks like a method name starts with test
                m = re.search(r'\s*def (\w+)', line)
                if m:
                    self.assertTrue(m.group(1).startswith('test'),
                                    'Method name does not start with test: def ' + m.group(1))

    def test_ap_ww(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[0], 'Aggie Pride - Worldwide')

    def test_aggie_do(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[1], 'Aggies Do!')

    def test_aggies_go(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[2], 'Go Aggies')

    def test_aggie_proud(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[3], 'We are Aggies!')

    def test_thats_on_1891(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[4], 'Thats on 1891!')

    def test_whataggiesdo(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[5], 'Thats What Aggies Do!')

    def test_letsgoaggies(self):
        result_list = show_aggie_pride()
        self.assertEqual(result_list[6], 'Lets Go Aggies!')

    def test_aggies_skate(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[7], 'Aggies skate, Aggies grind!')

    def test_show_aggies(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[8], 'Show em what Aggies do')



    def test_aggie_born(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[9], 'Aggie born, Aggie bred')

    def test_aggies_stick(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[10], 'Aggies stick together')
        
    def test_NeverUnderestimate_MoveForward(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[11], 'Never Ever Underestimate An Aggie. Move Forward With Purpose.')

    def test_aggies_rock(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[12], 'Aggies rock')

    def test_aggies_think_do(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[13], 'Aggies think, Aggies do!')
>>>>>>> aacbb6daf15577880a245dfcbc1590ce526ed450

    def test_aggie_pride(self):
        # make sure each slogan is in the expected position
        # merge errors are a common reason for failures
        result_list = show_aggie_pride()
        self.assertEqual(result_list[14] == 'Can I Get an Aggie Pride?')
        

if __name__ == '__main__':
    unittest.main()
