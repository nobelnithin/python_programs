numb=int (input("Enter a number: "))
def func(numb):
    if numb%2==0:
       print("{} is an even number".format(numb))
    else:
       print("{} is an odd number".format(numb))
func(numb)