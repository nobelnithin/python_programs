x=input("Enter your geander: B or G for boy or girl respectively:: ")
y = int(input("Enter your age: "))
if  x=="B" or "b":
    if y<18:
        print("Access denied")
    else:
        print("Access granded")
elif x=="g" or "G":
    if y<18:
        print("Access denied")
    else:
        print("Access granded")
