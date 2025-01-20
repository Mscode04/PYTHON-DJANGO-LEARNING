# 1.	Iterators: Create a class that implements an iterator to iterate over numbers from 1 to 10.

class Num:
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
        self.n=1
        return self
    def __next__(self):
        if self.n <= self.max:
            result=self.n
            self.n+=1
            return result
        else:
            raise StopIteration
num=Num(10)   
I=iter(num)
print(next(I)) 
print(next(I)) 
print(next(I)) 
print(next(I)) 
print(next(I)) 
print(next(I)) 
print(next(I)) 
print(next(I)) 
print(next(I)) 
print(next(I)) 
 
        