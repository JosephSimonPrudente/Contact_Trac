
info = {}


#Display Menu options

def menu():
    print("=====MENU=====")
    print("1 -> Add Item")
    print("2 -> Search")
    print("3 -> Exit")

#Allow user to select item in the menu (check if valid)
while True:
    user = input('Select from the Menu(1-3):')
    try:
        user = int(user)
    except:
        print('Please use numeric digits.')
        continue
    if user > 3:
        print('Please Try again.')
        continue
    break


#Perform the selected option
#- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
				   #Use dictionary to store the info
				   #Use the full name as key
				   #The value is another dictionary of personal information
while True:
    menu()
    if user == 1:
        fullname = input("Full name:")
        age = input("Age:")
        Address = input("Address:")
        Contact = input("Contact No.:")

        info[fullname] = {
        "Age": age,
        "Add": Address,
        "Contact": Contact,
        }
        print("SAVED", info)

        #- Option 2: Search, ask full name then display the record
    if user == 2:
        search = input("Fullname:")
        if search in info:
            for key, value in info[search].items():
                print(key,value)
        else:
            print("Doesnt Match Any info", search)

#- Option 3: Ask the user if want to exit or retry.

    if user == 3:
        Exit = input("You want to Exit or Retry(E/R):")
        if Exit == "E":
            break


    run_again = input("\nWould you like to try again the program?(y/n): ")
    if run_again == "y":
        continue
    else:
        print("Thank you for using the program!")
        break
