from bank_account import Bank_Account
from cash_machine import CashMachine
atm = CashMachine()
acc = Bank_Account('Kamil', 1234, 569089)


acc.ledger =100
acc.ledger =500
atm.user_interface(acc)
