class StudentClas:
    def __init__(self,name,add,roll):
        if(validate(name,add,roll)):

            self.__name= name
            self.__add= add
            self.__roll=roll
        else:

            raise Exception("check type")

    def increment(self):
        self.__roll += 1

    def updatename(self,new_name):
        if type(new_name) == str and len(new_name) > 0:
            self.__name= new_name
        else:
            raise Exception("must input a character")

    # def getName(self):
    #     return self.name
    #
    # def getclas(self):
    #     return self.add
    #
    # def getroll(self):
    #     return self.roll

    def __str__(self):
        return "Name:" + self.__name + "\n"  + "address:" + self.__add + "\n" + "roll number:" + str(self.__roll) + "\n"

def validate(name,add,roll):
    return (type(name)== str and type(add)== str and type(roll)== int and len(name)>0)


stud1=StudentClas("paritosh","Satdobato",109)

# print("before increament\n")
# print("Name:" +stud1.getName())
# print("Class:" + stud1.getclas())
# print("Roll No:" + str(stud1.getroll()) + "\n")
#
#print(stud1.__str__())
#
# stud1.increment()
#
# print("\nafter increament\n")
# print("Name:" +stud1.getName())
# print("Class:" + stud1.getclas())
# print("Roll No:" + str(stud1.getroll()))
#
print(stud1.__str__())
#
# print("\nafter update \n")
#
# stud1.updatename("jhakrii")
# print(stud1.__str__())

print(stud1._StudentClas__name)   #calling private object

