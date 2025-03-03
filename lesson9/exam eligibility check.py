medical_cause=input("Did you have any medical cause Y or N: ")
attendence=int(input(" enter your attendence:"))
if medical_cause=="Y":
     print("you are allowed")
else:
     if attendence>=75:
          print("allowed")  
     else:
          print("not allowed")
