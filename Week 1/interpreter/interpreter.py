def calculated(expression):
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)

    if y == "+":
        value = float(x + z)
    elif y == "-":
        value = float(x - z)
    elif y == "*":
        value = float(x * z)
    elif y == "/":
        value = float(x / z)
    else:
        value = "Invalid operator"
    return value

def main():
    expression_input = input("Expression: ")
    result = calculated(expression_input)
    print(result)  # Print the result instead of returning it

main()
