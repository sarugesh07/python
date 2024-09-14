a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))

from modul import *
if(c==1):
    print(add(a,b))
elif(c==2):
    print(sub(a,b))
elif(c==3):
    print(div(a,b))
elif(c==4):
    print(multi(a,b))
else:
    print("none")
print(add(a,b),sub(a,b),div(a,b),multi(a,b))

  
