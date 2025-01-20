# Decorator to ensure the salary is positive
def Pos(func):
    def wrapper(self, value):
        if value < 0:
            value = -value  
        return func(self, value)
    return wrapper

class Emp:
    def __init__(self):
        self._salary = 0 

    @property
    def Salary(self):
        return self._salary
    
    @Salary.setter
    @Pos 
    def Salary(self, value):
        self._salary = value  # Set the salary to the value


obj = Emp()


obj.Salary = 5000
print(obj.Salary)


obj.Salary = -3000
print(obj.Salary) 
