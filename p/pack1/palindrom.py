def palindrom():
   r=0
   n1=n=222
   while n>0:
       a=n%10
       r=(r*10)+a
       n//=10
   print(r)

   if n1==r:
       print("panlindrom")
   else:
       print("not palindrom")
