# Write a function describe_number(n) that:

# returns “positive” if n > 0

# returns “zero” if n == 0

# returns “negative” if n < 0

# Ask the user for a number, call the function, and print the message.*

# Write your code here:

n = float(input("Enter a number: "))
def describe_number(n):
    if n > 0:
        print ("positive")
    elif n == 0:
        print ("zero")
    elif n<0:
        print ("negative")
describe_number(n)

    

