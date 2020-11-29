class Dog():
    Cry= "bark!"
    def __init__(self,name):
        self.name=name
    def greeting(self):
        return("I'm"+" "+self.name+","+self.Cry)

class Retriever(Dog):
               pass
Benji=Retriever("Benji")    
print(Benji.greeting())
class Golden(Retriever):
    def greeting(self):
        return ("OHAI!"+Retriever.greeting(self))
dig=Golden("dig")
print(dig.greeting())
fa=Golden("fa")
print(fa.greeting())
fafa=Golden("fafa")
fafafa=Golden('Dog')
print(fafafa.greeting())
lucky=Retriever("lucky")
print(lucky.greeting())
hihi=Dog("hihi")
print(hihi.greeting())
losy=Dog("losy")
print(losy.greeting())
    
