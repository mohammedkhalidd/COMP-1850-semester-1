# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:

# Ask a user to enter two numbers (one per input)
try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))

    # multiply those numbers together

    result = num1 * num2

    # print out the result
    print(result)
except:
    print("That is not a number")

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!