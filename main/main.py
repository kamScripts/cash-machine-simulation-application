from bank_account import Bank_Account
from cash_machine import CashMachine
atm = CashMachine()
acc = Bank_Account(name='Kamil', pin=1234, acc_number=569089)

if __name__ == "__main__":
    atm.user_interface(acc)
    