class person:
   def __init__(self,name,age,salary,exprience):
      self.name=name
      self.age=age
      self.salary=salary
      self.exprience=exprience
   def print(self):
      print("name:",self.name)
      print("age:",self.age)
      print("salary:",self.salary) 
      print("exprience:",self.exprience)
class empoly(person):
   def __init__(self,name,age,salary,exprience):
      person.__init__(self,name,age,salary,exprience)
      self.best=100
x=empoly("sarugesh",18,100000,"three years")
print(x.best)
x.print()      
  