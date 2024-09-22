import re
import pwinput

class CashMachine: 
    PROMPT = '''
        Choose one of the following options:
            1. Check Balance
            2. Check Transfer history
            3. Withdraw Funds
            4. Deposit Funds
            5. Change Pin
            6. Exit
        Type 1-7 to choose following option:
         
''' 
    LINES = PROMPT.split('\n')
    MAX_LENGTH = len(LINES[1])
    
    def user_interface(self, account):
        self._verify_pin(account)
              
        
        while(True):
            print(self.PROMPT)
            choice = input('')
            print('\n')
            
            match choice:
                case '1': 
                    print(self._get_balance(account))
                case '2': 
                    print(self._transfer_history(account))
                case '3':
                    self._withdraw(account)
                case '4':
                    self._deposit(account)
                case '5':
                    self._set_new_pin(account)
                case '6':
                    self._goodbye()                
    def _verify_pin(self, account):
        attempt_counter = 0       
        while(True):            
            user_pin = pwinput.pwinput(prompt='\tPlease enter pin to log in:')
            welcome_string=f' Hi, {account.name}. '  
            if  re.match(r'^\d+$', user_pin):
                if self._check_pin(account, int(user_pin)): 
                    print('\n')
                    print(welcome_string.center(self.MAX_LENGTH, '*'))                      
                    return True
                else:               
                    if attempt_counter >=3:
                        print('\tYou have exceeded maximum attempts, your card is blocked. Contact bank')
                        quit()
            attempt_counter+=1
            print(f'\tincorrect pin, you have {4-attempt_counter} attempts')
    def _check_pin(self, account, pin_to_verify):
        if account.pin == pin_to_verify:
            return True
        else:
            return False
    def _get_balance(self, account):
        return f' Account Balance: £{account.ledger:.2f} '.center(self.MAX_LENGTH, '*') 
    def _transfer_history(self, account):
        output = ' Deposit History: '
        
        for entry in account.deposit_history():
            output += f' {entry} '
        output+='\n'
        output += ' Withdrawals History: '
        
        for entry in account.withdrawal_history():
            output += f' {entry} '
        
        return output
         
# add conditionals to withdraw/deposit to prevent ValueError, regex: r'^\d+$'
    def _withdraw(self, account):
        amount = input('\tAmount to withdraw: ')
        if re.match(r'^\d+$', amount):
            boolean = account.withdraw(float(amount))        
            if(boolean):
                print(f' You successfully withdrew £{amount} '.center(self.MAX_LENGTH, '*'))   
            else:
                print('You have not enough funds'.center(self.MAX_LENGTH, '*'))
        else:
            print(' Value error, type only digits. '.center(self.MAX_LENGTH, '*'))
    def _deposit(self, account):
        amount = input('\tAmount to deposit: ')
        if re.match(r'^\d+$', amount):
            account.deposit(float(amount))
            print(f' You successfully deposited £{amount}. '.center(self.MAX_LENGTH, '*'))
        else:
            print(' Value error, type only digits. '.center(self.MAX_LENGTH, '*'))
    def _set_new_pin(self, account):        
        new_pin = input('Type New Pin:')
        if re.match(r'^\d{4-6}$', new_pin):                        
            account.pin(int(new_pin))
            print(' success, new pin set. '.center(self.MAX_LENGTH, '*'))
        else:
            print(' incorrect format. type(4 to 6 digits) '.center(self.MAX_LENGTH, '*'))
    def _goodbye(self):
        print(" Thank you for using CASH MACHINE. ".center(self.MAX_LENGTH, '*'))
        print(" Take your Credit Card first ".center(self.MAX_LENGTH, '*'))
        print(" Your Withdrawal will follow shortly ".center(self.MAX_LENGTH, '*'))        
        quit() 