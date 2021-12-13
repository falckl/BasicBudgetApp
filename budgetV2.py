class Budget():
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"The budget in category {self.name} is {self.balance}"
    
    def deposit(self,deposit):
        return self.balance + deposit
    
    def withdraw(self,withdrawal):
        return self.balance - withdrawal

    def checkBalance(self):
        return self.balance 