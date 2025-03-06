MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

Money = 0

def report():
    print(f"Water: {resources["water"]}ml\n"
          f"Milk : {resources["milk"]}ml\n"
          f"Coffee: {resources["coffee"]}g\n"
          f"Money : ${Money}")

def recipe():
    required_ingredients = MENU[start_machine]["ingredients"]
    # print(required_ingredients)
    difference_quantity = {}
    for key in resources:
        if key in required_ingredients:
            difference_quantity[key] = resources[key] - required_ingredients[key]
    for key in difference_quantity:
        if any(value < 0 for value in difference_quantity.values()):
            print(f"Sorry, not enough {key} available to make {start_machine}")
            break
        else:
            charges()
            for key in resources:
                resources[key] = resources.get(key, 0) - required_ingredients.get(key, 0)
            return resources

def charges():
    global Money
    print("Please insert coins")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))

    total_coins = round(((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)), 2)
    # print(total_coins)
    cost = round(MENU[start_machine]["cost"], 2)
    remainder = round(total_coins - cost, 2)
    # print(cost)
    # return total_coins, cost, remainder
    if total_coins >= cost:
        print(f"Here is ${remainder} in change.")
        print(f"Here is your {start_machine}")
        Money += cost
    elif total_coins < cost:
        print(f"Sorry that's not enough money. Money refunded amount ${total_coins}.")

print("WELCOME TO SAL'S BISTRO COFFEE VENDING MACHINE")
machine_running = True
while machine_running:
    start_machine = input("What would you like? [espresso($1.5)/latte($2.5)/cappuccino($3.0)]: ").lower()

    if start_machine == "report":
        report()

    if start_machine == "off":
        exit()

    if start_machine == "latte":
        recipe()

    if start_machine == "espresso":
        recipe()

    if start_machine == "cappuccino":
        recipe()