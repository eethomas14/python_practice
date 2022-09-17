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
    "money": 0
}

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}
# Todo 3. Print a report when user enters "report", a report should be generated that shows the current resources.
def report():
    print(f"Water: {resources['water']}, Milk: {resources['milk']}, Coffee: {resources['coffee']}, Money: ${resources['money']}0")
# TODO 4. Check sufficient resources

# TODO 5. Process Coins

def takeMoney(drink):
    owed = MENU[drink]["cost"]
    amount_paid = 0
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many nickels?: "))
    nickels = int(input("How many dimes?: "))
    pennies = int(input("How many pennies?: "))

    if quarters > 1:
        amount_paid += coins["quarter"]*quarters
    elif dimes > 1:
        amount_paid += coins["dime"] * dimes
    elif nickels > 1:
        amount_paid += coins["nickel"] * nickels
    elif pennies > 1:
        amount_paid += coins["penny"] * pennies

    if amount_paid < owed:
        print(f"You have not inserted enough money. The cost is: {owed}")

    elif amount_paid > owed:
        print(f"You Paid: ${float(amount_paid)} Please take your change: ${float(owed - amount_paid)}")
        resources["money"] += owed
    elif amount_paid == owed:
        print("You have given the exact amount")
        resources["money"] += owed


def check_resources(drink):
    ingredient_dict = MENU[drink]["ingredients"]
    processed = False
    for key in ingredient_dict:
        if key in resources:
            if ingredient_dict[key] > resources[key]:
                print(f"There is not enough {key} to complete your order.")
                break
            else:
                resources[key] -= ingredient_dict[key]
                processed = True
    if processed:
        takeMoney(drink)
    else:
        print("Sorry, please come again!")


# TODO 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
user_choice = ""
while user_choice != 'off':
    user_choice = input("What would you like? (espresso/latte/cappuccino?) : ").lower()
    if user_choice != "report":
        check_resources(user_choice)

# TODO 2. Turn off the coffee Machine by entering "off" to the prompt.

# Todo 3. Print a report when user enters "report", a report should be generated that shows the current resources.
    if user_choice == "report":
        report()

