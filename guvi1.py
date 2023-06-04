get_range=int(input("Enter the range of your list: "))
list=[]
for i in range(1,get_range+1):
    values=str(input("Enter your string {} ".format(i)))
    value=values.capitalize()
    list.append(value)
print(list)
