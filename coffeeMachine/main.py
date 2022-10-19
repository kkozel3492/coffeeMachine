# types of coffee
import sys

def checkResources(resources, revenue):
    print(resources['water'])
    print(resources['milk'])
    print(resources['coffee'])
    print(f"${revenue}")

def isResourceSufficient(orderIngredients):
    for item in orderIngredients:
        if orderIngredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def subtractResources(drink, ingredients):
    for key in ingredients:
        resources[key] -= ingredients[key]
    print(f"Here is your {drink}, Enjoy!")

def insertCoins():
    quarters = float(input("How many quarters?: ")) * .25
    dimes = float(input("How many dimes?: ")) * .10
    nickles = float(input("How many nickles?: ")) * .05
    pennies = float(input("How many pennies?: ")) * .01
    total = quarters + dimes + nickles + pennies
    total = round(total, 2)
    return total

def processTransaction(coins, drinkCost):
    if coins >= drinkCost:
        change = round(coins - drinkCost, 2)
        print(f"Here is ${change} in change")
        global revenue
        revenue += drinkCost
        return True
    else:
        print("Sorry that is not enough money. Money refunded")
        return False



import coffeeFile

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

drinks = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
            'milk': 0,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'coffee': 24,
            'milk': 150,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'coffee': 24,
            'milk': 100,
        },
        'cost': 3,
    },

}

coins = {
    'penny': .01,
    'nickle': .05,
    'dime': .1,
    'quarter': .25,
}

# 1. print report 2. check resources? 3. check cash, issue refund 4. make coffee
coffeeOn = True
revenue = 0
while coffeeOn == True:  # Coffee Maker is on and ready for instructions
    waitingForInput = True
    while waitingForInput == True:  # Loop to validate order, reloop after report
        userChoice = input("What would you like?")
        if userChoice == 'report':
            checkResources(resources, revenue)
        elif userChoice == 'off':  # Turn off the machine
            sys.exit("You have successfully turned off the coffee maker.")
        elif userChoice in drinks:  # Assign the userinput to a key in the drinks
            drink = drinks[userChoice]
            waitingForInput = False
        else:
            print("Please select correct option")

#Process order and make coffee
    if isResourceSufficient(drink['ingredients']):
        amount = insertCoins()
        if processTransaction(amount, drink['cost']):
            subtractResources(userChoice, drink['ingredients'])

