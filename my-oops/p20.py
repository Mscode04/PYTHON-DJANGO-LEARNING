class Base:
    def __init__(self, value):
        self.__private_value = value  # Private attribute, name-mangled with __ to make it private

    def get_value(self):
        return self.__private_value  # Public method to access the private attribute


class Derived(Base):
    def __init__(self, value):
        super().__init__(value)  # Call the __init__ method of the Base class
    
    def display_value(self):
        # Accessing the private attribute of the Base class using the public method
        print(f"Accessing private value from Base class: {self.get_value()}")

# Create an object of Derived class
derived_obj = Derived(10)

# Display the value from the Base class
derived_obj.display_value()  # Output: Accessing private value from Base class: 10
