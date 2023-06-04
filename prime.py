numb=int(input("Enetr a number: "))

def prime(numb):
    if numb%2==1:
        print("{} is a prime number".format(numb))

    else :
        print("{} is not a prime number".format(numb))
if numb==2:
    print("2 is a prime number")
elif numb==1:
    print("1 is not a prime number")
else:
     prime(numb)