class Animal:
    def sayhi(self,name):
        self.name=name
        return name +   " says hello."
    def __init__(self,name):
        print(name +   " speaks hello.")



cat=Animal("paritosh")




print(cat.sayhi("paritosh"))

