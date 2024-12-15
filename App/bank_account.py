from App.file_handler import save_balance, save_transaction, read_first_line, create_file


class Bank_Account:    
    def __init__(self, name, pin, acc_number):
        self.__name = name
        self.__pin = pin
        self.__acc_number = acc_number
        self.transaction_history = f'.\\App\\data\\{acc_number}.txt'
        self.balance_file = f'.\\App\\data\\{acc_number}_b.txt'

        create_file(self.balance_file)
        create_file(self.transaction_history)
                     
    def deposit(self, amount):
        self.balance = amount
        save_transaction(self.transaction_history,amount)

    def withdraw(self, amount):
        if self.check_funds(amount):
            self.balance = -amount
            save_transaction(self.transaction_history,-amount)
            return True

    def transfer_history(self):
        transfers = []
        with open(self.transaction_history, "r", encoding="UTF-8") as f:
# check only last 160 transfers
            lines = f.readlines()[-1:-160:-1]
            for line in lines:              
                if line == '\n':
                    continue  
# avoid value error when unpacking if line equals '\n'
                amount, _ = line.rstrip('\n').split(',')
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
        b = read_first_line(self.balance_file)
        if b == "":
            b = 0
        else:
            b = float(b)
        return b
    
    @balance.setter
    def balance(self, amount):
        amount += self.balance
        save_balance(self.balance_file, amount)
             
     
     

         
     


    


