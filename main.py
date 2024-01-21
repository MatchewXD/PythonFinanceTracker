print('Financial Tracker initializing')
username = ''
task = ''

def main():
  print('Welcome to the console-based financial tracker. What should I call you?')
  username = input()
  print('Hello ' + username + '''
  What can I help you with today?''')
  user_task_options()

def user_task_options():
  print('''Options
        add_income
        add_expense
        view_summary
        ''')
  task = input()
  handle_task_option(task)

def handle_task_option(task):
  if task != 'exit':
    if task == 'add_income':
      print('what would you like to add? (amount, date, category)')
    elif task == 'add_expense':
      print('What would you like to add? (amount, date, category)')
    elif task == 'view_summary':
      print('Here is a summary: \n')
    else:
      print('Invalid input, ')
      user_task_options()



if __name__ == "__main__":
    main()