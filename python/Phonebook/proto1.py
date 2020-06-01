import pymysql

class Phonebook(object):
    # Open database connection
    db = pymysql.connect("localhost","root","J@imatadi19","TESTDB" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    contact_count = 0

    def __init(self):
        # Create table as per requirement
        sql = """CREATE TABLE PHONEBOOK (
           F_NAME  VARCHAR(20) NOT NULL,
           L_NAME  VARCHAR(20),
           CONTACT_NO VARCHAR(10),
           EMAIL_ID VARCHAR(30),
           DESIGNATION VARCHAR(30),
            PRIMARY KEY(CONTACT_NO))"""

        Phonebook.cursor.execute(sql)
        Phonebook.db.close()

    def add_contact(self):
        number = input("Please enter the number:")
        if (Phonebook.contact_count != 0):
            cmd = "SELECT CONTACT_NO from Phonebook"
            Phonebook.cursor.execute(cmd)
            result = Phonebook.cursor.fetchall()
            if number in result:
                return("The number already exists.")
        else:
            f_name = input("Enter First name:")
            l_name = input("Enter last name:")
            email_id = input("Enter email_id, press '-' if not present and press enter")
            designation = input("Enter designation, press '-' if not present and press enter")
            #try:
            temp = """INSERT INTO PHONEBOOK
            (F_NAME,L_NAME,CONTACT_NO,EMAIL_ID, DESIGNATION) VALUES
            ('%s', '%s', '%s', '%s', '%s' ) """ % (f_name,l_name,number,email_id,designation)
            Phonebook.cursor.execute(temp)
            Phonebook.contact_count += 1
            return("Number Added succesfully")

            #except:
            #    return("Operation unsuccessful")

    def print_contacts(self):
        if(Phonebook.contact_count != 0):
            cmd = "SELECT F_NAME from PHONEBOOK"
            Phonebook.cursor.execute(cmd)
            result = Phonebook.cursor.fetchall()
            print(result)
        else:
            return(None)





pb = Phonebook()
#print(pb.add_contact())
#print(pb.print_contacts())
