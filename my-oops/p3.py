class Vahicle:
    def Road(self):
        print("Road Trasport")
    def Air(self):
        print("Air Trasport")
    def Water(self):
        print("Water Trasport")
class Car(Vahicle):
    def __init__(self,Brand,Model):
        self.Brand=Brand
        self.Model=Model
        print(f'The Car Brand is {Brand} In Model {Model}')
        
class Plane(Vahicle):
    def __init__(self,Brand,Model):
        self.Brand=Brand
        self.Model=Model
        print(f'The Plane Brand is {Brand} In Model {Model}')
        
        
car1=Car('BMW','150')
car1.Road()    

    
plane1=Plane('AirIndia','Boil170')
plane1.Air()    

    