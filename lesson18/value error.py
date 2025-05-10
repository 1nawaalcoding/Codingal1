try:
    n=int(input("enter a number:"))
    print("the number entered is:",n)
except ValueError as ex:
    print("The value error is",ex)
    