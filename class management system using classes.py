class Standard():
    def __init__(self, std):
        self.std = std
        
class Student(Standard):
    def __init__(self):
        self.super()
        
    def set_roll_number(self,roll_no):
        if(roll_no in self):
            print("Roll no already exist")
        else:
            pass
    

choice = 0 
while( choice != 6):
    print("Menu" , "1. Add a Student ", "2. Update a student details", "3. Delete a student details ","4. search a student " , sep = '\n')
    choice=int("Enter Your Choice - ")
    if(choice == 1):
        roll_no = int(input("Enter the roll no - "))
        
