import calander
y=int(input("Your year: "))
m=1
print('')
cal=calander.TextCalandar(calander.SUNDAY)
i=1
while i<=12:
    cal.prmonthly(y,i)
    i+=1