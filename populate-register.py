from App.bank_account import Bank_Account

#acc = Bank_Account('Kamil', 1234, 222330)

def populate_deposit(account: Bank_Account, num):
    for s in range(100, num, 50):        
        account.deposit(s)
def populate_withdraw(account: Bank_Account, num):
    for s in range(100, num, 30):        
        account.withdraw(s)


#populate_deposit(acc, 1000)
#populate_withdraw(acc, 600)
    
 
 
