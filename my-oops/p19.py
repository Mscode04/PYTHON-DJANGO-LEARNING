class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit  # The maximum number up to which Fibonacci series is generated
        self.a, self.b = 0, 1  # The first two numbers in the Fibonacci series

    def __iter__(self):
        return self  # Returns the iterator object itself

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration  # Stop the iteration when the limit is reached
        current_value = self.a
        self.a, self.b = self.b, self.a + self.b  # Update the values to the next Fibonacci numbers
        return current_value


# Create a FibonacciIterator object with a limit
fib_iterator = FibonacciIterator(50)


for num in fib_iterator:
    print(num)
