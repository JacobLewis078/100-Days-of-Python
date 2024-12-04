from Info import MENU, resources


def print_resources():
    water_level = resources["water"]
    milk_level = resources["milk"]
    coffee_level = resources["coffee"]
    report_levels = f"Water: {water_level} ml\nMilk: {milk_level} ml\nCoffee: {coffee_level} g\n"
    return report_levels


def turn_off():
    return


def check_resources(coffee):
    water_level = resources["water"]
    milk_level = resources["milk"]
    coffee_level = resources["coffee"]

    if coffee == "espresso":
        water_needed = MENU["espresso"]["ingredients"]["water"]
        coffee_needed = MENU["espresso"]["ingredients"]["coffee"]
        if water_level >= water_needed and coffee_level >= coffee_needed:
            return True
        else:
            return False
    elif coffee == "latte":
        water_needed = MENU["latte"]["ingredients"]["water"]
        coffee_needed = MENU["latte"]["ingredients"]["coffee"]
        milk_needed = MENU["latte"]["ingredients"]["milk"]
        if water_level >= water_needed and coffee_level >= coffee_needed and milk_level >= milk_needed:
            return True
        else:
            return False
    elif coffee == "cappuccino":
        water_needed = MENU["cappuccino"]["ingredients"]["water"]
        coffee_needed = MENU["cappuccino"]["ingredients"]["coffee"]
        milk_needed = MENU["cappuccino"]["ingredients"]["milk"]
        if water_level >= water_needed and coffee_level >= coffee_needed and milk_level >= milk_needed:
            return True
        else:
            return False


def process_coins(q, d, n, p):
    """Takes coin input and calculates the total. Calls function to process transaction"""
    quarter_total = q * .25
    dime_total = d * .10
    nickle_total = n * .05
    penny_total = p * .01
    total = round(quarter_total + dime_total + nickle_total + penny_total, 2)
    return total


def get_change(total, coffee):
    coffee_cost = MENU[coffee]["cost"]
    change = total - coffee_cost
    return change


def legit_transaction(total_payment, coffee):
    espresso_cost = MENU["espresso"]["cost"]
    latte_cost = MENU["latte"]["cost"]
    cappuccino_cost = MENU["cappuccino"]["cost"]

    if coffee == "espresso":
        if total_payment >= espresso_cost:
            return True
        else:
            print("not enough money. Refunding coins")
            return False
    elif coffee == "latte":
        if total_payment >= latte_cost:
            return True
        else:
            print("not enough money. Refunding coins")
            return False
    else:
        if total_payment >= cappuccino_cost:
            return True
        else:
            print("not enough money. Refunding coins")
            return False


def reduce_resources(coffee):
    if coffee == "espresso":
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    else:
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]


def coffee_maker():
    more_coffee = True

    while more_coffee:
        # TODO: Prompt user for which type of coffee they want
        coffee_choice = input("What would you like? (Espresso, Latte, Cappuccino): ").lower()

        # TODO: PRINT REPORT DETAILING HOW MANY SUPPLIES ARE LEFT
        if coffee_choice == "report":
            report = print_resources()

            print(report)

        # TODO: Create off switch for coffee maker
        elif coffee_choice == "off":
            turn_off()

        # TODO: Check resources
        else:
            enough_resources = check_resources(coffee_choice)

            if enough_resources:
                # TODO: Process coins
                print("Please insert coins:")
                quarters = float(input("How many quarters? "))
                dimes = float(input("How many dimes? "))
                nickles = float(input("How many nickles? "))
                pennies = float(input("How many pennies? "))

                total = process_coins(quarters, dimes, nickles, pennies)
                print(f"total inserted coins: ${total}")

                # TODO: Check if coins sufficient for transaction
                good_transaction = legit_transaction(total, coffee_choice)

                # TODO: Make Coffee
                if good_transaction:
                    reduce_resources(coffee_choice)
                    change = get_change(total, coffee_choice)
                    print(f"Your change is: ${change}")
                    print(f"enjoy your {coffee_choice}!")

                another_coffee = input("Would you like another coffee? 'y' or 'n': ")
                if another_coffee == "n":
                    more_coffee = False
            else:
                print("not enough resources for coffee.")
                more_coffee = False


coffee_maker()
