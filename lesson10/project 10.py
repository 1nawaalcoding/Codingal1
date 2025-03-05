base=int(input("enter your base number:"))
exponent=int(input("enter the exponent:"))
result=1
for i in range(exponent):
    result=result*base
print("the result is",result)
