def details(name,age,add):
    try:
        assert(type(name)== str and type(age)== int and type(add) == str and len(name) >0 and len(add)>0),"enter the right type"
        print(True)

    except AssertionError:
        print("error")

details("paritosh",21,"Satdobato")


