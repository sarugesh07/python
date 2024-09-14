a=1
b=2
c=3
if (a>b and a>c):
    if(b>c):
        print("b mid")
    else:
        print("c mid")

if(b>a and b>c):
    if(a>c):
        print("a mid")
    else:
        print("c mid")

if(c>a and c>b):
    if(c>a):
        print("c mid")
    else:
        print("a mid")
