F=[1,1]
n=int(input("Enter a number for the range of fibonacci series: "))
for i in range(n-2):
    x=len(F)-1
    y=F[x]+F[x-1]
    F.append(y)
print(F)