datastorage = []

def storage(amount, date, category):
  datastorage.append({'value': amount, 'date': date, 'category': category})


storage(100, "01/18/2024", "savings")
storage(300, "01/20/2024", "computer")

print(datastorage)
