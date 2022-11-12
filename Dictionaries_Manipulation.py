print("PROGRAMMED BY: JOSEPH SIMON PRUDENTE")
info = {}

def menu():
    print()
    print("============MENU===========")
    print()
    print("        1 -> Add Item")
    print("        2 -> Search")
    print("        3 -> Exit")
    print("        4 -> Values")
    print()
    print("===========================")
    print()

while True:
    menu()
    user = int(input('Select from the Menu(1-4):'))
    if user > 0 and user <= 4:
            print("You entered a valid number")

    if user == 1:
        fullname = input("Full name:")
        age = int(input("Age:"))
        Address = input("Address:")
        Contact = int(input("Contact No.:"))

        info[fullname] = {
        "Age:": age,
        "Add:": Address,
        "Contact:": Contact,
        }
        print("SAVED", info)


    elif user == 2:
        search = input("Fullname:")
        if search in info:
            for key, value in info[search].items():
                print(key,value)
        else:
            print("Doesnt Match Any info About", search)


    elif user == 3:
        Exit = input("You want to Retry or Exit(R/E):")
        if Exit == "R":
            continue
        else:
            print("Thank you")
            break

    elif user == 4:
        print(len(info))

    else:
        print("You must enter a number between 1 to 4")
        continue

    run_again = input("Would you like to try again the program?(y/n): ")
    if run_again == "y":
        continue
    else:
        print("Thank you")
        break

