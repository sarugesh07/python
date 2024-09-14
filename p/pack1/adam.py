def adam():
   n1=n=int(input("Enter the value"))
   a=n*n
   print(a)
   r=0
   while a>0:
      c=a%10
      r=(r*10)+c
      a//=10
   print(r)
   
