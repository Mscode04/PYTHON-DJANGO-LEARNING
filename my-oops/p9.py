# 1.	Super Keyword: Write a program where a subclass calls a method from its parent class using the super() function.
class Parent:
    def man(self):
        print("From The parent")
    
class Child(Parent):
    def man(self):
        print("From The Child")
        super().man()


obj=Child()
obj.man()















