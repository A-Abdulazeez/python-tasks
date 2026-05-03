import unittest
import nairaexchange
class TestNairaExchange(unittest.TestCase):
	def test_test_naira_exchange_exists(self):
		nairaexchange.naira_exchange(1.2)
	def test_test_naira_exchange_return_correct_result_with_a_float_digit(self):
		actual = nairaexchange.naira_exchange(1.2)
		expected = 1860.0
		self.assertEqual(actual, expected)
	def test_test_naira_exchange_return_correct_result_with_a_int_digit(self):
		actual = nairaexchange.naira_exchange(1)
		expected = 1550
		self.assertEqual(actual, expected)
	def test_test_naira_exchange_return_invalid_data_type_with_wrong_input(self):
		actual = nairaexchange.naira_exchange("musa")
		expected = "invalid input"
		self.assertEqual(actual, expected)
