import unittest
import tax

class taxTests(unittest.TestCase):

	def test_calculate_tax_method(self):

		self.assertEqual(tax.calculate_tax(100), 15)

if __name__ == "__main__":
	unittest.main()