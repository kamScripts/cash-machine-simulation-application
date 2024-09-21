class Bank_Account:
    def __init__(self, name, pin, acc_number):
        self.__name = name
        self.__pin = pin
        self.__ledger = []
        self.__acc_number = acc_number
    
    def deposit(self, amount):
        self.ledger = float(amount)
    def withdraw(self, amount):
        if self.check_funds(amount):
            self.ledger = -float(amount)
            return True
        else:
            return False
    def withdrawal_history(self):
        return [f'£{abs(entry):.2f}' for entry in self.ledger if entry <0]
    
    def deposit_history(self):
        return [f'£{entry:.2f}' for entry in self.ledger if entry >0]
    
    def check_balance(self):
        return sum(amount for amount in self.ledger)
    
    def check_funds(self, amount):
        return  amount <= self.check_balance()

    @property 
    def name(self):
        return self.__name
    @property
    def pin(self):
        return self.__pin
    @property
    def ledger(self):
        return self.__ledger
    @property
    def acc_number(self):
        return self.__acc_number
    @pin.setter
    def pin(self, new_pin):
        self.__pin = new_pin
    @ledger.setter
    def ledger(self, amount):
        self.__ledger.append(amount)
    


