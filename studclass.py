class Student:
    def __init__(self):
        pass

    def setName(self, name):
        if type(name)== str:
            self.name= name
        else:
            print("input must be string")

    def setClass(self,clas):
        if type(clas) == str:
            self.clas = clas
        else:
            raise Exception("type error")
    def setRoll(self,roll):
        if type(roll) == int:

            self.roll=roll
        else:
            raise Exception("type error")

    def getName(self):
        return self.name

    def getclas(self):
        return self.clas
    def getroll(self):
        return self.roll

stud1 = Student()
stud1.setName("paritosh")
stud1.setClass("Bachelors")
stud1.setRoll(109)

print("Name:" +stud1.getName())
print("Class:" + stud1.getclas())
print("Roll No:" + str(stud1.getroll()))


#now try using constructor

