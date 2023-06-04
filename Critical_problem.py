"""
   This is the problem of 1/1! +4/2! +27/3!+....
"""
def fact(n):
    f=1
    if (n==0):
        return 1
    else:
        for i in range (1,int(n+1)):
            f=f*i
        return f
n=int(input("Entr your value: "))
s=0.0
for i in range (1,n+1):
    s=s+(float(i*i)/fact(i))
print("Result: ",format(s,'.5f'))