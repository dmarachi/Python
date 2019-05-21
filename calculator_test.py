import unittest
import calculator

class calculatorTests(unittest.TestCase):

	def test_add_method(self):
		result = calculator.add(2,2)
		self.assertEqual(4, result)

	def test_subtract_method(self):
		result = calculator.subtract(2,2)
		self.assertEqual(result, 0)

	def test_multiply_method(self):
		result = calculator.multiply(2,2)
		self.assertEqual(4, result)

	def test_divid_method(self):
		result = calculator.divid(2,2)
		self.assertEqual(1, result)



if __name__ == "__main__":
	unittest.main()