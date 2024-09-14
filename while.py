r=0
n1=n=432
while n>0:
    a=n%10
    r=r+(a**3)
    n//=10   
print(r)

if n1==r:
   print("armstrong s")
else:
   print("armstorng no") 
