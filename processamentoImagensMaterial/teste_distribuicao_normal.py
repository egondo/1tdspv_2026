import random

mean = 0
std_dev = 1

# Generate a single random number
sample = random.gauss(mean, std_dev)
print("Single sample:", sample)

# Generate a list of 5 random numbers using a list comprehension
list_samples = [random.gauss(mean, std_dev) for _ in range(5)]
print("List of samples:", list_samples)