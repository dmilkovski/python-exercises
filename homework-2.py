class Account : 
    def __init__(self, owner:str, balance:float) :
        self.owner = owner
        self.balance = balance
    
    def deposit(self, value) :
        if value < 0 :
            print('Cannot add negative deposit')
            return
        
        self.balance = self.balance + value
        print('Deposit successful')
    
    def withdraw(self, value) :
        if  value > self.balance or self.balance - value < 0 :
            print(f'Cannot withdraw ${value} you do not have enough money')
            return
        
        self.balance = self.balance - value 
        print('Withdraw successful')
    
    def __str__(self) :
        return f'Account Owner: {self.owner}\nAccount Balance: {self.balance}'
    
john = Account('John', 500)
print(john)

john.withdraw(501)
print(john)
