# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

from pathlib import Path

# open and read the file
def count_words(storytxt):
    try:
        file_path = Path(__file__).with_name(storytxt)
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"{storytxt} - {word_count}")
    except FileNotFoundError:
        print(f"Error: {storytxt} not found.")

# ask the user which story file to open
story_choice = input("Which story file do you want to count?  ")
count_words(story_choice)

# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210