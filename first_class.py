class FirstClass:
    def setdata(self,value):
        self.data=value
    def display(self):
        print(self.data)
    def keitest(self,num1,num2):
        a=self.num1=num1
        b=self.num2=num2
        sum=a+b
        print(sum)
        
test=FirstClass()
test2=FirstClass()
test.setdata(26)
test.display()
test.keitest(50,6)
test2.keitest(37,9)
