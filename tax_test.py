import unittest
import tax

class taxTests(unittest.TestCase):

	def test_calculate_tax_method(self):

		self.assertEqual(tax.calculate_tax(100), 15)
		self.assertEqual(tax.calculate_tax(47630), 7144.5)
		self.assertEqual(tax.calculate_tax(95259), 16908.945)
		self.assertEqual(tax.calculate_tax(147667), 30534.08)
		self.assertEqual(tax.calculate_tax(210371), 48719.16)
		self.assertEqual(tax.calculate_tax(8710371), 2853719)
		self.assertEqual(tax.calculate_tax(85259), 14858.945)
		self.assertEqual(tax.calculate_tax(207667), 47935)

if __name__ == "__main__":
	unittest.main()
