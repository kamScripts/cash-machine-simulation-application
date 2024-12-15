from time import sleep
try:
    import pwinput
except ImportError as err:
    print(err)
     
import getpass
import os
from App.style import yellow, red, green, center_input, withdraw_notes
from App.prompter import prompts
from App.accounts import accounts
class ATM:
    """Methods to take and verify user input, then call bank account methods"""

    t_length, t_height = os.get_terminal_size()

    def insert_card(self):
        """Verify Account Number"""     
        acc_number = ''
        while acc_number != 'q':
            acc_number = input(yellow("Please enter account number or enter q to exit: "))
            if acc_number.isdigit():
                acc_number =int(acc_number)
# check if number match any acc number in the database.
                for acc in accounts:
                    if acc.acc_number == acc_number:
                        return acc
            else:
                print('Try again or press q to e.')
        os._exit(0)
        
    def _verify_pin(self, account):
        """Verify Account's password"""           
        welcome_string = f' Hi, {account.name}.'
# three attempts to log in
        for x in range(3):
# If pwinput not installed, use getpass.
            try:
                user_pin = pwinput.pwinput(prompt=f'{yellow("Please enter PIN to log in:")}')
            except NameError as err:
                print(err)
                user_pin =  getpass.getpass(prompt='Please enter PIN (Input will be hidden):')
# return true if password is correct.
            if user_pin.isdigit() and self._check_pin(account, int(user_pin)):
                print(green(welcome_string.center(self.t_length, '*')))
                self.clear_terminal(1)
                return True
            print(f'{red("incorrect PIN, you have")} {3-(x+1)} {red("more attempts")}'.center(self.t_length))
            self.clear_terminal(1)
        print('You have exceeded maximum attempts, your card is blocked. Contact bank')
        return False


    def clear_terminal(self, delay):
        """clear terminal with delay to simulate real atm loading""" 
        sleep(delay)
        os.system('cls')

    def _check_pin(self, account, pin_to_verify):
        """verify input against object's password"""
        return account.pin == pin_to_verify

    def _get_balance(self, account):
        return f'{green("Account Balance:")} £{account.balance:.2f}' 

    def _transfer_history(self, account):
        """Display Transfer history"""
        ledger = account.transfer_history()
        output = ''.rjust(self.t_length, '*')
        output += '\n' * ((self.t_height // 2)-1)
        output += green('     Deposit History:\n')
# temp variables to store part of the output string when loop through ledger list.
        dep, wit = '',''
# to add \n when len(string) reach ((length of terminal) - 10).
        counter_d,counter_w=1,1
        for entry in ledger :
                # when length of string is close to length of terminal add new line.
                #counters keep track of number of lines.                                
            if len(dep) >=counter_d*(self.t_length-10):
                dep+='\n  '
                counter_d +=1
            if len(wit) >=counter_w*(self.t_length-10):
                wit+='\n  '
                counter_w +=1
#when value is bigger than 0 assign to deposit part of the string and format size of entry to always has len() of 7
            if float(entry) > 0:
                dep += f'|{"£ "+ entry if len(entry) == 7 else " " * (7-len(entry)) + "£ "+ entry}|'
# format size to len() of 7, if len() of number not equal seven add space character n  times.
            else:
                wit += f'|{"£ "+entry.lstrip("-") if len(entry)-1 == 7 else " " * (7-(len(entry)-1)) +"£ "+ entry.lstrip("-")}|'
        output+= dep.strip() +'\n'
        output += red(' Withdrawals History:\n') + wit
        return output

    def _withdraw(self, account):
        center_input(self.t_length, self.t_height)
        amount = input(f'{yellow(prompts["withdraw"][0])}')
        if amount.isdigit() and 10 <= int(amount)<=260 and int(amount)%10 == 0:
# check if enough funds to withdraw and output result to the user.
            if account.withdraw(float(amount)):
                print(f'{green(prompts["withdraw"][1])}{amount}')
                self.clear_terminal(2)
                return   withdraw_notes(int(amount))
            else:
                return red(prompts['withdraw'][2])
        else:
            return red(prompts['withdraw'][3])

    def _deposit(self, account):
        center_input(self.t_length, self.t_height)         
        amount = input(f'{green(prompts["deposit"][0])}')
        if amount.isdigit() and 10 <= int(amount) <= 5000 and int(amount)%10 == 0:
            account.deposit(float(amount))            
            return f'{green(prompts["deposit"][1])}{amount}'
        else:
            return red(prompts['deposit'][2])

    def _goodbye(self):
        for message in prompts['exit']:
            print(yellow(message.center(self.t_length, '*')))