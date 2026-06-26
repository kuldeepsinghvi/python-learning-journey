try:
    if(int(input("Enter a number"))):
        exit
except:
    print("Not a integer")

a = str(input("Enter a string"))
try:
    if(a.isalpha):
        print("Not a String")
except:
    print("a string")