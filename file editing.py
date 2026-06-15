f=open("text.txt",'w')
d={}
d[1]=['k','s']
d[2]=['s','s']
d[3]=['c','s']
d[4]=['d','s']
d[5]=['ka','s']
for i in d:
    f.write(str(d[i]))
f.close()
with open("text.txt",'r') as f:
    print(f.read())
