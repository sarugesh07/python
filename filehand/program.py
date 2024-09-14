class new:
    def adam(self):
        n1=n=int(input("enter the number"))
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
    def fibo(self):
        x=1
        y=1
        n=5
        while(n>0):
            z=x+y 
            x=y
            y=z
            n-=1
            print(z)
    def adam_fibo(self):
        print("name") 
    def set(self,name):
        self.name=name           
class news(new):
    def arm(self):
        r=0
        n1=n=153
        while n>0:
            a=n%10
            r=r+(a**3)
            n//=10
        print(r)
    def fact(self):
        n=int(input("enter the number"))
        r=1
        while(n>0):
            r=r*n
            n-=1
        print(r)
    def arm_fact(self):
        print("number")  
    
      

obj1=news()
obj1.adam_fibo()
obj1.arm_fact()
obj1.set("school")

a=1
if (a==1):
   obj1.adam()
elif(a==2):
    obj1.fibo()  
elif(a==3):
    obj1.arm()   
elif(a==4):
    obj1.fact()
else:
    print("run code")   
