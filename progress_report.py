sub=int(input('Enter your number of Subject: '))
list=[]
for i in range(1,sub+1):
    x=int(input("mark for subject %s: "%i))
    list.append(x)
add=0
for i in list:
    add=add+i
print('Toatal mark is:',add)
print('average: ',add/sub)

