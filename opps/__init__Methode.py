class name:
    def __init__(self,name,age,pro):
        self.name=name
        self.age=age
        self.profession=pro

    def about(self):
        print(f"about {self.name}",self.age,self.profession)

    def ageUpdate(self,other):
        self.age=other.age

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

rana=name("rana",21,"hacker")
rana.about()
rohit=name("rohit",22,'account')
rohit.about()

# rohit.ageUpdate(rana)

if rana.compare(rohit):
    print("the age are same")
else:
    print("Age are different")


