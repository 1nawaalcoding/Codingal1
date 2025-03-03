character=str(input("enter your character:"))
if len(character)==1:
  if ("A"<=character<="Z") or ("a"<=character<="z"):
    print(character,"is a alphabet")
  else:
    print(character,"is not a alphabet")
else:
  print("please enter only one character")
