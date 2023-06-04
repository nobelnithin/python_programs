import time
import random
s=0
list=[1,2,3,4,5,6,10,15,20,25,50,100]
for i in range(10):
    x=random.randint(0,12)
    print(list[x])
    time.sleep(1.5)
    s+=list[x]
print("")
print(s)
    
    
