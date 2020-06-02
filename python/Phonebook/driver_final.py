from Phone_book import Phonebook

decision = input("Do you wanna use the current DB ? \n Y/N:")
if decision == 'Y' or decision == 'y':
    mode = 1
else :
    mode = 0
    
pb = Phonebook(mode)
stmt = """Enter the proper index to utilise functions
        1 : Add a new number
        2 : Update a new Number
        3 : Print all  contacts
        4 : Delete a contact
        5 : Print contact starting with...
        9 : EXIT
        """

while True:

    print(stmt)
    choice = int(input(">"))

    if choice == 1 :
        number = input("Please enter the number:")
        f_name = input("Enter First name : ")
        l_name = input("Enter last name : ")
        email_id = input("Enter email_id, press '-' if not present and press enter : \n")
        designation = input("Enter designation, press '-' if not present and press ente : \n")

        print(pb.add_contact(number, f_name, l_name, email_id, designation))

        continue

    elif choice == 2 :
        print(pb.update_contacts())
        continue

    elif choice == 3 :
        pb.print_contacts()

    elif choice == 4 :
        pb.delete_contacts()
        continue

    elif choice == 5:
        pb.print_contacts(mode = 1)
        continue

    elif choice == 9:
        Phonebook.db.close()
        break
