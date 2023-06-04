p=float(input("Enter your principle amount: "))
r=float(input("Enter your rate: "))
n=int(input("Enter your number of years: "))
def simple_interest(p,r,n):
    si=(p*r*n)/100
    return si
    """this thre formation of simpleintrest"""
pa =simple_interest(p,r,n)+p

print("Simple Intrest: ",simple_interest(p,r,n))

print("Principle amount: ",pa)