    
rows = int(input("Enter the number of rows: "))
number = 1

for i in range(1, rows + 1):
  
    for j in range(rows - i):
        print(" ", end=" ")
    
    for a in range(i):
        print(number, end=" ")
        number += 1
    print()