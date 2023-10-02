# This library is a package of resources to use shell commands
import os
# Global Variables
database = list()

os.system("cls")

# Functions
def show_menu():
    print("\n\t\t🏋️  1.- Upload new patient.")
    print("\t\t🕵️  2.- Search for a patient by name.")
    print("\t\t🧙 3.- List every patient.")
    print("\t\t🏃 4.- Exit program.\n")
    option = input("\t»ENTER AN OPTION: ")
    os.system("cls")
    return option

def is_valid_option(option): 
    valid = False    
    msg = ""
    if option.isdigit():
        option = int(option)
        if option >= 1 and option <= 4:
            valid = True
        else:
            msg = "Please enter an option between 1 and 4."
    else:               
        msg = "Wrong option, please enter a valid option."
    return valid, option, msg

print("Welcome to the clinical historic system of the hospital 🏥")
option = 0
while option != 4:
    option = show_menu()
    valid, option, msg = is_valid_option(option)
    print(msg)
    if valid:
        if option == 1:
            name = input("\tEnter the name of the patient: ")
            clinic_history = input("\tEnter the patient's clinic history: ")
            patient = {"name":name, "clinic_history":clinic_history}
            database.append(patient)
            print("Patient added.")
        elif option == 2:
            found = False
            input_name = input("\tEnter the name of the patient you want to find: ").lower()
            for i in range(len(database)):
                for k, v in database[i].items():
                    if k == "name" and v.lower() == input_name:
                        found = True
                        print("\tPATIENT FOUND | CLINIC HISTORY: ", database[i]["clinic_history"])
            if not found:
                print("\tPatient not found.")
        elif option == 3:
            print("LISTING THE ENTIRE DATABASE OF PATIENTS...\n")
            for i in range(len(database)):
                # The method "rjust()"" from String returns a right-justified string with a padding made of spaces
                    print("\tName:".rjust(10),database[i]["name"],"\tClinic history:".rjust(10),database[i]["clinic_history"])                    
            print("\nEND OF DATABASE.")
        else:
            print("See you soon.")