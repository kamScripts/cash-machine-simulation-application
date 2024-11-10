from App.style import yellow, center_input
from App.prompter import prompts
from App.atm_methods import ATM

class CashMachine(ATM):  
          
    def user_interface(self):
        app_on = True
        account = self.insert_card()
        if not self._verify_pin(account):
            app_on = False       
        
        while app_on: 
            # position text in the middle of the terminal.
            center_input(self.t_length, self.t_height)        
            for num, line in enumerate(prompts['main_menu']):                               
                print(f'{yellow(str(num+1)+".")}{line}'.center(self.t_length))                            
            choice = input('Choose [1-5]: ')                     
            match choice:
                case '1':
                    self.clear_terminal(1)                                       
                    print('\n',self._get_balance(account).center(self.t_length))                    
                case '2': 
                    self.clear_terminal(1) 
                    print(self._transfer_history(account))
                case '3':
                    self.clear_terminal(1) 
                    print(self._withdraw(account).center(self.t_length))
                case '4':
                    self.clear_terminal(1) 
                    print(self._deposit(account).center(self.t_length))
                case '5':
                    self.clear_terminal(1) 
                    self._goodbye()
                    app_on = False
                
                           
    