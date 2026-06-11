class parent():
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class child(parent):
    def __init__(self,name,age, gender):
        super().__init__(name, age, gender)
        print("Hello i am child ", self.name)

p1=parent("ks","45","Male")
p1=child("ks","45","Male")