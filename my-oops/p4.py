class Parent:
    def describe(self):
        print('The Class One') 
        
class Child1(Parent):
    def describe(self):
        print('The Class Two') 
        super().describe()
        
class Child2(Child1):
    def describe(self):
        print('The Class Three') 
        super().describe()
        
obj=Child2()
obj.describe()     
        