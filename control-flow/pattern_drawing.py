# Prompt the user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer while loop for each row
while row < size:
    # Inner for loop to print asterisks in the current row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
