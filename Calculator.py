print("Welcome to the calculator")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


operations =  {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = int(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        symbol_choice = input("choose a symbol from above: ")
        num2 = int(input("Enter the second number: "))
        calculation_function = operations[symbol_choice]
        answer = calculation_function(num1, num2)
        calculation = (f"{num1} {symbol_choice} {num2} = {answer}")
        print(calculation)

        if input(f"Type 'y' to continue calculating with {answer} or 'n' to exit or 'f' for fresh calculation") == "y":
            num1 = answer

        else:
            should_continue = False
            calculator()

calculator()

