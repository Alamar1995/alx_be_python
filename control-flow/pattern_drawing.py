# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Draw the Pattern
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # move to the next line after each row
    row += 1
