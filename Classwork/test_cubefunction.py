import unittest
import cubefunction
class TestCubeFunction(unittest.TestCase):
	def test_test_cube_function_exists(self):
		cubefunction.cube(3)
	def test_test_cube_function_return_correct_result(self):
		actual = cubefunction.cube(10)
		expected = 1000
		self.assertEqual(actual, expected)
	def test_test_cube_function_return_invalid_data_type_with_wrong_input(self):
		actual = cubefunction.cube("musa")
		expected = "invalid input"
		self.assertEqual(actual, expected)
