

# pattern_drawing.py

# Prompt user for size of the pattern
size = int(input("Enter the size of the pattern: "))

# Start row counter
row = 0

# While loop to go through rows
while row < size:
    # For loop to print stars in each row
    for col in range(size):
        print("*", end="")
    # Move to the next line after finishing a row
    print()
    row += 1


