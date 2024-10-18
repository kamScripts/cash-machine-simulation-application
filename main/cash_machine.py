import pwinput 
import os
from time import sleep
from style import green, red, yellow, red_no_background, green_no_background
from prompter import prompts
from accounts import accounts




class CashMachine:    
    MAX_LENGTH, _ = os.get_terminal_size()
    def user_interface(self):
        exit_app = False
        account = self.insert_card()
        if(not self._verify_pin(account)):
            exit_app = True       
        
        while exit_app is False: 
            print(green_no_background('*')* self.MAX_LENGTH)           
            for num, line in enumerate(prompts['main_menu']):                               
                print(f'{yellow(str(num+1)+'.')}{line}'.center(self.MAX_LENGTH)) 
            print(green_no_background('*')* self.MAX_LENGTH)               
            choice = input('Choose [1-5]: ')                     
            match choice:
                case '1':
                    self.clear_terminal(1)                    
                    print(self._get_balance(account).center(self.MAX_LENGTH))                    
                case '2': 
                    self.clear_terminal(1) 
                    print(self._transfer_history(account))
                case '3':
                    self.clear_terminal(1) 
                    print(self._withdraw(account).center(self.MAX_LENGTH))
                case '4':
                    self.clear_terminal(1) 
                    print(self._deposit(account).center(self.MAX_LENGTH))
                case '5':
                    self.clear_terminal(1) 
                    self._goodbye()
                    exit_app = True
                    
               
    def insert_card(self):
        acc_number = int(input(yellow("Please enter account number: ")))
        for acc in accounts:
            if acc.acc_number == acc_number:                
                return acc
            else:
                print('wrong number')
      
        
        

    def _verify_pin(self, account):        
        attempt_counter, welcome_string = 0, f' Hi, {account.name}.'           
        while attempt_counter <=3:                    
            user_pin = pwinput.pwinput(prompt=f'{yellow("Please enter pin to log in:")}')
            #user_pin =  input(f'{yellow("Please enter pin to log in:")}')            
            if user_pin.isdigit() and self._check_pin(account, int(user_pin)):                 
                print(green(welcome_string.center(self.MAX_LENGTH, '*')))
                self.clear_terminal(1)                      
                return True
            else:                          
                attempt_counter+=1
                print(f'\t{red_no_background("incorrect pin, you have")} {4-attempt_counter} {red_no_background("attempts")}'.center(self.MAX_LENGTH))
                self.clear_terminal(1)
        print('You have exceeded maximum attempts, your card is blocked. Contact bank')
        
    def clear_terminal(self, delay):
            sleep(delay)
            os.system('cls') 
            
    def _check_pin(self, account, pin_to_verify): 
        return account.pin == pin_to_verify
           
    def _get_balance(self, account):
        return f'{green('Account Balance:')} £{account.balance:.2f}' 
    
    def _transfer_history(self, account):        
        ledger = account.transfer_history()
        output = green('     Deposit History:')              
        for entry in ledger :
            if float(entry) > 0:
                output += f'|{"£ "+ entry if len(entry) == 7 else " " * (7-len(entry)) + "£ "+ entry}|'
        output+='\n'
        output += red(' Withdrawals History:')
        for entry in ledger:
            if float(entry) < 0:
                output += f'|{"£ "+entry.lstrip('-') if len(entry)-1 == 7 else " " * (7-(len(entry)-1)) +"£ "+ entry.lstrip('-')}|'        
        return output
        
    def _withdraw(self, account):
        amount = input(f'{yellow(prompts['withdraw'][0])}')
        if amount.isdigit() and int(amount)<=2000:                               
            if account.withdraw(float(amount)):
                return f'{green_no_background(prompts['withdraw'][1])}{amount}'   
            else:
                return red_no_background(prompts['withdraw'][2])
        else:
            return red(prompts['withdraw'][3])

    def _deposit(self, account):         
        amount = input(f'{green_no_background(prompts['deposit'][0])}')   
        if amount.isdigit() and int(amount) <= 10000:
            account.deposit(float(amount))            
            return f'{green_no_background(prompts['deposit'][1])}{amount}'
        else:
            return red(prompts['deposit'][2])

    def _goodbye(self):       
        for message in prompts['exit']:
            print(message.center(self.MAX_LENGTH, '*'))      
         