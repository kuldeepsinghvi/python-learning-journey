string = str(input("Enter a Name or Number you think is palindrome"))
'''char = []
string = string.strip()
for _ in range(len(string)):
    char.append(string[_])
char2 = char.copy()
char2.reverse()
if( char == char2):
    print(f"{string} is palindrome")
else :
    print(f"{string} is not palindrome")'''
string = string.strip()
string = string.replace(" ","")
string = list(string.lower())
if ( string == string [::-1]):
    print("palindrome")
else :
    print(" not palindrome")