def gcd(x,y):
    for i in range(1,min(x,y)+1):
        if x%i==0 and y%i==0:
            soln=i
    return soln

def main():
    m=50
    n=5
    if m<n:
        (m,n)=(n,m)
    print('GCD: ',gcd(m,n))
if __name__ == "__main__":
        main()
