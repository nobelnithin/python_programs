list=[]
num= int(input("Enter your list range: "))
for i in range (1,num+1):
    val=int(input('Enter your {} number: '.format(i)))
    list.append(val)
x=0
n=len(list)
for i in range(n):
    x=x+list[i]
print(x)