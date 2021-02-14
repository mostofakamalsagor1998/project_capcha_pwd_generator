import random

a=random.randrange(1, 100)
b=random.randrange(101, 200)
c=a+b
d=int(input(str(a)+"+"+str(b)+"\n"))
if c==d:
  print("Your calculation is OK")
else:
  print("Your calculation is not OK")