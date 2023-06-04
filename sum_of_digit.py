'''
     This block of code will sum up all the digit in the
     number
     eg: 12=1+2=3
        123=1+2+3=6
'''

x=int(input("Enter your number: "))
y=str(x)
n=len(y)
m=0
for i in range(n):
    m=m+int(y[i])
print(m)