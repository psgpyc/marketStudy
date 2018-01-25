def even(num):
    return num%2==0

def fact(num):
    if num==0:
        return 1
    else:
        return num * fact(num-1)
def length(strin):
    return len(strin)


def entry():
    choice = int(input("enter the choice"))
    if choice == 1:
        print(even(12))
    elif choice == 2:
        print(fact(2))

    elif choice ==3:
        print(length("nepali"))

    else:
        print("enter the valid number")

# def main2():
#     print("this is nepal")






# main2()

if __name__  == "__main__":

    entry()
