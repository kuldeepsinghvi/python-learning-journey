class Standard():
    def __init__(self, std):
        self.std = std
        
class Student():
    
        
    def set_roll_number(self,student_db,roll_no):
        if(roll_no in student_db.keys()):
            print("Roll no already exist")
            return 1
        else:
            return 0

    def add_student(self,student_db,roll_no,f_name,l_name):      
        student_db[roll_no]={f_name,l_name}

    def update_student(self,student_db,roll_no,f_name,l_name):
        student_db[roll_no][1]=f_name
        student_db[roll_no][2]=l_name
        print(f"{roll_no} data have been updated")
    

choice = 0 
student_db = {}
while( choice != 6):
    s1 = Student()
    print("Menu" , "1. Add a Student ", "2. Update a student details", "3. Delete a student details ","4. search a student " , sep = '\n')
    choice=int(input("Enter Your Choice - "))
    if(choice == 1):
        roll_no = int(input("Enter the roll no - "))
        f = s1.set_roll_number(student_db,roll_no)
        if(f== 0):
            f_name , l_name = input("Enter First name and last name - ").split()
            s1=s1.add_student(student_db,roll_no,f_name,l_name)
        else:
            pass

    elif(choice == 2):
        roll_no = int(input("Enter the roll no whose data needs to be updated - "))
        f_name , l_name = input("Enter First name and last name to be updated- ").split()
        roll_no_new = int(input("Enter the roll no - "))
        s1=s1.update_student(student_db,roll_no,roll_no_new,f_name,l_name)
    elif(choice == 3):
        print(student_db)
    else:
        pass

        
