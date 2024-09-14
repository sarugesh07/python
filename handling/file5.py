
for x in range(5):
   a=(input("enter the name"))
   b=(input("enter the age"))
   c=(input("my native place is"))
   d=(input("my ambition is"))  
   f=open("hand.txt","a")
   f.write("\n"+a+"\t"+b+"\t"+c+"\t"+d)

     
name=input("Enter your name")

f=open("hand.txt",'r')
info=f.read().split("\n")
for x in info:
    data=x.split("\t")
    if(data[0]==name):
        print(data[3])
        break
else:
    print("not found!!!!!!!!!!!")
   