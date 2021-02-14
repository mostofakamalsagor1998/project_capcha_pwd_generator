import string
import random

s1=string.ascii_uppercase#A-Z
# print(s1)
s2=string.ascii_lowercase#a-z
# print(s2)
s3=string.digits#0-9
# print(s3)
s4=string.punctuation
# print(s4)

u=[]#list
u.extend(list(s1))
random.shuffle(u)
v=[]#list
v.extend(list(s2))
random.shuffle(v)
w=[]#list
w.extend(list(s3))
random.shuffle(w)
x=[]#list
x.extend(list(s4))
random.shuffle(x)
plen=int(input(" Enter password length: "))
p1=""
p2=""
p3=""
p4=""
if plen%2==0:
    p3 = "".join(w[0:plen//4])#0,1
    p4 = "".join(x[0:plen//4])
    p1 = "".join(u[0:(plen-len(p3)-len(p4))//2])
    p2 = "".join(v[0:plen-len(p3)-len(p4)-len(p1)])
elif plen%2!=0:
    p3 = "".join(w[0])#1
    p4 = "".join(x[0])#1
    p1 = "".join(u[0:(plen-len(p3)-len(p4)-1)//2])#3
    p2 = "".join(v[0:plen-len(p3)-len(p4)-len(p1)])#9-5=4

password=p1+p3+p2+p4
print(" Your password is : "+password)
#
# msg=" Your password is : "+password

# f=open("password.txt","x")
# f.close()
# f=open("password.txt","w")
# f.write(msg)
#
