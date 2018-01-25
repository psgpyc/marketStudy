class Employee:
    raise_amount = 1.04

    def __init__(self,name,address,salary):
        self.name = name
        self.address = address
        self.salary = salary
        self.email = name + "employee@gmail.com"

    def __str__(self):
        return "employee name   : " + self.name + "\nEmployee address: " + self.address + "\nemployee salary : " + str(self.salary) + "\nemployee email  : " + self.email + "\nraise_amount    : " +  str(self.raise_amount)


    @classmethod
    def update_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def parsing_String(cls,empstring):
        name,add,sal = empstring.split("-")
        return cls(name,add,sal)


emp1 = Employee("paritosh","satdobato",20000)

print(emp1.__str__())

#changing the class variable using class method

Employee.update_raise_amount(1.05)
print("\n" + emp1.__str__())

#using class method to automate the parsing of strings


emp_string = "jhakrii-baneshowr-12000"
new_emp = Employee.parsing_String(emp_string)

# print("\nemployers name  : " + new_emp.name)
#
#
# print(new_emp.email)

print("\n" + new_emp.__str__())