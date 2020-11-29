class Account:
    
    def __init__(self,balance):
        self.balance=balance

    def getMonthlyInterestRate(self,annualInterest):
        self.annualInterest=annualInterest
        return (annualInterest/100)
    def getMonthlyInterest(self):
        return balance * monthlyInterestRate	        

    def display(self):
        print(self.balance,kei.getMonthlyInterestRate(2))
        
kei=Account(200)
kei.display()
balance=kei.balance
print(balance)
monthlyInterestRate=kei.getMonthlyInterestRate(10)
print(monthlyInterestRate)
print(kei.getMonthlyInterest())





