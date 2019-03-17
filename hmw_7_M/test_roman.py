import unittest
from coursepy import roman


class TestRoman(unittest.TestCase):

    def setUp(self):
        print('start testing')


    def test_variety(self):
        self.assertEqual(roman.to_roman(30), 'XXX')
        self.assertEqual(roman.to_roman(40), 'XXXX')
        self.assertEqual(roman.to_roman(20), 'XX')

    def test_err(self):
        with self.assertRaises(ValueError):
            roman.to_roman('string', 5001)


    def tearDown(self):
        print('end')

if __name__ == '__main__':
    unittest.main()