import re
import os

all_contacts = dict() # Dictionary keeps track of all contacs and their information

# Function to print all availabe options for the user
def printInstructions():
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contact to text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

# Function to add a new contact
def addContact(phone_number):
    # If phone number is already saved in contacts, notify user 
    if phone_number in all_contacts.keys():
        print("You already has this number save in your contacts.")
    # Otherwise, take input for name and email
    else:
        name = input("Please enter the name of the contact you'd like to add: ")
        email = input("Please enter the email of the contact you'd like to add: ")
        # Store provided data in nested dictionary
        all_contacts[phone_number] = {"Name" : name, "Email" : email}
        print(f"{name} has been saved in your contacts with the phone number: {phone_number}.")

# Function to edit an existing contact
def editContact(phone_number):
    while True: # Loop until user quits, or a name or email has been edited
        quit = False
        # Verify that the phone number correlates to a contact
        if phone_number in all_contacts.keys():
            print (all_contacts[phone_number]) # Display the selected contact to the user
            user_input1 = input("Would you like to edit the 'name' or 'email': ") # Get input for what needs changing
            if user_input1.lower() == "name":
                user_input2 = input("What would you like to change the name to: ") # Get input for what the name should be changed to
                all_contacts[phone_number]["Name"] = user_input2
                break
            elif user_input1.lower() == "email":
                user_input2 = input("What would you like to change the email to: ") # Get input for what the email should be changed to
                all_contacts[phone_number]["Email"] = user_input2
                break
            elif user_input1.lower() == "quit": # Quit the loop if requested by user
                quit = True
                break
            else:
                print("Please select an option from 'name', 'email', or 'quit'")
        # Notify user if they've entered an incorrect phone number
        else:
            if not quit:
                print("This number is not saved in your contacts.")
            break

# Function to delete a contact
def deleteContact(phone_number):
    # Verify the provided phone number correlates to an existing contact
    if phone_number in all_contacts.keys():
        deleted_contact = all_contacts.pop(phone_number) # Remove contact from dictionary and display the contact to the user
        print(f"{deleted_contact["Name"]} has been removed from your contacts.")
    # Notify user if they've entered an incorrect phone number
    else:
        print("This number is not saved in your contacts.")

# Function to search for a contact from a phone number
def searchContact(phone_number):
    # Verify the provided phone number correlates to an existing contact
    if phone_number in all_contacts.keys():
        name = all_contacts[phone_number]["Name"] # Store the name of the contact
        email = all_contacts[phone_number]["Email"] # Store the email of the contact
        # Display the stored information to the user based on the phone number provided
        print(f"Phone Number: {phone_number}")
        print(f"Name: {name}")
        print(f"Email: {email}")
    # Notify user if they've entered an incorrect phone number
    else:
        print("This number is not saved in your cantacts.")

# Function to display all contacts currently saved
def displayContacts():
    # Notify user if no contacts are saved, so none can be displayed
    if len(all_contacts) == 0:
        print("You have no contacts saved.")
    else:
        for key, value in all_contacts.items(): # Loop through all stored contacts
            name = value["Name"]
            email = value["Email"]
            print(f"Phone Number: {key} - Name: {name}, Email: {email}") # Display all information about each contact to the user

# Function to export all contacts to a text file
def exportContacts():
    file = open("contacts.txt", "w") # Creates a new file if it doesn't exist, or it will modify an existing one with the same name
    for key,value in all_contacts.items(): # Loop through all saved contacts
        name = value["Name"]
        email = value["Email"]
        file.write(f"Phone Number: {key} - Name: {name}, Email: {email}\n") # Each contacts information is stored in a single line
    print("Your contacts have been exported to the text file name 'contacts.txt'") # Notify user once the contacts have been exported to the text file
    file.close() # Close file

# Function to import all contacts from a specified text file
def importContacts(path):
    file = open(path, "r") # Open file from provided path
    count = 0 # This keeps track of the total number of contacts added
    for line in file: # Loop through each line in the file (each line will contain information about exactly one contact)
        count += 1
        number = re.search(r"(?<=Phone Number: )\d+", line) # Extract the phone number using regex
        number = int(number.group())

        name = re.search(r"(?<=Name: ).*(?=,)", line) # Extract the name using regex
        name = name.group()

        email = re.search(r"(?<=Email: ).*", line) # Extract the email using regex
        email = email.group()

        all_contacts[number] = {"Name" : name, "Email" : email} # Save the extracted information in the nested dictionary

    print(f"You have imported {count} contacts.") # Notify user how many contacts have been imported
    file.close() # Close file

# Main method which runs the command line interface in order to interact with the user
if __name__ == "__main__":
    print("Welcome to the Contact Management System.")
    printInstructions()

    while True: # Continue to loop until the user chooses to exit
        # Verify that the user enters a valid number
        try:
            user_input_num = int(input("Please enter a number from the options above: "))
        except ValueError:
            print("Please enter a valid number.")
        else:
            # Verify that the user enters a valid number from the list of options provided
            if (user_input_num < 1 or user_input_num > 8):
                print("Please enter a number from 1-8.")

            # If user enters '1' they'd like to add a new contact
            elif (user_input_num == 1):
                while True:
                    try:
                        phone_number = int(input("Please enter the phone number of the contact you'd like to add: "))
                        break
                    except ValueError:
                        print("Please enter a valid phone number using only digits.")

                addContact(phone_number)
                printInstructions()

            # If user enters '2' they'd like to edit a contact
            elif (user_input_num == 2):
                while True:
                    try:
                        phone_number = int(input("Please enter the phone number of the contact you'd like to edit: "))
                        break
                    except ValueError:
                        print("Please enter a valid phone number using only digits.")
                
                editContact(phone_number)
                printInstructions()

            # If user enters '3' they'd like to delete a contact
            elif (user_input_num == 3):
                while True:
                    try:
                        phone_number = int(input("Please enter the phone number of the contact you'd like to delete: "))
                        break
                    except ValueError:
                        print("Please enter a valid phone number using only digits.")

                deleteContact(phone_number)
                printInstructions()

            # If user enters '4' they'd like to search for a contact
            elif (user_input_num == 4):
                while True:
                    try:
                        phone_number = int(input("Please enter the phone number of the contact you'd like to search for: "))
                        break
                    except ValueError:
                        print("Please enter a valid phone number using only digits.")
                
                searchContact(phone_number)
                printInstructions()

            # If user enters '5' they'd like to display all contacts saved
            elif (user_input_num == 5):
                displayContacts()
                printInstructions()

            # If user enters '6' they'd like to export all contacts saved to a text file
            elif (user_input_num == 6):
                exportContacts()

            # If user enters '7' they'd like to import contacts from an uploaded text file
            elif (user_input_num == 7):
                input_path = input("Please upload the text file and enter it's name without the .txt extension: ")
                input_path = input_path + ".txt"
                if (os.path.isfile(input_path)):
                    importContacts(input_path)
                else:
                    print("The text file could not be found from the path entered.")
                printInstructions()

            # If user enters '8' exit the loop and end the program
            elif (user_input_num == 8):
                break