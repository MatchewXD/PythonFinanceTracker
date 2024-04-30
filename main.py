from data_storage import store_income, store_expense, income, expense

print('Financial Tracker initializing')
username = ''
task = ''

def main():
  print('Welcome to the console-based financial tracker. What should I call you?')
  username = input()
  print('\n Hello ' + username + '''
  What can I help you with today?''')
  user_task_options()

def user_task_options():
  print('''Options
        add_income
        add_expense
        view_summary
        exit
        ''')
  task = input()
  handle_task_option(task)

def handle_task_option(task):
  if task != 'exit':
    if task == 'add_income':
      print('what would you like to add? (amount, date, category)')
      add_income()
    elif task == 'add_expense':
      print('What would you like to add? (amount, date, category)')
      add_expense()
    elif task == 'view_summary':
      view_summary()
    else:
      print('Invalid input, ')
      user_task_options()

def add_income():
  users_income = input()
  # check if the input is amount, date, category
  # convert the data into a dictionary
  parsed_user_income = parse_user_input(users_income)
  # run function store_income with the dictionary
  store_income(parsed_user_income)
  print('\n Your Income has been Stored')
  user_task_options()

def add_expense():
  users_expense = input()
  parsed_user_expense = parse_user_input(users_expense)
  store_expense(parsed_user_expense)
  print('\n Your Expense has been Stored')
  user_task_options()

def view_summary():
  if len(income) == 0 and len(expense) == 0:
    print('There are not transactions')
    user_task_options()
    return

  income_list = create_transaction_list(income)
  expense_list = create_transaction_list(expense)

  print('''\nIncome Summary
Amount --- Date --- Category''')
  print(income_list)
  print("""Expense Summary
Amount --- Date --- Category""")
  print(expense_list)

  print('\n \n \n ')
  print('Type enter to return to the options menu')
  temp_input = input()
  user_task_options()

def create_transaction_list(transaction_summary):
  final_list = ''
  for i in transaction_summary:
    final_list += f'- {i['value']}  {i['date']}  {i['category']}'
    if i != len(transaction_summary):
      final_list += '\n'

  return final_list




def parse_user_input(users_input):
  parts = 0 # what part of the string? amount = 0, date = 1 or category = 2
  amount = 0
  date = ''
  category = ''
  current_string = ''

  # take a string and separate it into parts depending on a ,
  current_iteration = 1
  for current_letter in users_input:
    if current_letter == ' ':
      current_iteration += 1
      continue
    if current_letter == ',':
      # if part == 0 convert string to number
      if parts == 0:
        amount = float(current_string)
        current_string = ''
        parts += 1
      # store the current string in variable. move to the next variable
      elif parts == 1:
        date = current_string
        current_string = ''
        parts += 1
      else:
        category = current_string
        current_string = ''
        parts += 1

    else:
      current_string += current_letter
      if current_iteration == len(users_input):
        category = current_string
    current_iteration += 1
  # return a dictionary with all the parts
  return {'value' : amount, 'date' : date, 'category' : category}

if __name__ == "__main__":
    main()