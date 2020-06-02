from company import Company

class Internship_Center(Company):

    # Open database connection
    db = pymysql.connect("localhost","root","J@imatadi19","TESTDB" )

    # prepare a cursor object using cursor() method

    cursor = db.cursor()


    def __init__(self,name,field,MD,type,project,mode = 0):
        if mode == 0:
            cmd = "DROP TABLE IF EXISTS '%s'" %(name)
            sql = """CREATE TABLE '%s' (
                F_NAME  VARCHAR(20) NOT NULL,
                L_NAME  VARCHAR(20),
                ID_NO VARCHAR(15),
                EMAIL_ID VARCHAR(30),
                PROJECT VARCHAR(30),
                COACH VARCHAR(20),
                PRIMARY KEY(ID_NO))"""  %(name)

        super().__init__(elf,name,field,MD,type)
        self.students = []
        self.coach = None

    def set_Coach(self,coach):
        self.coach = coach

    def add_Student(self,student):
        self.students.append(student)
