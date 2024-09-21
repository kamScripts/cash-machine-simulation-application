import re
import pwinput

class CashMachine:

    
    def user_interface(self, account):
        self._verify_pin(account)
        print(f'\nHi, {account.name}.')
        while(True):
            print('''
    Choose one of the following options:
        1. Check Balance
        2. Check Deposit history
        3. Check Withdrawal history
        4. Withdraw Funds
        5. Deposit Funds
        6. Change Pin
        7. Exit
''')
            choice = input('\tType 1-7 to choose following option: ')
            match choice:
                case '1': 
                    print(f'\Account Balance: £{account.check_balance():.2f}')                    
                case '2':                    
                    print(f'Deposit History: \n{account.deposit_history()}')
                case '3':
                    print(f'Withdrawals History: \n{account.withdrawal_history()}')
                case '4':
                    amount = input('Amount to withdraw: ')


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
                    new_pin = input('')
                case '7':
                    print("Thank you for using CASH MACHINE.\n Don't forget Your Card")
                    break           
        
        
            
    def _verify_pin(self, account):
        attempt_counter = 0       
        while(True):            
            user_pin = pwinput.pwinput(prompt='Please enter pin to log in:')
            if  re.match(r'^\d+$', user_pin):
                if self._check_pin(account, int(user_pin)):                       
                    return True
                else:               
                    if attempt_counter >=3:
                        print('You have exceeded maximum attempts, your card is blocked. Contact bank')
                        quit()
            attempt_counter+=1
            print(f'incorrect pin, you have {4-attempt_counter} attempts')

    def _check_pin(self, account, pin_to_verify):
        if account.pin == pin_to_verify:
            return True
        else:
            return False
         
    
    