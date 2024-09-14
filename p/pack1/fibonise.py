def fibonise():

   x=1
   y=1
   n=5
   while(n>0):
       z=x+y
       x=y
       y=z
       n-=1
       print(z)
