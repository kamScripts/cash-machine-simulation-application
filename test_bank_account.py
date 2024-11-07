import unittest
import os
from App.bank_account import Bank_Account

class TestBankAccount(unittest.TestCase):
    def setUp(self):        
        self.account = Bank_Account('Alice Smith', 1234, 9595959)
    def tearDown(self):        
        os.remove(self.account.transaction_history)
        os.remove(self.account.balance_file)
    def test_initialization(self):
        print('test_initialization')
        self.assertEqual(self.account.name, "Alice Smith")
        self.assertEqual(self.account.pin, 1234)
        self.assertEqual(self.account.acc_number, 9595959)
        self.assertEqual(self.account.transaction_history, ".\\App\\data\\9595959.txt")
        self.assertEqual(self.account.balance_file, ".\\App\\data\\9595959_b.txt") 
    def test_balance_getter_new_account(self):
        print('test_balance_getter_new_account')
        self.assertEqual(self.account.balance, 0)
    def test_balance_setter(self):
        print('test_balance_setter')
        self.account.balance =50
        self.account.balance = 30
        self.account.balance = -20
        self.assertEqual(self.account.balance, 60)  
    def test_deposit(self):
        print('test_deposit')
        self.account.deposit(500)
        self.account.deposit(350)
        self.account.deposit(150)
        self.assertEqual(self.account.balance, 1000)
    def test_withdraw_valid(self):
        print('test_withdraw_valid')
        self.account.deposit(500)        
        self.assertTrue(self.account.withdraw(250))
        self.assertEqual(self.account.balance, 250)
    def test_withdraw_not_valid_empty_account(self):
        print('test_withdraw_not_valid_empty_account')
        self.assertEqual(self.account.balance, 0)
        self.assertFalse(self.account.withdraw(100))
    def test_withdraw_not_valid_money_in(self):
        print('test_withdraw_not_valid_money_in')
        self.account.deposit(500)
        self.assertFalse(self.account.withdraw(600))
    def test_transfer_history(self):
        print('test_transfer_history')
        self.account.deposit(500)
        self.account.withdraw(100)
        self.account.deposit(350)
        self.account.withdraw(100) 
        history = self.account.transfer_history()     
        self.assertEqual(history, ['-100.00', '350.00', '-100.00', '500.00'])
    def test_check_funds(self):
        print('test_check_funds')
        self.account.deposit(500)
        self.assertTrue(self.account.check_funds(400))
        self.assertFalse(self.account.check_funds(501))
    
    
    
       
        
    
        
        


if __name__ == "__main__":
    unittest.main()
