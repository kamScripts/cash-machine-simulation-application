from App.file_handler import save_balance, save_transaction, read_first_line, check_path, create_file



# find way to store and edit balance in file
#change __ na _, bo nie potrzebne.
#change csv na txt
class Bank_Account:
    
    def __init__(self, name, pin, acc_number):
        self.__name = name
        self.__pin = pin
        self.__acc_number = acc_number 
        self.transaction_history = f'{acc_number}.csv'
        self.balance_file = f'{acc_number}_b.txt'
        #check if new object balance is read properly after remove value in innit
        create_file(self.balance_file)
        create_file(self.transaction_history)
        
#self.transaction_history, "w")

               

                
              
    def deposit(self, amount):
        self.balance = amount
        save_transaction(self.transaction_history,amount)

    def withdraw(self, amount):
        if self.check_funds(amount): 
            self.balance = -amount          
            save_transaction(self.transaction_history,-amount)
            return True
# transfer history need to be improved
#idea, maybe nest 2 lists in transfers to store separate deposits and withdraws
#move file handling 
    def transfer_history(self):
        transfers = []
        with open(self.transaction_history, "r") as f:
            # check only last 20 transfers
            lines = f.readlines()[-1:-100:-1]          
            for line in lines:
                # avoid value error when unpacking if line equals '\n'
                if line == '\n' or not line.isdigit():
                    continue
                amount, _ = line.strip().split(',')
                transfers.append(amount)
        return transfers
       
    def check_funds(self, amount):
        return  amount <= self.balance       

    @property 
    def name(self):
        return self.__name
    @property
    def pin(self):
        return self.__pin
    @property
    def acc_number(self):
        return self.__acc_number
    @property
    def balance(self):
        b = float(read_first_line(self.balance_file))          
        return b
    
    @balance.setter
    def balance(self, amount):
        amount += self.balance
        save_balance(self.balance_file, amount)
             
     
     

         
     


    


