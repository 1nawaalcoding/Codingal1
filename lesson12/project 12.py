dec=int(input("enter a decimal number:"))
binary=""
while dec>0:
    binary=str(dec%2)+binary
    dec=dec//2
print("the binary value is",binary)
