# 01-multiples-of-3-or-5/test_multiples.py - Check small sums and the answer
# Usage: python3 -m unittest test_multiples -v

# Use Python's built-in test tools and the solution function
import unittest
from multiples import sum_multiples


# Check the upper limit, shared multiples, and the full problem
class MultiplesTests(unittest.TestCase):
    # Small sums make the numbers included and excluded easy to check
    def test_small_sums(self):
        for limit, expected in (
            (0, 0),
            (3, 0),
            (4, 3),
            (6, 8),
            (10, 23),
        ):
            with self.subTest(limit=limit):
                self.assertEqual(sum_multiples(limit), expected)

    # Count 15 once even though it is divisible by both 3 and 5
    def test_shared_multiple(self):
        self.assertEqual(sum_multiples(16), 60)

    # Check the default limit against a separate arithmetic calculation
    def test_answer(self):
        self.assertEqual(sum_multiples(), 233168)


# Run the same checks when called directly
if __name__ == "__main__":
    unittest.main()
