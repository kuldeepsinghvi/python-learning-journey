a={'a':[1,2,3],'b':2,'c':('ks',3)}
print(a)
print(a.fromkeys('b'))
c=a.pop('b')
print(c)
c=a.popitem()
print(c)
print(a)
b=[]
b=a.pop('a')
print(b)

student={}

student[1]=["kuldeep","singhvi"]
student_k=[]
student_k=student.pop(1)
print(student_k)
f_name = student_k.pop(0)
print(student_k)
student[1]=[f_name,l_name]