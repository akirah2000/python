try:
    num=int(input("Enter a number:"))
    result=10/num
except valueError:
    print("Error:Invalid input!Please enter a valid number.")
except zerodivisionerror:
    print("Error:Division by zero!")
else:
    print("Result:",result)
