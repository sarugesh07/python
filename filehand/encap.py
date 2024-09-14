class student:
    def __init__(self,name,age,std,rank,score):
        self.name=name
        self.age=age
        self.std=std
        self.rank=rank
        self.score=score
    def getname(self):
        print("my name is:",self.name)
        print("my age is:",self.age)
        print("I am studing:",self.std)
        print("I get the:",self.rank)
        print("I was scored: ",self.score)
    def setname(self,name):
        self.name=name
            

school=student("venkat",18,12,"first rank",550) 
school.getname()
school.setname("ajay") 
school.getname()     
school.setname("adhi")
school.getname()
                                                                                                  
    