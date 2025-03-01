s1=int(input("enter your speed:" ))
s2=int(input("enter your speed:" ))
s3=int(input("enter your speed:" ))
average=(s1+s2+s3)/3
if s1<average:
    print("s1 is slower than the average with difference of",average-s1)
if s2<average:
    print("s2 is slower than the average with difference of",average-s2)

if s3<average:
    print("s3 is slower than the average with difference of",average-s3)
