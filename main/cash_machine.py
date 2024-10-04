import re
#import pwinput 
from style import green, red, yellow, red_no_background, green_no_background

class CashMachine: 
    PROMPT = f'''
Choose one of the following options:
    {yellow('1.')} Check Balance
    {yellow('2.')} Check Transfer history
    {yellow('3.')} Withdraw Funds
    {yellow('4.')} Deposit Funds
    {yellow('5.')} Change Pin
    {yellow('6.')} Exit       
''' 
    MAX_LENGTH = 40
    
    def user_interface(self, account):
        self._verify_pin(account)            
        while(True):
            print(self.PROMPT)
            choice = input('')           
            
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
            #user_pin = pwinput.pwinput(prompt=f'{yellow("Please enter pin to log in:")}')
            user_pin =  input(f'{yellow("Please enter pin to log in:")}')
            welcome_string=f' Hi, {account.name}. '
            if  re.match(r'^\d+$', user_pin):
                if self._check_pin(account, int(user_pin)): 
                    
                    print(green(welcome_string.center(self.MAX_LENGTH, '*')))                      
                    return True
                else:               
                    if attempt_counter >=3:
                        print('\tYou have exceeded maximum attempts, your card is blocked. Contact bank')
                        quit()
            attempt_counter+=1
            print(f'\t{red_no_background("incorrect pin, you have")} {4-attempt_counter} {red_no_background("attempts")}')
            
    def _check_pin(self, account, pin_to_verify):
        if account.pin == pin_to_verify:
            return True
        else:
            return False
    def _get_balance(self, account):
        return f' {green('Account Balance:')} £{account.ledger:.2f} '.center(self.MAX_LENGTH, '*') 
    def _transfer_history(self, account):
    #    output = green(' Deposit History: '.center(22))
    #    
    #    for entry in account.deposit_history():
    #        output += f' {entry} '
    #    output+='\n'
    #    output += red(' Withdrawals History: ')
    #    
    #    for entry in account.withdrawal_history():
    #        output += f' {entry} '
    #    
    #    return output
        return(account.transfer_history())
    def _withdraw(self, account):
        amount = input(f'{yellow("Amount to withdraw:"):>45} ')
        if re.match(r'^\d+$', amount):
            boolean = account.withdraw(float(amount))        
            if(boolean):
                print(f' {green_no_background("You successfully withdrew £")}{amount} '.rjust(self.MAX_LENGTH))   
            else:
                print(red_no_background(' Not not enough funds ').center(self.MAX_LENGTH, '*'))
        else:
            print(red(' Value error, type only digits. ').center(self.MAX_LENGTH, '*'))
    def _deposit(self, account):
        amount = input(f'{green_no_background("Amount to deposit:"):>45} ')
        if re.match(r'^\d+$', amount):
            account.deposit(float(amount))
            print(f' {green_no_background("You successfully deposited £")}{amount} '.center(self.MAX_LENGTH, '*'))
        else:
            print(red(' Value error, type only digits. ').center(self.MAX_LENGTH, '*'))
    def _set_new_pin(self, account):        
        new_pin = input('Type New Pin:')
        if re.match(r'^\d{4}$', new_pin):                        
              account.pin = new_pin
              print(green_no_background(' success, new pin set. ').center(self.MAX_LENGTH, '*'))
        else:
                print(red(' incorrect format. type(4 digits) ').center(self.MAX_LENGTH, '*'))
    def _goodbye(self):
        print(" Thank you for using CASH MACHINE. ".center(self.MAX_LENGTH, '*'))
        print(" Take your Credit Card first ".center(self.MAX_LENGTH, '*'))
        print(" Your Withdrawal will follow shortly ".center(self.MAX_LENGTH, '*'))        
        quit() 