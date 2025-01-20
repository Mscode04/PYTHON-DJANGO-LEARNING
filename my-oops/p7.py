# 1.	Generators: Write a program to create a class SquareGenerator that generates the squares of numbers from 1 to 10 using a generator function.

class SquareGenerator:
    def __init__(self,num):
        self.num=num
    def sq(self):
        for i in self.num:
            yield i**2
lists=[1,2,3,4,5]
obj=SquareGenerator(lists)
sqt=obj.sq()
for square in sqt:
    print(square)  
    
    
    
 