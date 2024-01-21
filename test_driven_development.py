import unittest
from data_storage import store_expence, store_income, income, expence

class TestDataStorage(unittest.TestCase):

  def setUp(self):
    expence.clear()
    income.clear()

  def test_income_storage(self):
    store_income(100, "01/01/2024", "savings")
    self.assertEqual(len(income), 1)

    expected_income = {'value' : 100, 'date':"01/01/2024", 'category':"savings" }
    self.assertDictEqual(income[0], expected_income)

  def test_expence_storage(self):
    store_expence(99, '01/01/2024', 'checking')
    self.assertEqual(len(expence), 1)

    expected_expence = {'value' : 99, 'date' : '01/01/2024', 'category' : 'checking'}
    self.assertDictEqual(expence[0], expected_expence)



if __name__ == '__main__':
  unittest.main()