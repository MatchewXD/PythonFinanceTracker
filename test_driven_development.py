import unittest
from data_storage import store_expense, store_income, income, expense
from main import parse_user_input

class TestDataStorage(unittest.TestCase):

  def setUp(self):
    expense.clear()
    income.clear()

  def test_income_storage(self):
    store_income({'value' : 100, 'date':"01/01/2024", 'category':"savings" })
    self.assertEqual(len(income), 1)

    expected_income = {'value' : 100, 'date':"01/01/2024", 'category':"savings" }
    self.assertDictEqual(income[0], expected_income)

  def test_expense_storage(self):
    store_expense({'value':99, 'date':'01/01/2024', 'category':'checking'})
    self.assertEqual(len(expense), 1)

    expected_expence = {'value' : 99, 'date' : '01/01/2024', 'category' : 'checking'}
    self.assertDictEqual(expense[0], expected_expence)

class TestIncomeStoring(unittest.TestCase):

  def test_convert_string_to_dictionary(self):
    expected_result = {'value' : 99, 'date' : '01/01/2024', 'category' : 'Savings'}
    self.assertDictEqual(parse_user_input('99, 01/01/2024, Savings'), expected_result)

  # def test_check_user_input(self):
    # User input should be amount, date, category. Any other input returns an error


if __name__ == '__main__':
  unittest.main()