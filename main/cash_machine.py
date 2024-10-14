import pwinput 
from style import green, red, yellow, red_no_background, green_no_background
from bank_account import Bank_Account
from prompter import prompts


#database = [Bank_Account(name='Kamil', pin=1234, acc_number=1111), Bank_Account(name='Kasia', pin=4321, acc_number=2222)]

class CashMachine:
    MAX_LENGTH = 58
    def user_interface(self, account):
        exit_app = False
        if(not self._verify_pin(account)):
            exit_app = True       
        
        while(exit_app is False):
            
            for num, line in enumerate(prompts['main_menu']):
                print(f'\t{yellow(str(num+1)+'.')}{line}')                
            choice = input('Choose [1-6]: ')                     
            match choice:
                case '1': 
                    print(self._get_balance(account).center(self.MAX_LENGTH))
                case '2': 
                    print(self._transfer_history(account))
                case '3':
                    print(self._withdraw(account).center(self.MAX_LENGTH))
                case '4':
                    print(self._deposit(account).center(self.MAX_LENGTH))
                case '5':
                    self._goodbye()
                    exit_app = True
                    
    def insert_card(self):
        pass

    def _verify_pin(self, account):        
        attempt_counter, welcome_string = 0, f' Hi, {account.name}.'           
        while(attempt_counter <=3):                    
            user_pin = pwinput.pwinput(prompt=f'{yellow("Please enter pin to log in:")}')
            #user_pin =  input(f'{yellow("Please enter pin to log in:")}')            
            if user_pin.isdigit() and self._check_pin(account, int(user_pin)):                 
                print(green(welcome_string.center(self.MAX_LENGTH, '*')))                      
                return True
            else:                          
                attempt_counter+=1
                print(f'\t{red_no_background("incorrect pin, you have")} {4-attempt_counter} {red_no_background("attempts")}'.center(self.MAX_LENGTH))
        print('You have exceeded maximum attempts, your card is blocked. Contact bank')
        return False
            
    def _check_pin(self, account, pin_to_verify): 
        return account.pin == pin_to_verify
    def _str_to_number(self, num):
        if num.isdigit()and 
        
    def _get_balance(self, account):
        return f'{green('Account Balance:')} £{account.sum_expenses():.2f}' 
    
    def _transfer_history(self, account):        
        ledger = account.transfer_history()
        output = green('     Deposit History:')              
        for entry in ledger :
            if float(entry) > 0:
                output += f'|{"£ "+ entry if len(entry) == 7 else " " * (7-len(entry)) + "£ "+ entry}|'
        output+='\n'
        output += red(' Withdrawals History:')
        # zmienic pierwsze if na usuniecie elementu z lista a druga petla odmienia z pozastalej listy, i drugi if nie potrzebny. Albo polaczyc w jedna petle i zapisuje do dwoch stringow
        for entry in ledger:
            if float(entry) < 0:
                output += f'|{"£ "+entry.lstrip('-') if len(entry)-1 == 7 else " " * (7-(len(entry)-1)) +"£ "+ entry.lstrip('-')}|'        
        return output
        
    def _withdraw(self, account):
        amount = input(f'{yellow("Amount to withdraw:")}')
        if amount.isdigit() and int(amount)<=2000:                               
            if(account.withdraw(int(amount))):
                return f' {green_no_background("You successfully withdrew £")}{amount}'   
            else:
                return red_no_background('Not not enough funds')
        else:
            return red('Maximum withdraw amount: £2000')

    def _deposit(self, account):         
        amount = float(input(f'{green_no_background("Amount to deposit:")}'))   
        if amount <= 10000:
            account.deposit(amount)            
            return f'{green_no_background("You successfully deposited £")}{amount}'
        else:
            return red('Value error, type only digits and less or equal than maxi £10000.')

    def _goodbye(self):       
        for message in prompts['exit']:
            print(message.center(self.MAX_LENGTH, '*'))      
         