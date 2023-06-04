
def fact(n):

    """
        The __doc__ in below is document that print this comment also but this comment must be
        in the first place of the function.
    """
    f = 1
    """
           This comment will be ignored because it is not in the first palce of the function
    """

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
print(fact.__doc__)
