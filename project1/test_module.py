import unittest
from arithmetic_arranger import arithmetic_arranger


# the test case
class UnitTests(unittest.TestCase):
    def test_arrangement(self):
        actual = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
    
if __name__ == "__main__":
    unittest.main()
