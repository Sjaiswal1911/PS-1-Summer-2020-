import pymysql

class Phonebook(object):
    # Open database connection
    db = pymysql.connect("localhost","root","J@imatadi19","TESTDB" )

    # prepare a cursor object using cursor() method

    cursor = db.cursor()

    contact_count = 0

    def __init__(self,mode):
        # Create table as per requirement
        # Open database connection
        Phonebook.db = pymysql.connect("localhost","root","J@imatadi19","testdb" )

        # prepare a cursor object using cursor() method
        Phonebook.cursor = Phonebook.db.cursor()

        Phonebook.contact_count = 0

        if mode == 0:

            cmd = "DROP TABLE IF EXISTS PHONEBOOK"
            sql = """CREATE TABLE PHONEBOOK (
                F_NAME  VARCHAR(20) NOT NULL,
                L_NAME  VARCHAR(20),
                CONTACT_NO VARCHAR(10),
                EMAIL_ID VARCHAR(30),
                DESIGNATION VARCHAR(30),
                PRIMARY KEY(CONTACT_NO))"""
            Phonebook.cursor.execute(cmd)
            Phonebook.cursor.execute(sql)
            print("New table created.")


    def add_contact(self,number, f_name,last_name, email_id, designation):

        if (Phonebook.contact_count != 0):
            cmd = "SELECT CONTACT_NO from Phonebook"
            Phonebook.cursor.execute(cmd)
            result = Phonebook.cursor.fetchall()
            if number in result:
                return("The number already exists.")

        try:
            temp = """INSERT INTO PHONEBOOK
            (F_NAME,L_NAME,CONTACT_NO,EMAIL_ID, DESIGNATION) VALUES
            ('%s', '%s', '%s', '%s', '%s' ) """ % (f_name,l_name,number,email_id,designation)
            Phonebook.cursor.execute(temp)
            Phonebook.contact_count = Phonebook.contact_count + 1
            Phonebook.db.commit()
            return("Number Added succesfully")

        except:
            return("Operation unsuccessful")

    def print_contacts(self,mode = 0):
        if(Phonebook.contact_count != 0):
            if (mode == 0):
                cmd = "SELECT F_NAME from PHONEBOOK"
            #if (mode == 1):
            #    alpha = input("Enter the alphabet")
            #    cmd = """SELECT F_NAME from PHONEBOOK where F_NAME LIKE "'%s'%" """ % (alpha)
            Phonebook.cursor.execute(cmd)
            result = Phonebook.cursor.fetchall()
            for row in result:
                fname = row[0]
                print(f"Fname -> {fname}")



    def delete_contacts(self):
        if(Phonebook.contact_count == 0):
            return("No contacts to delete.")
        else:
            print("The contacts stored are:")
            self.print_contacts()
            choice = input("Enter first name of the contact to delete:")
            try:
                cmd = "DELETE from PHONEBOOK where F_NAME = '%s'" % (choice)
                Phonebook.cursor.execute(cmd)
                Phonebook.contact_count = Phonebook.contact_count - 1
                self.print_contacts()
                Phonebook.db.commit()
                return("Operation completed successfully")

            except:
                return("Operation unsuccessful")


    def update_contacts(self):

        print("The contacts saved are...")
        self.print_contacts()
        chosen = input("Enter name of contact to be edited")

        stmt = '''1 : First name \t 2 : Last_name \t  3: Number \t
                4 : Email \t  5: Designation
                9 : exit '''

        while True:
            print(stmt)
            choice = int(input())
            if choice == 1:
                change = input("Enter  new First Name : \n")
                cmd = "UPDATE PHONEBOOK SET F_NAME = '%s' where F_NAME = '%s'" %(change,chosen)

            elif choice == 2:
                change = input("Enter new Last name : \n")
                cmd = "UPDATE PHONEBOOK SET L_NAME = '%s' where F_NAME = '%s'" %(change,chosen)

            elif choice == 3:
                change = input("Enter new Number : \n")
                cmd = "UPDATE PHONEBOOK SET CONATCT_NO = '%s' where F_NAME = '%s'" %(change,chosen)

            elif choice == 4:
                change= input("Enter new EMAIL ID : \n")
                cmd = "UPDATE PHONEBOOK SET EMAIL_ID = '%s' where F_NAME = '%s'" %(change,chosen)

            elif choice == 5:
                change = input("Enter new Designation : \n")
                cmd = "UPDATE PHONEBOOK SET DESIGNATION = '%s' where F_NAME = '%s'" %(change,chosen)

            elif choice == 9:
                return("Operation completed.")

            try:
                Phonebook.cursor.execute(cmd)
                Phonebook.db.commit()

            except:
                return("Operation failed")
