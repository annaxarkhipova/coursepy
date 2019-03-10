import unittest
import roman


class TestRoman(unittest.TestCase):

    def setUp(self):
        print('start testing')


    def test_normal(self):
        r = to_roman(30)
        self.assertEqual(r, 'XXX')


    def tearDown(self):
        print('end')

if __name__ == '__main__':
    unittest.main()