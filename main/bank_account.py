import datetime
#zmienic czek @property ledger, check funds, dodac wybor kont i moze stworzenie nowego konta
#posprzatac funkcje, zrobic cos z self.ledger
# zmienic ledger na self.balance  i przy transferze update? 
# zmienic transfer history w atm zeby wyswietlalo oddzielnie depozyty i wyplaty
class Bank_Account:
    def __init__(self, name, pin, acc_number):
        self.__name = name
        self.__pin = pin
        self.__acc_number = acc_number
        self.__ledger = []
        self.file = f'{acc_number}.csv'
        
    def save(self, item):
        print(self.file)
        with open(self.file, "a") as f:
            f.write(f'{float(item):.2f}, {datetime.datetime.now()}\n')

    def deposit(self, amount):
        self.ledger = float(amount)
        self.save(amount)
    def withdraw(self, amount):
        if self.check_funds(amount):
            self.ledger = -float(amount)
            self.save(-amount)
            return True
        else:
            return False
    def transfer_history(self):
        transfers = []
        with open(self.file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                amount, _ = line.strip().split(',')
                transfers.append(amount)
        return transfers
    def withdrawal_history(self):        
        return [f'£{abs(entry):.2f}' for entry in self.__ledger if entry <0]
    
    def deposit_history(self):
        return [f'£{entry:.2f}' for entry in self.__ledger if entry >0]
    def check_funds(self, amount):
        return  amount <= self.ledger

    @property 
    def name(self):
        return self.__name
    @property
    def pin(self):
        return self.__pin
    @property
    def ledger(self):
        return sum(self.__ledger)
    @property
    def acc_number(self):
        return self.__acc_number
    @pin.setter
    def pin(self, new_pin):
        if len(new_pin)>= 4 or len(new_pin) <=6:        
            self.__pin = new_pin
        else:
            return False        
    @ledger.setter
    def ledger(self, amount):
        self.__ledger.append(amount)
    


