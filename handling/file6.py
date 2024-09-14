""" for x in range(2):
    a=input("employ name:")
    b=input("project name:")
    c=input("employ skill:")
    d=input("exprience:")
    e=input("salary:")
    f=input("language:")
    g=open("hand.txt","a")
    g.write("\n"+a+"\t"+b+"\t"+c+"\t"+d+"\t"+e+"\t"+f)
 """
word=input("enter the name")

g=open("hand.txt",'r')
info=g.read().split("\n")
for x in info:
    data=x.split("\t")
    if(data[0]==word):
        print(data[1])
        print(data[2])
        print(data[3])
        print(data[4])
        print(data[5])
        break
else:
    print("not found!!!!!!!!!!!")