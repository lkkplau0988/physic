class Account:
    
    def __init__(self,balance):
        self.balance=balance

    def getMonthlyInterestRate(self,annualInterest):
        self.annualInterest=annualInterest
        return (annualInterest/100)
    def getMonthlyInterest(self):
        return balance * monthlyInterestRate	        

    def display(self):
        print(balance,monthlyInterestRate,kei.getMonthlyInterest())
        
kei=Account(1000)
balance=kei.balance
monthlyInterestRate=kei.getMonthlyInterestRate(5)
kei.display()



