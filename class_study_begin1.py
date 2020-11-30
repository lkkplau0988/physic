class Person:
    def setName(self, name):
        self.name = name.title()
    def getName(self):
        return self.name
    
# end of class definition
#start of program
person1 = Person() #create instance of class
person1.setName('Mr. Smith') #set name
print(person1.getName()) # get name

