list=[1,1]
n=int(input("Enter the value: "))
i=0
while i<=n-3:
    y=list[i]+list[i+1]
    list.append(y)
    i+=1
print(list)