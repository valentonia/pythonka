import random

# Set the range of random numbers
min_number = 50
max_number = 50000

# Generate 200 random numbers
random_numbers = [random.randint(min_number, max_number) for _ in range(200)]

# Print the list of random numbers
print(random_numbers)
