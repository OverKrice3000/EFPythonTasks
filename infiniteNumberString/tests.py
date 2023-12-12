import unittest

from main import find_digital_string_position_in_infinite_digital_string


class TestCorrectness(unittest.TestCase):

    def test_pass_fixed_tests(self):
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("456") , 3,"...3456...")
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("454") , 79,"...444546...")
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("455") , 98,"...545556...")
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("456") , 3,"...3456...")
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("454") , 79,"...444546...")
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("455") , 98,"...545556...")
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("910") , 8,"...7891011...")
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("9100") , 188,"...9899100...")
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("99100") , 187,"...9899100...")
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("00101") , 190,"...9899100...")
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("001") , 190,"...9899100...")
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("00") , 190,"...9899100...")
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("123456789") , 0)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("1234567891") , 0)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("123456798") , 1000000071)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("10") , 9)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("53635") , 13034)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("040") , 1091)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("11") , 11)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("99") , 168)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("667") , 122)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("0404") , 15050)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("949225100") , 382689688)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("58257860625") , 24674951477)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("3999589058124") , 6957586376885)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("555899959741198") , 1686722738828503)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("01") , 10)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("091") , 170)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("0910") , 2927)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("0991") , 2617)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("09910") , 2617)
        self.assertEqual(find_digital_string_position_in_infinite_digital_string("09991") , 35286)