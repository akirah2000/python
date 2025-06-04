f=open("c:\\users\\Administrator s\\Desktop\\pythonlab\\8.5 file and write,read content.py","r")
print("The file pointer is at byte:",f.tell())
f.seek(10);
print("After reading,the file pointer is at:",f.tell())
