class MyClass:
    def __init__(self, public_value, private_value):
        self.public_value = public_value  
        self.__private_value = private_value 

    def get_private_value(self):
        return self.__private_value


obj = MyClass("Public", "Private")
print("Public Value:", obj.public_value)
print("Private Value:", obj.__private_value) 


