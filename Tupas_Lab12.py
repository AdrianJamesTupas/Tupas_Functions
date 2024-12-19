#shows the menu prompt of the system,
def menu():
    print("Menu Items: \n1.Cheese Burger - 25.00 \n2.French Fries - 20.00\n3.Soda - 10.00\n4.FriedChicken w/Rice - 80.00")

#def the function for Cheese Burger, calculates the change for burger while also checks if the amount of payment is sufficient
def Burger():
    while True:
        #user cash amount input
        cash = float(input("Enter Payment Amount for CheeseBurger: "))
        #price set for burger
        burger = 25.00
        #calculate change
        if(cash >= burger):
            change = cash - burger
            print("\n\n\n===========================================")
            print("You Bought: CheeseBurger")
            print("--------------------------")
            print("Change Amount: ", change)
            print("Thank You! Please Come Again.")
            print("===========================================")
            break
        #for insufficient amount
        else:
            print("\n\n===========================================")
            print("Insufficient amount of cash, Pls try again.")
            print("===========================================")

#def the function for French Fries, calculates the change for fries while also checks if the amount of payment is sufficient
def Fries():
    while True:
        #user cash amount input
        cash = float(input("Enter Payment Amount for FrenchFries: "))
        # price set for burger
        fries = 20.00
        # calculate change
        if(cash >= fries):
            change = cash - fries
            print("\n\n\n===========================================")
            print("You Bought: French Fries")
            print("--------------------------")
            print("Change Amount: ", change)
            print("Thank You! Please Come Again.")
            print("===========================================")
            break
        # for insufficient amount
        else:
            print("\n\n===========================================")
            print("Insufficient amount of cash, Pls try again.")
            print("===========================================")

#def the function for Soda, calculates the change for Soda while also checks if the amount of payment is sufficient
def Soda():
    while True:
        # user cash amount input
        cash = float(input("Enter Payment Amount for Soda: "))
        # price set for burger
        soda = 10.00
        # calculate change
        if(cash >= soda):
            change = cash - soda
            print("\n\n\n===========================================")
            print("You Bought: Soda")
            print("--------------------------")
            print("Change Amount: ", change)
            print("Thank You! Please Come Again.")
            print("===========================================")
            break
        # for insufficient amount
        else:
            print("\n\n===========================================")
            print("Insufficient amount of cash, Pls try again.")
            print("===========================================")

#def the function for FriedChicken w/Rice, calculates the change for chicken while also checks if the amount of payment is sufficient
def FriedChicken():
    while True:
        # user cash amount input
        cash = float(input("Enter Payment Amount for FriedChicken w/Rice: "))
        # price set for burger
        chicken = 80.00
        # calculate change
        if(cash >= chicken):
            change = cash - chicken
            print("\n\n\n===========================================")
            print("You Bought: FriedChicken w/Rice")
            print("--------------------------")
            print("Change Amount: ", change)
            print("Thank You! Please Come Again.")
            print("===========================================")
            break
        # for insufficient amount
        else:
            print("\n\n===========================================")
            print("Insufficient amount of cash, Pls try again.")
            print("===========================================")

while True:
    #call the menu function
    menu()
    #user input for choosing from the menu
    choose = int(input("Please Choose an Item from the Menu(1-4): "))
    #prompt for choosing menu item number 1
    if(choose == 1):
        #call the Burger function
        Burger()
        break
    # prompt for choosing menu item number 2
    elif(choose == 2):
        # call the Fries function
        Fries()
        break
    # prompt for choosing menu item number 3
    elif(choose == 3):
        # call the Soda function
        Soda()
        break
    # prompt for choosing menu item number 4
    elif(choose == 4):
        # call the FriedChicken function
        FriedChicken()
        break
    #for invalid inputted number of choice
    else:
        print("\n\n===========================================")
        print("Invalid choice. Please try again.")
        print("===========================================")
        continue