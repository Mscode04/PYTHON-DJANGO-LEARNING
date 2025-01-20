class Shaheen:
    name='Shaheen'
    def __init__(self,Age,Place):
        self.Age=Age
        self.Place=Place
    def prints(self):
        print(f'Age: {self.Age}  Place:  {self.Place}')    
obj=Shaheen(12,'MLP')
print(obj.prints())
print(obj.name)
obj.Age=23
print(obj.prints())
Shaheen.name='mazin'
print(obj.name)