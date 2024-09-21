class CashMachine:
    
    def user_interface(self, account):
        self.verify_pin(account)
        print(f'Hi, {account.name}.')
        while(True):
            print('''
Choose one of the following options:
        1. Check Balance
        2. Check Deposit history
        3. Check Withdrawal history
        4. Withdraw Funds
        5. Deposit Funds
        6. Exit
''')
            choice = input('Type 1-5 to choose following option: ')
            match choice:
                case '1': 
                    print(f'Account Balance: £{account.check_balance():.2f}')
                    
                case '2':                    
                    print(f'Deposit History: \n{account.deposit_history()}')
                case '3':
                    print(f'Withdrawals History: \n{account.withdrawal_history()}')
                case '4':
                    amount = float(input('Amount to withdraw: '))
                    boolean = account.withdraw(amount)
                    if(boolean):
                        print('You successfully withdrew funds')
                    else:
                        print('You have not enough funds')
                case '5':
                    amount = float(input('Amount to deposit: '))
                    account.deposit(amount)
                    print(f'You successfully deposited £{amount}.')
                case '6':
                    print("Thank you for using CASH MACHINE.\n Don't forget Your Card")
                    return
            
        
            
            
    def verify_pin(self, account):
        
        while(True):
            user_pin = int(input('Please enter pin to log in:'))
            if self.check_pin(account, user_pin):                       
                return True
            else:
                print('wrong pin')
                
    def check_pin(self, account, pin_to_verify):
        if account.pin == pin_to_verify:
            return True
        else:
            return False
         
    
    