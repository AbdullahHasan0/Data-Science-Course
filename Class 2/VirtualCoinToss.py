import random

# Original Approach
side = random.randint(0, 1)  # Generate a random integer, either 0 or 1
if side == 0:
    print("Heads")
else:
    print("Tails")

# Another Approach
side = random.choice(["Heads", "Tails"])  # Randomly choose either "Heads" or "Tails" from the list
print(side)