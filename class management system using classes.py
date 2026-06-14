class Student_Manager():
    
    #check if roll no exist already or not before adding it    
    def set_roll_number(self,student_db,roll_no):
        if(roll_no in student_db.keys()):
            print("Roll no already exist")
            return 1
        else:
            return 0
        
    #add the student to the db
    def add_student(self,student_db,roll_no,f_name):      
        student_db[roll_no]=f_name

    #update the student details in db
    def update_student(self,student_db,roll_no,f_name,l_name):
        student_db[roll_no][1]=f_name
        student_db[roll_no][2]=l_name
        print(f"{roll_no} data have been updated")

    #delete the student details in db after checking if roll_no exist or not
    def Delete_student(self, student_db, roll_no):
        if(roll_no in student_db):
            student_db[roll_no].pop()
            print(f"roll no - {roll_no} Data Has Been Deleted")
        else:
            print(f"roll no - {roll_no} Doesn't Exist !")

    #search for the student data in db using roll no
    def search_student(self, student_db ,roll_no):
        if(roll_no in student_db):
            print(f"roll no - {roll_no}" , f"First Name - {student_db[roll_no][0]}", f"Last Name - {student_db[roll_no][1]}" , sep="\n" )
        else:
            print(f"{roll_no} Doesn't Exist !")

    #print all the student data in the db 
    def all_students(self, student_db):
        print("Here is the list of all student - ")
        for i in student_db.keys():
            print(f" Roll no - {i}")
            print(f"First Name - {student_db[i][0]}")
            print(f"Last Name - {student_db[i][1]}")


class Student:
    def __init__(self,roll_no,f_name,l_name):
             self.roll_no = roll_no
             self.roll_no = f_name
             self.l_name = l_name

choice = 0 
student_db = {}
s1 = Student_Manager()
while( choice != 6):
    print("Menu" , "1. Add a Student ", "2. Update a student details", "3. Delete a student details ","4. search a student " , "5. Print All Student in the database" ,"6. Exit", sep = '\n')
    choice=int(input("Enter Your Choice - "))
    
    if(choice == 1):
        roll_no = int(input("Enter the roll no - "))
        f = s1.set_roll_number(student_db,roll_no)
        if(f== 0):
            f_name , l_name = input("Enter First name and last name - ").split()
            f_name = Student(roll_no,f_name,l_name) 
            s1=s1.add_student(student_db,roll_no,f_name)
        else:
            pass

    elif(choice == 2):
        roll_no = int(input("Enter the roll no whose data needs to be updated - "))
        f_name , l_name = input("Enter First name and last name to be updated- ").split()
        roll_no_new = int(input("Enter the roll no - "))
        s1=s1.update_student(student_db,roll_no,roll_no_new,f_name,l_name)

    elif(choice == 3):
        roll_no = int(input("Enter the roll no whose data needs to be Deleted - "))
        s1=s1.Delete_student(student_db,roll_no)

    elif(choice == 4):
         roll_no = int(input("Enter the roll no whose data needs to be Searched - "))
         s1.search_student(student_db,roll_no)
    
    elif(choice == 5):
        s1.all_students(student_db)
    
    else:
        exit()

        
