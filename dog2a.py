class Dog():
    Cry= "bark!"
    def __init__(self,name):
        self.name=name
    def greeting(self):
        return("I'm"+" "+self.name+","+self.Cry)

class Retriever(Dog):
               pass
Benji=Retriever("Benji")    

class Golden(Retriever):
    def greeting(self):
        return ("OHAI!"+Retriever.greeting(self))
Lassie=Dog("Lassie")
hihi=Retriever("hihi")
Sidney=Golden("Sidney")
print(Benji.greeting())
print(Lassie.greeting())
print(hihi.greeting())
print(Sidney.greeting())
print(Dog.greeting(Sidney))
    
