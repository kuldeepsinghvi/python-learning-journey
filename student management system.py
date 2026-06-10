def Add_a_Student(Student_DB):
    roll_no = int(input("Enter the roll no - "))
    F_name , L_Name = input("Enter the First name and last name (space in between them ) -").split()
    Student_DB[roll_no]=[F_name , L_Name]

def Update_a_Student(Student_DB):
        Student_update=[]
        Roll_no = int(input("Enter the student Roll no Whose data needs to be updated - "))
        print("1. Change first name", "2. Change Last name " , "3. Change Roll no " ,"5. Exit",sep='\n')
        f=int(input("Enter Your Choice - "))
        if(f==1):
            f_name = input("Enter New First name")
            Student_update=Student_DB.pop(Roll_no)
            l_name = Student_update.pop(1)
            Student_DB[Roll_no]=[f_name,l_name]

        elif(f == 2):
            l_name = input("Enter New Last name")
            Student_update=Student_DB.pop(Roll_no)
            f_name = Student_update.pop(0)
            Student_DB[Roll_no]=[f_name,l_name]
        
        elif(f == 3):
             Student_update=Student_DB.pop(Roll_no)
             Roll_no = input("Enter The New Roll number - ")
             f_name = Student_update.pop(0)
             l_name = Student_update.pop(0)
             Student_DB[Roll_no]=[f_name,l_name]
        
def delete_a_student(Student_DB):
     roll_no = int(input("Enter The Roll Number who Data Need to deleted -"))
     s=[]
     s=Student_DB.pop(roll_no)

def Display_database(Student_DB):
     print(Student_DB)
     
def Search_a_student(Student_DB):
     roll_no = int(input("Enter The Roll Number who Data Need to be Searched -"))
     print(Student_DB[roll_no])
i=0
Student_DB = {}
while(i != 6):
    print("MENU ","1. Add a Student ", "2. Update a Student Data" , "3. Delete a Student Data" ,"4. Display All Student Data","5. Search a Student" ,"6. Exit", sep='\n')
    i = int(input("Enter Your Choice - "))
    if(i == 1):
        Add_a_Student(Student_DB)
    elif(i == 2):
        Update_a_Student(Student_DB)
    elif(i == 3):
         delete_a_student(Student_DB)
    elif(i==4):
         Display_database(Student_DB)
    elif(i==5):
         Search_a_student(Student_DB)