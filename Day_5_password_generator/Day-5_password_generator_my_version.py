import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    actual_letters = nr_letters - nr_symbols - nr_numbers
    pass_letters = random.sample(letters, actual_letters)
    pass_numbers = random.sample(numbers, nr_numbers)
    pass_symbols = random.sample(symbols, nr_symbols)

    password = pass_letters + pass_symbols + pass_numbers
    random.shuffle(password)
    final_password = ''.join(password)
    print(f"Your password can be: {final_password}")


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many characters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

regenerate = True

while regenerate:
    generate_password()
    new_pass = input(f"Do you want to re-generate password? Type 'y' or 'n': ").lower()
    if new_pass == "y":
        continue
    else:
        regenerate = False
        print("Thank you. Bye")