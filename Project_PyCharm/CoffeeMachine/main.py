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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if(order_ingredients[item] >= resources[item]):
            return False
    return True

def process_coins(price):
    quarters = int(input('Enter the number of quarters: '))
    dimes = int(input('Enter the number of dimes: '))
    nickles = int(input('Enter the number of nickels: '))
    pennies =int(input('Enter the number of pennies: '))

    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total

def is_transaction_successful(money_received, price):
    if (price > money_received):
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print('Order processing')
        global profit
        profit += money_received
        change = round(money_received - price, 2)
        print(f"Here's your {change} change.")
        return True

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

while(is_on):
    choice = input('What would you like? (espresso/latte/cappuccino): ')

    if(choice == 'off'):
        print('Machine turned off')
        is_on = False
    elif(choice == 'report'):
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
    else:
        drink = MENU[choice]
        print(drink['ingredients'])
        if(is_resource_sufficient(drink['ingredients'])):
            payment = process_coins(drink['cost'])
            if(is_transaction_successful(payment, drink['cost'])):
                make_coffee(choice, drink['ingredients'])

