
def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


def main():
    user_input = input("Enter your text: ")
    print(convert(user_input))

main()
