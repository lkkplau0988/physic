class Account:
    
    def __init__(self,balance):
        self.balance=balance

    def getMonthlyInterestRate(self,annualInterest):
        self.annualInterest=annualInterest
        return (annualInterest/100)
    def getMonthlyInterest(self):
        return kei.balance * monthlyInterestRate	        

    def display(self):
        print(self.balance,kei.getMonthlyInterestRate(2))
        
kei=Account(200)
kei.display()
print(kei.balance)
monthlyInterestRate=kei.getMonthlyInterestRate(6)
print(monthlyInterestRate)
print(kei.getMonthlyInterest())





