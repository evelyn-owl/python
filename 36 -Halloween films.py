import os, time

def printl(l):
  for i in l:
    print(i)

people = []
while True:
  print("🎃  Halloween films  👻\n".upper())
  name = input("What is your name? ").strip().title()
  surname = input("What is your surname? ").strip().title()
  fullname = f"{name} {surname}"
  if fullname not in people:
    people.append(fullname)
  else:
    print("You are already in the list!😑🤬")
  print()
  printl(people)
  time.sleep(3)
  os.system("clear")
  
  
