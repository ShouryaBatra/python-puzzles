shopping_list = []

# Welcome message
print("welcome")

# Display menu and handle user input

while True:
    
    

    # Print menu options
    print("heres the menu")
    print("'1' - add item to shopping list")
    print("'2' - remove item to shopping list")
    print("'3' - show shopping list")
    print("'4' - quit")

    choice = input()
    # Get user's choice

    if choice == "1":
        # Add item to shopping list
        print("what item would u like to add?")
        item = input()
        shopping_list.append(item)

    elif choice == "2":
        # Remove item from shopping list
        print("what item would u like to remove?")
        item = input()
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("thats not in the list")

    elif choice == "3":
        print(shopping_list)

    elif choice == "4":
        # Quit the program
        print("bye")
        break

    else:
        # Handle invalid choice
        print("stop it ur not funny")