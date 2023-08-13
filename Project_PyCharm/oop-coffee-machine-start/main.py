from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()

moneyMachine.report()
coffeeMaker.report()

is_True = True

while(is_True):
    options =  menu.get_items()
    choice = input(f"What would you like to have from ({options}): ")

    if(choice == 'off'):
        is_True = False
    elif(choice == 'report'):
        moneyMachine.report()
        coffeeMaker.report()
    else:
        drink = menu.find_drink(choice)
        if(coffeeMaker.is_resource_sufficient(drink)):
            if(moneyMachine.make_payment(drink.cost)):
                coffeeMaker.make_coffee(drink)

