Amount= int (input("enter amount for withdrawl "))
note_1=Amount//100
note_2=(Amount%100)//50
note_3=((Amount%100)%50)//10
print("the hundred notes are",note_1)
print("the fifty notes are",note_2)
print("the tens notes are",note_3)
