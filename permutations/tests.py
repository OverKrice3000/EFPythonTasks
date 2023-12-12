import unittest

from main import totally_good


class TestCorrectness(unittest.TestCase):
    def test_tot1ally_good_basic_small(self):
        self.assertEqual(totally_good('ABC', []), 6)
        self.assertEqual(totally_good('ABCD', []), 24)
        self.assertEqual(totally_good('ABCDE', []), 120)
        self.assertEqual(totally_good('ABCD', ['AB']), 18)
        self.assertEqual(totally_good('ABCD', ['BA']), 18)
        self.assertEqual(totally_good('ABCD', ['A']), 0)
        self.assertEqual(totally_good('ABC', ['AB', 'CA']), 3)

    def test_totally_good_simple_small(self):
        self.assertEqual(totally_good('ABCD', ['A', 'BC']), 0)
        self.assertEqual(totally_good('ABCD', ['AB', 'CD']), 14)
        self.assertEqual(totally_good('ABCDE', ['AB', 'CD']), 78)
        self.assertEqual(totally_good('ABCDE', ['AB', 'CDE']), 92)

    def test_totally_good_first_complex(self):
        self.assertEqual(totally_good('ABCD', ['A', 'AC']), 0)
        self.assertEqual(totally_good('ABCDE', ['AB', 'BC']), 78)
        self.assertEqual(totally_good('ABCDE', ['ABC', 'BE']), 90)
        self.assertEqual(totally_good('ABCDEF', ['FC', 'CAE']), 582)
        self.assertEqual(totally_good('ABCDEF', ['FC', 'BC', 'EC']), 360)
        self.assertEqual(totally_good('ABCDEF', ['FC', 'BC', 'EC', 'BE']), 288)
        self.assertEqual(totally_good('ABCDEFGH', ['FC', 'ABD', 'EHG']), 34098)
        self.assertEqual(totally_good('ABCDEFGH', ['ABCD', 'BCDE']), 40104)
        self.assertEqual(totally_good('ABCDEFGH', ['ABCD', 'BCDEFG']), 40196)

    def test_totally_good_second_complex(self):
        self.assertEqual(totally_good('ABCDE', ['ABC', 'CD', 'DEA']), 89)
        self.assertEqual(totally_good('ABCDEFGH', ['ABCD', 'CDEFG', 'FGH']), 39469)
        self.assertEqual(totally_good('ABCDEFGH', ['AB', 'BCD', 'CDE', 'DEFG', 'GH']), 29966)
        self.assertEqual(totally_good('ABCDEFGH', ['ABCD', 'CDEF', 'EFGH', 'GHAB']), 39864)

    def test_totally_good_third_complex(self):
        self.assertEqual(totally_good('ABCDE', ['ABC', 'BE', 'ADC']), 86)
        self.assertEqual(totally_good('ABCDE', ['ABC', 'BE', 'EA', 'CB']), 60)
        self.assertEqual(totally_good('ABCDEFGH', ['AB', 'BC', 'FG', 'GH']), 24024)
        self.assertEqual(totally_good('ABCDEFGH', ['AB', 'BC', 'CDE', 'FG', 'GH']), 23662)
        self.assertEqual(totally_good('ABCDEFGH', ['ABC', 'CD', 'DEFG', 'FGH']), 34023)

    def test_totally_good_tricky_cases(self):
        self.assertEqual(totally_good('ABCDEFGH', ['ABCDE', 'BCD']), 39600)
        self.assertEqual(totally_good('ABCDEFGH', ['ABCDEF', 'BCDE', 'DE']), 35280)
        self.assertEqual(totally_good('ABCDEFGH', ['ABCDEF', 'BCDEF', 'BCDE', 'CDE', 'DE']), 35280)
        self.assertEqual(totally_good('ABCDEFGH', ['ABH', 'CH', 'DEH', 'FGH']), 33120)
        self.assertEqual(totally_good('ABCDEFGH', ['ABH', 'CBH', 'DEBH', 'FGBH']), 38640)

    def test_totally_good_more_tricky_cases(self):
        self.assertEqual(totally_good('ABCDEFG', ['BCDE', 'CE', 'CF', 'CB', 'EB']), 2376)
        self.assertEqual(totally_good('ABCDEFGH', ['AB', 'BC', 'CDE', 'BCD', 'DEFG', 'GH']), 26761)
        self.assertEqual(totally_good('ABCDEFGH', ['AB', 'BC', 'CDE', 'BCD', 'DEFG', 'GH', 'EF']), 23662)
        self.assertEqual(totally_good('ABCDEFGH', ['AB', 'BC', 'CDE', 'BCD', 'DEFG', 'GH', 'EF', 'HCBG']),
                           23566)
        self.assertEqual(
            totally_good('ABCDEFGH', ['AB', 'BC', 'CDE', 'BCD', 'DEFG', 'GH', 'EF', 'HCBG', 'CB']), 19942)
        self.assertEqual(
            totally_good('ABCDEFGH', ['BCDEFG', 'CDEF', 'DE', 'BCD', 'EFG', 'CD', 'EF', 'FEDC', 'ABC', 'ABCD']),
            26694)
        self.assertEqual(totally_good('ABCDEFGH', ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']), 36000)

    def test_totally_good_larger_alphabets(self):
        self.assertEqual(totally_good('ABCDEFGHIJKL', []), 479001600)
        self.assertEqual(
            totally_good('ABCDEFGHI', ['AB', 'CD', 'EFGH', 'BC', 'FG', 'BH', 'ABCDE', 'DAC', 'ADG', 'IFBC']),
            194520)
        self.assertEqual(totally_good('ABCDEFGHI',
                                        ['ABCDEF', 'CDFIBA', 'HIFDCA', 'GHFCAB', 'ABCDIHG', 'EFGCDA', 'IHEFDCA',
                                         'HAIE', 'FEBHDA', 'ACHIEBF', 'CE', 'BADICE']), 321678)
        self.assertEqual(
            totally_good('ABCDEFGHIJ', ['AB', 'CD', 'EFGH', 'BC', 'FG', 'BH', 'ABCDE', 'DAC', 'ADG', 'IFBC']),
            2082240)
