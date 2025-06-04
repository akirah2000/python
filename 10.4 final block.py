try:
    file=open("my file.txt","r")
except ioerror:
    print("Error:Unable to read the file!")
finally:
    file.close()
