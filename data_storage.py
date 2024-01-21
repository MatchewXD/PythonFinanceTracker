income = []
expence = []

def store_income(amount, date, category):
  income.append({'value': amount, 'date': date, 'category': category})

def store_expence(amount, date, category):
  expence.append({'value': amount, 'date': date, 'category': category})