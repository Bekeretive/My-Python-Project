# Asking the user to enter a number for which they want to find the factorial
number = int(input("Enter the Number: "))

# Initialize factorial to 1, as the factorial of 0 and 1 is 1
factorial = 1

# Check if the entered number is negative
if number < 0:
    print("Sorry, We Can't Compute Factorial for Negative Numbers")

# Check if the entered number is 0 or 1, as factorial for both is 1
elif number < 2:
    print("{}! = {}".format(number, factorial))

# If the entered number is greater than 1, calculate factorial using a loop
else:
    # Loop through the range from the entered number down to 2 (inclusive)
    for num in range(number, 1, -1):
        factorial = factorial * num

    # Print the result
    print("{}! = {}".format(number, factorial))
