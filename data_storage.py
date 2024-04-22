income = []
expence = []

def store_income(user_income):
  income.append(user_income)

def store_expence(amount, date, category):
  expence.append({'value': amount, 'date': date, 'category': category})