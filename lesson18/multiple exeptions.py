try:
    num1,num2=eval(input("enter two numbers separated by a comma:"))
    result=num1/num2
    print("the quotient is:",result)
except ZeroDivisionError:
    print("there is zero division error")
except SyntaxError:
    print("there is a syntax error, enter numbers separated by a comma like this:1,2")
except ValueError:
    print("please enter a right value")
except:
    print('wrong input')
else:
    print("there is no exeption")
finally:
    print("this will execute no matter what.")