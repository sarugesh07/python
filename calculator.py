def rev(a):
    c=0
    while(a>0):
        c=(c*10)+a%10
        a//=10
    return c
def square(a):
    return a*a
print(rev(452))
print(square(10))
