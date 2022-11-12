#Display Menu options
print("=====MENU=====")
print("1 -> Add Item")
print("2 -> Search")
print("3 -> Exit")

#Allow user to select item in the menu (check if valid)
user = int(input("Select from the Menu(1-3):"))
if user > 3:
    print("Invalid")

#Perform the selected option
#- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
				   #Use dictionary to store the info
				   #Use the full name as key
				   #The value is another dictionary of personal information

if user == 1:
    fullname = input("Full name:")
    age = input("Age:")
    Address = input("Address:")
    Contact = input("Contact No.:")
    Contacts = {
        "Name":fullname,
        "Age":age,
        "Add": Address,
        "Contact": Contact,
    }
    print("SAVED",Contacts)


#- Option 2: Search, ask full name then display the record
if user == 2:
    search = input("Fullname:")
    if search in Contacts:
        for key, search in Contacts.items():
            print(key,search)
#- Option 3: Ask the user if want to exit or retry.