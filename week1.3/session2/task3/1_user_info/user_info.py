# Week 1.3, Session 2: Write User Information to a File

# Prompt the user for their name, age, and favorite colour.
name = input("Enter your name: ")
age = input("Enter your age: ")
colour = input("Enter your favorite colour: ")

# Open a file called 'user_info.txt' for writing.
# Write each piece of information to the file, each on a new line.
with open("user_info.txt", "w") as file:
    file.write(name + "\n")
    file.write(age + "\n")
    file.write(colour + "\n")

print("Your information has been saved to user_info.txt")

# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
