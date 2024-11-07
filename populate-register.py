from App.bank_account import Bank_Account

acc = Bank_Account(name='Kamil', pin=1111, acc_number=222330)

def populate_deposit(account: Bank_Account, num):
    for s in range(1000, num, 100):       
        account.deposit(s)
def populate_withdraw(account: Bank_Account, num):
    for s in range(100, num, 30):        
        account.withdraw(s)


populate_deposit(acc, 2000)
populate_withdraw(acc, 800)
    
 
 
