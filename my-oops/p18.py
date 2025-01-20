class Point:
    def __init__(self, x, y):
        self.x = x  # x coordinate
        self.y = y  # y coordinate

    # Overloading the + operator using __add__
    def __add__(self, other):
        if isinstance(other, Point):
            # Add the corresponding coordinates of two points
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        # This is to give a user-friendly string representation of the Point object
        return f"Point({self.x}, {self.y})"

# Create two Point objects
p1 = Point(3, 4)
p2 = Point(1, 2)

# Add the two points using the overloaded + operator
p3 = p1 + p2

# Print the result
print(p3)  # Output: Point(4, 6)
