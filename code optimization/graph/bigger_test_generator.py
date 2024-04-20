import random

# Define the number of pairs
num_pairs = 10000

# Define the file path
file_path = 'big_test.txt'

# Write the random values to the file
with open(file_path, 'w') as file:
    for _ in range(num_pairs):
        value1 = random.randint(1, 100)
        value2 = random.randint(1, 100)
        file.write(f"{value1},{value2}\n")
