"""
    this problem is made for the recursive addition like
          if n==4
        answer=  4+3+2+1
          elif n==10
        answer= 10+9+8+7+6+5+4+3+2+1

"""
def add(n):
    if n==1 or n==0:
        return 1
    else :
        return n+add(n-1)
x=float (input("Enter your value: "))
print(add(x))