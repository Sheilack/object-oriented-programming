# oop checkpoint
class Account:
  def __init__(self, account_holder, account_number, account_balance):
    self.account_holdder = account_holder
    self.account_number = account_number
    self.account_balance = account_balance

  def deposit(self, amount):
    if amount > 0.00:
      self.account_balance = self.account_balance + amount
      print(f"Deposit of {amount} successful. New balance is {self.account_balance}")
    else:
      print("Invalid deposit amount!")


  def withdraw(self, amount):
    if self.account_balance >= amount:
      self.account_balance = self.account_balance - amount
      print(f"Withdrawal of {amount} successful. New balance is {self.account_balance}")
    else:
      print("Insufficient funds!")


  def check_balance(self):
    print(f"Your balance is {self.account_balance}")


my_account = Account("Sheila Koskei", "20462233978", 616500.75)


my_account.deposit(500000.00)
my_account.check_balance()

my_account.deposit(-50900.00)
my_account.check_balance()

my_account.withdraw(120000.00)
my_account.check_balance()
