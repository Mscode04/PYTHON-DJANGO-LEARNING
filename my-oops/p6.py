# 1.	Lambda: Create a class MathOperations with a method that uses a lambda function to add two numbers.
class MathOperations:
    def addition(self):
        return lambda x,y:x+y
obj=MathOperations()   
res=obj.addition()
print(res(1,3))