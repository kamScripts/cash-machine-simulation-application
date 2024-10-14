import datetime
# find way to store and edit balance in file
#change __ na _, bo nie potrzebne.
#change csv na txt
class Bank_Account:
    
    def __init__(self, name, pin, acc_number):
        self.__name = name
        self.__pin = pin
        self.__acc_number = acc_number
        self._balance = 0    
        self.file = f'./main/{acc_number}.csv'      

    def deposit(self, amount):
        self.balance = amount
        self.save(amount)

    def withdraw(self, amount):
        if self.check_funds(amount): 
            self.balance = -amount          
            self.save(-amount)
            return True

    def transfer_history(self):
        transfers = []
        with open(self.file, 'r') as f:
            lines = f.readlines()[-1:-20:-1]          
            for line in lines:
                amount, _ = line.strip().split(',')
                transfers.append(amount)
        return transfers
       
    def check_funds(self, amount):
        return  amount <= self.sum_expenses()
    
    def save(self, amount):
            with open(self.file, "a") as f:
                f.write(f'{float(amount):.2f}, {datetime.datetime.now()}\n')

    def sum_expenses(self):
            return sum([float(transfer) for transfer in self.transfer_history()])
         

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
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        self._balance += amount
         
     


    


