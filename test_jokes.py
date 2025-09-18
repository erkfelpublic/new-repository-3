import unittest
from joke import jokes

class TestJokes(unittest.TestCase):
    def test_number_of_jokes(self):
        """Test that there are exactly 42 jokes."""
        self.assertEqual(len(jokes), 42)

if __name__ == '__main__':
    unittest.main()
