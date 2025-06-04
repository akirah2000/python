f=open("c:\\users\\Administrator s\\Desktop\\pythonlab\\3.2 add and remove.py","r")
data=f.read()
lw=data.split()
d={}
for word in lw:
    if word not in d:
        d[word]=1
    else:
        d[word]=d[word]+1
    print(d)
