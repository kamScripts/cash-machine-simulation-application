from bank_account import Bank_Account
from cash_machine import CashMachine
atm = CashMachine()
acc = Bank_Account(name='Kamil', pin=1234, acc_number=569089)
acc.ledger =5000


atm.user_interface(acc)
