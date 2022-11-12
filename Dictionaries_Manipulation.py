#Display Menu options
print("=====MENU=====")
print("1 -> Add Item")
print("2 -> Search")
print("3 -> Exit")

#Allow user to select item in the menu (check if valid)
user = int(input("Select from the Menu:"))
if user > 3:
    print("Invalid")

#Perform the selected option
#- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
				   #Use dictionary to store the info
				   #Use the full name as key
				   #The value is another dictionary of personal information

#- Option 2: Search, ask full name then display the record

#- Option 3: Ask the user if want to exit or retry.