num=int(input("enter a number:"))
temp=num
sum=0
while temp>0:
    digit= temp % 10
    sum=sum+digit**3
    temp=temp//10
if num==sum:
    print(num,"is a armstrong number")
else:
       print(num,"is not a armstrong number")