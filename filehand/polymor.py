class shape1:
    def __init__(self,name,edge,size):
        self.name=name
        self.edge=edge
        self.size=size
    def info(self):
        print("my name is", self.name)
        print("edge is",self.edge)
        print("my size is",self.size)
    def colour(self):
        print("red")
class shape2:
    def __init__(self,name,edge,size):
        self.name=name
        self.edge=edge
        self.size=size
    def info(self):
        print("my name is",self.name)
        print("edge is",self.edge)
        print("my size is",self.size)
    def colour(self):
        print("orange")
        
x=shape1("rectangle","four","5 cm long and 2 cm hight") 
y=shape2("circle","zero","something else")
for shape in(x,y):
     shape.colour()
     shape.info()       
