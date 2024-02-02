"""
Probelm:
When texting or tweeting, it’s not uncommon to shorten words to save time or space,
as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py,
implement a program that prompts the user for a str of text and then outputs that same text but with
all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase. """


def remove_vowels(text):
    # Define a string of vowels in both uppercase and lowercase
    vowels = "aeiouAEIOU"

    # Use a list comprehension to create a list of characters from the input text,
    # omitting any that are in the vowels string. Then, join these characters back into a string.
    return ''.join([char for char in text if char not in vowels])

def main():
    # Prompt the user for input and store it in the variable 'text'
    text = input("Input: ")

    # Print the output, which is the result of calling remove_vowels function on the input text
    print("Output:", remove_vowels(text))

# Check if the script is run as the main program and if so, call the main function
if __name__ == "__main__":
    main()
