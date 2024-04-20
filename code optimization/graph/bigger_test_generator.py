import random

# Define the number of pairs
num_pairs = 10000

# Define the file path
file_path = 'big_test.txt'

# Generate unique pairs
unique_pairs = set()
while len(unique_pairs) < num_pairs:
    value1 = random.randint(1, 20000)
    value2 = random.randint(1, 20000)
    unique_pairs.add((value1, value2))

# Write the unique pairs to the file
with open(file_path, 'w') as file:
    for pair in unique_pairs:
        file.write(f"{pair[0]},{pair[1]}\n")
