try:
    num=int(input("Enter a number:"))
    result=10/num
    print("Result:",result)
except valueError:
    print("Error:Invalid input! Please enter a valid number:")
except zeroDivisionError:
    print("Error:Division by Zero!")
