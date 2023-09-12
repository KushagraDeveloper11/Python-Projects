import asciiart
from alldata import MENU
from alldata import resources
import os

def is_resourses_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
    
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item]-= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")
    
def coffee_machine():
    untill_empty=True
    while untill_empty:
        coffee=input("What would you like? \nEspresso(Rs.40/-)\nLatte(Rs.60/-)\nCappuccino(Rs.80/-)\nCheck Status type 'Status'\nType 'Off' to turn off\n")
        if coffee=="Off":
            return False
        elif coffee=='Status':
            print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {resources['money']}\n")
        else:
            drink=MENU[coffee]
            if is_resourses_enough(drink["ingredients"]):
            
                print("Please insert coins.")
                bees_rupay=int(input("How Many Rs.20 coins?: "))
                das_rupay=int(input("How Many Rs.10 coins?: "))
                paanch_rupay=int(input("How Many Rs.5 coins?: "))
                do_rupay=int(input("How Many Rs.2 coins?: "))
                ek_rupya=int(input("How Many Rs.1 coins?: "))

                total_rupees= 20*bees_rupay+10*das_rupay+5*paanch_rupay+2*do_rupay+ek_rupya

                if total_rupees>=drink["cost"]:
                    change=total_rupees-drink["cost"]
                    print(f"Here's your change of Rs.{change}")
                    make_coffee(coffee, drink["ingredients"])
                    
                    resources["money"]+=drink["cost"]
                else:
                    print("Sorry that's not enough money, money refunded.")

        
while input("\nWould you like to order a fresh and hot coffee? Type 'Y' for Yes and 'N' for No: ")=='Y':
    os.system('cls')
    print("\nWelcome to 🚂☕Expersso Coffee Machine! ")
    coffee_machine()
    