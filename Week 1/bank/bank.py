def main():
    greeting = input("Enter your greeting: ").strip().lower()
    # The strip() funcion is used to remove any leading and trailing whitespace from a string. It's used in wcb workpace many times
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
