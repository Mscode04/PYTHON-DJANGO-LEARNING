class Person:
    def company(self):
        print("Neuraq Technologies")
class Employee(Person):
    def __init__(self,name,position,age):
        self.name=name
        self.position=position
        self.age=age
        print(name,position,age)
        
class Manager(Employee):
    def __init__(self, salary,name,position,age):
        self.salary=salary
        print(salary)
        super().__init__(name,position,age)
obj=Manager('120000','Shaheen','Maneger','!2')
