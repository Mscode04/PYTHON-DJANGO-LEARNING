def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  # Extract the last digit
        n = n // 10      # Remove the last digit
    return total


sum_of_digits(34)