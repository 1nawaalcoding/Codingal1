def factorial(x):
    '''this is a recursive function to find the factorial of a integer'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("factorial of 0 is",factorial(0))
print("factorial of 1 is",factorial(1))
print("factorial of 5 is",factorial(5))