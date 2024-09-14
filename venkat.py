n1=n=int(input("enter the number"))

#condition 1
r=0
while n>0:
    a=n%10
    r=a+(r*10)
    n//=10
ab=a=r*r
print(ab)
    
#condition 2
a=n1*n1
r=0
while a>0:
    a1=a%10
    r=a1+(r*10)
    a//=10

    
print(a,ab)

if (a==ab):
    print("adam")
else:
    print("not adam")

