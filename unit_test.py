import unittest
from main import reverse_word

class TestWord(unittest.TestCase):
    
    def test_reverse(self):
        self.assertEqual(reverse_word('Hello'), 'olleH')
        self.assertEqual(reverse_word('World'), 'dlroW')
        self.assertEqual(reverse_word("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc")


if __name__ == '__main__':
    unittest.main()
    