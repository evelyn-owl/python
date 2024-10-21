import os, time

def plist(l):
  for i in l:
    print(i)

todos = []

while True:
  print("🕣 TODO 🕣")
  action = input("What do you want: view, add, remove? ")
  if action == "view" or action == "v":
    plist(todos)
  elif action == "add" or action == "a":
    task = input("What do you want to add? ")
    todos.append(task)
  elif action ==  "remove" or action == "r":
    taskR = input("What do you want to remove? ")
    if taskR in todos:
      todos.remove(taskR)
  time.sleep(1) 
  os.system("clear")
