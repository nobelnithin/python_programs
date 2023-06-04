import random
while True:
   s=0
   for i in range(10):
      x=random.randint(1,100)
      print(x)
      s+=x
   enter=input("Enter :")
   print(s)
   print("")
