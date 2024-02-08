""" Problem

Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line,
until the user inputs control-d (which is a common way of ending one’s input to a program). Then
output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line
with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively. """

def main():
    # Create an empty dictionary to store grocery items and their counts
    grocery_list = {}

    try:
        # Continuously prompt the user for items
        while True:
            # Get input from the user and convert it to uppercase for case-insensitivity
            item = input("Enter an item: ").upper()

            # Check if the item is already in the grocery list
            if item in grocery_list:
                # If the item is already in the list, increment its count
                grocery_list[item] += 1
            else:
                # If the item is not in the list, add it with a count of 1
                grocery_list[item] = 1
    except EOFError:
        # When the user inputs Control-D, EOFError is raised and caught here

        # Print the grocery list
        print("\nYour Grocery List:")
        # Sort the items in the dictionary alphabetically and print each with its count
        for item in sorted(grocery_list):
            print(f"{grocery_list[item]} {item}")


if __name__ == "__main__":
    # If the script is run directly, call the main function
    main()

