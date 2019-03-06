
import unittest
import main


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        print('start testing')

    def test_with_range(self):
        self.assertEqual(main.fizzbuzz(range(1, 21)),
                         [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
                          'Fizz', 'Buzz', 11, 'Fizz', 13, 14,
                          'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz'])

    def test_normal(self):
        self.assertEquals(main.fizzbuzz([1, 27, 45, 4, 7, 8, 9, 0]),
                          [1, 'Fizz', 'FizzBuzz', 4, 7, 8, 'Fizz', 'FizzBuzz'])

    def test_empty(self):
        self.assertListEqual(main.fizzbuzz([]), [])

    def tearDown(self):
        print('end')

if __name__ == '__main__':
    unittest.main()