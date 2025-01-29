x = input("enter the number")
match x:

    case 0:
        print("Zero")
    case 4:
        print("x is four")
    case _ if x!= 100:
        print(x,"is not 100")
    case _ if x !=80:
        print(x,"is 80")
    case _:
        print(x)
