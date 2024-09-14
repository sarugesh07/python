n1=n=int(input("Enter the value"))
a=n*n
print(a)
r=0
while a>0:
    c=a%10
    r=(r*10)+c
    a//=10
print(r)

r=0
while n>0:
      c=n%10
      r=(r*10)+c
      n//=10
print(r)
b=r*r
print(b)
if(r==b):
       print("adam no")
else:
    print("not adam no")
     
