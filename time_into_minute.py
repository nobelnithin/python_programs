def conversion(h,m):
    minute=h*60+m
    return minute
h=int(input("Enter hour: "))
m=int(input("Enter minutes: "))
m=conversion(h,m)
print(m)