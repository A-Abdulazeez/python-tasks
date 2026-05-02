from unittest import TestCase
import pybank

class TestValidateUserEmail (TestCase):

	def test_that_validate_email_exists(self): 
		pybank.user_email("adebex@gmail.com")
		
	def test_that_validate_email_is_more_than_8_characters_return_True(self):  
		is_valid = pybank.user_email("adebex@gmail.com")
		self.assertTrue(is_valid)
		
	def test_that_validate_email_is_less_than_8_characters_return_False(self):  
		is_valid = pybank.user_email("ade@.c") 
		self.assertFalse(is_valid)

	def test_that_valid_email_contains_special_character(self): 
		is_valid = pybank.user_email("adebex@gmail.com") 
		self.assertTrue(is_valid)

	def test_that_valid_email_does_not_start_with_special_character(self): 
		message = pybank.user_email("@adebex@gmail.com") 
		self.assertEqual(message, "invalid email")

	def test_that_valid_email_does_not_end_with_special_character(self): 
		message = pybank.user_email("@adebex@gmail.com") 
		self.assertEqual(message, "invalid email")

class TestCalculateBalance (TestCase):
	def test_that_validate_email_exists(self): 
		pybank.calculate_balance([0])
	def test_that_the_balance_is_giving_positive_result_for_deposit(self):
		actual = pybank.calculate_balance([0, 200, 300])
		self.assertEqual(actual, 500)
	def test_that_the_balance_is_giving_negative_result_for_withdrawal(self):
		actual = pybank.calculate_balance([0, 200, -100])
		self.assertEqual(actual, 100)
	def test_that_the_empty_list_is_returning_negative_result_for_withdrawal(self):
		actual = pybank.calculate_balance([0])
		self.assertEqual(actual, 0)
		
class TestStrongPassword (TestCase):
	def test_that_strong_password_exists(self): 
		pybank.strong_password("passwpord")
	def test_that_password_is_more_than_8_characters(self):
		is_valid = pybank.strong_password("passwpord")
		self.assertTrue(is_valid)
	def test_that_password_is_less_than_8_characters(self):
		is_valid = pybank.strong_password("pass")
		self.assertFalse(is_valid)
		
class TestApplyInterest (TestCase):
	def test_that_apply_interest_exists(self):
		pybank.apply_interest(1000, 2, 2)
	def test_that_year_is_less_than_one(self):
		is_valid = pybank.apply_interest(1000, 2, 0)
		self.assertFalse(is_valid)	
	def test_that_rate_is_a_negative_number(self):
		is_valid = pybank.apply_interest(1000, -1, 1)
		self.assertFalse(is_valid)
	def test_that_year_is_more_than_one(self):
		is_valid = pybank.apply_interest(1000, 2, 1)
		self.assertTrue(is_valid)	
	def test_that_rate_is_a_positive_number(self):
		is_valid = pybank.apply_interest(1000, 1, 1)
		self.assertTrue(is_valid)
	def test_that_compound_interest_ives_correct_value(self):
		expected = pybank.apply_interest(1000, 1, 1)
		self.assertEqual(expected, 
