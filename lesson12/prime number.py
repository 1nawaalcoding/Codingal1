lower=int(input("enter your lower number:"))
upper=int(input("enter your upper number:"))
print("the prime numbers between",lower,"and",upper)
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
          if  num%i==0:
             break
        else:
           print(num)

        