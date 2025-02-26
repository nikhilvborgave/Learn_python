def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#This piece of code was created without watching the video.
#In lecture, Angela provides multiple TODOs as we go along with video

# continue_calculation = True
# first_number = None
# while continue_calculation:
#     if first_number is None:
#         first_number = int(input("What is your first number?: "))
#     operations = ["+", "-", "*", "/"]
#     for symbols in operations:
#         print(symbols)
#     operation = input("Pick an operation: ")
#     second_number = int(input("What is your second number? "))
#
#     if operation == "+":
#         result = add(n1=first_number, n2=second_number)
#         print(f"{first_number} {operation} {second_number} = {result}")
#     if operation == "-":
#         result = substract(n1=first_number, n2=second_number)
#         print(f"{first_number} {operation} {second_number} = {result}")
#     if operation == "*":
#         result = multiply(n1=first_number, n2=second_number)
#         print(f"{first_number} {operation} {second_number} = {result}")
#     if operation == "/":
#         result = divide(n1=first_number, n2=second_number)
#         print(f"{first_number} {operation} {second_number} = {result}")
#
#     restart = input(f"Type 'y' to continue with {result}, or type 'n' to start new calculation:    ")
#     if restart == "y":
#         continue_calculation = True
#         first_number = result
#     elif restart == "n":
#         continue_calculation = False
#         print("Restarting.....")
#         print("\n" * 20)
#         continue_calculation = True
#         first_number = None

# Below piece of code is according to Angela's TODOs
# TODO: add these 4 functions into a dictionary as the values. keys = "+","-","*","/".
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

#TODO: use the dictionary operatios to perform calculations

# multiplication = operations["*"]
# print(multiplication(2, 5))

#TODO: final project

continue_calculation = True
first_number = None
while continue_calculation:
    if first_number is None:
        first_number = int(input("What is your first number?: "))
    for key in operations:
        print(key)
    symbol = input("Pick an operation: ")
    second_number = int(input("What is your second number? "))

    if symbol in operations:
        result = operations[symbol](n1=first_number, n2=second_number)
        print(f"{first_number} {symbol} {second_number} = {result}")

    restart = input(f"Type 'y' to continue with {result}, or type 'n' to start new calculation:    ")
    if restart == "y":
        continue_calculation = True
        first_number = result
    elif restart == "n":
        continue_calculation = False
        print("Restarting.....")
        print("\n" * 20)
        continue_calculation = True
        first_number = None