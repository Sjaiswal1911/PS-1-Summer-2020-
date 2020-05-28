class ContactBook(object):

    def __init__(self):
        self.contacts = []
        self.contact_names = []

    def add_Contact(self):
        print("Hello adding now.")

        # taking the mobile number as input
        number = input("Please enter the contact number :")
        while (len(number) != 10):
            del number
            number = input("Please enter a valid contact number :")

        # to check if the number already exists
        if(len(self.contacts) != 0):
            for contact in self.contacts:
                if(number in contact.numbers):
                    target = contact
                    print("The number already exists!")
                    print("Do you wanna update it: Y/N")
                    choice = input()
                    if (choice == "y" | choice == "Y" ):
                        self.update_Contact(target)
                    elif (choice == "n" | choice == "N" ):
                        return("Operation Terminated.")
                    else :
                        return("Learn to type, please :)")

        name = input("Enter enter the name for the contact:")
        self.contact_names.append(name)
        self.contacts.append(Contact(number,name))

        print('''Do you wish to add further details?
        Press 1 for yes. 9 for no and exit)''')
        choice = input()
        if choice == '1':
            print("Press the appropriate key to do the following")
        elif choice == '9':
            return("Contact added successfully.")
        else:
            print("Learn to type")
            return("Contact saved, NOOB")

        return(self.update_Contact(index = -1,mode = 0))


    def update_Contact(self, index, mode):
        # mode 0 : adding new numbers
        # mode 1: Updating old numbers
        if mode == 0:
            stmt = '''1 : emailID \t 2 : address \t  3: Designation \t
             9 : exit '''
        else :
            stmt = '''1 : emailID \t 2 : address \t  3: Designation \t
                    4 : name \t  5: number  \t 6 : Add number
                    9 : exit '''

        while True:
            print(stmt)
            choice = int(input())
            if choice == 1:
                self.contacts[index].emailID = input("Enter email id")
                continue
            elif choice == 2:
                self.contacts[index].address = input("Enter address")
                continue
            elif choice == 3:
                self.contacts[index].Designation = input("Enter Designation")
                continue
            elif choice == 4:
                self.contacts[index].name = input("Enter new name")
                continue
            elif choice == 5:
                print(self.contacts[index].numbers)
                num_index = input("Choose the index of no. to edit")
                try:
                    num = input("Input new number")
                    self.contacts[index].numbers[num_index] = num
                except:
                    print("You are dumb")
                continue
            elif choice == 6:
                num = input("Enter number to be added")
                self.contacts[index].numbers.append(num)
                continue
            elif choice == 9:
                break

    def findIndex(self,target):
        i = 0
        for con in self.contacts:
            if con.name == target:
                return i
            i = i + 1

    def print_Names(self):
        self.contact_names.sort()
        for name in self.contact_names:
            print(name)


class Contact(object):

    def __init__(self,number,name):

        self.numbers = []
        self.numbers.append(number)
        self.name = name
        self.emailID = None
        self.Address = None
        self. Designation = None

cb = ContactBook()
while True:
    print("what do you wanna do?")
    print("Enter relevant digit")
    print(''' 1: Add new number
            2: Update existing
            3: Delete a number
            4: View all numbers
            5: View numbers starting with''
            9: EXIT ContactBook
            ''' )
    choice = int(input())
    if (choice == 1):
        cb.add_Contact()
        continue
    elif (choice == 2):
        print("The contacts stored are:")
        cb.print_Names()
        target = input("Enter name to be edited")
        try :
            cb.update_Contact(index = cb.findIndex(target) , mode =1)
        except:
            pass    
        continue
    elif (choice == 9):
        break
