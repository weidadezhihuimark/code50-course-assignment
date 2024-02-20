""" problem:
Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, some programs support “codes,”
whereby you can type, for instance, :thumbs_up:, which will be automatically converted to 👍. Some programs additionally
support aliases, whereby you can more succinctly type, for instance, :thumbsup:, which will also be automatically converted to 👍.

See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with aliases.

In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the “emojized”
version of that str, converting any codes (or aliases) therein to their corresponding emoj"""


pip install emoji

# Importing the emoji module
import emoji

def main():
    # Prompting the user to enter a string containing emoji codes or aliases
    user_input = input("Enter text to emojize: ")

    # Using the emojize function to convert the codes/aliases to emojis
    # The language='alias' parameter allows the function to recognize aliases
    emojized_text = emoji.emojize(user_input, language='alias')

    # Outputting the 'emojized' string
    print(emojized_text)

if __name__ == "__main__":
    main()
