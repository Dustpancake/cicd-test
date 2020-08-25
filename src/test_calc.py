import unittest
import calc 

class TestCalc(unittest.TestCase):

	def test_add_integers(self):
		result = calc.addn("1", "2", "3")
		self.assertEqual(result, 6)

	def test_add_floats(self):
		result = calc.addn('10.5', "4")
		self.assertEqual(result, 14.5)

	def test_add_string(self):
		result = calc.addn("hello ", "world")
		self.assertEqual(result, "hello world")

	def test_add_string_and_integer(self):
		result = calc.addn("hello", "1")
		self.assertEqual(result, "hello1")

	def test_add_string_and_float(self):
		result = calc.addn("hello", "12.5", "0.5", "world")
		self.assertEqual(result, "hello12.50.5world")

if __name__ == '__main__':
	unittest.main()
