"""Problem:
--------------------------
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore
 any integer that isn’t an accepted denomination. """



def main():
    # Initial amount due
    amount_due = 50

    while amount_due > 0:
        try:
            # Prompt user for a coin
            coin = int(input("Insert Coin: "))

            # Check if the coin is valid
            if coin in [25, 10, 5]:
                amount_due -= coin

            # Display the remaining amount if still due
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")

        except ValueError:
            # Handle non-integer inputs
            print("Invalid input. Please insert 25, 10, or 5 cents.")

    # Output change owed
    print(f"Change Owed: {abs(amount_due)}")

if __name__ == "__main__":
    main()

