import os, time

def prettyPrint(l):
  os.system("clear")
  for i in range(len(l)):
    print(f"{i+1}. {l[i]}\n")
    time.sleep(1)
    print(lorem[i % len(lorem)])
    time.sleep(2)
    os.system("clear")

def plist(l):
  for i in l:
    print(i)

todos = ["read", "eat", "movie", "read", "eat", "movie", "read", "eat", "movie", "read", "eat", "movie"]

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc est ipsum, mollis a purus quis, iaculis mattis purus. Suspendisse iaculis consequat lectus, et suscipit ipsum semper ac. Maecenas mattis egestas sem ac ullamcorper. Etiam blandit sem tortor, sed suscipit sapien laoreet quis. Nam vestibulum, ante a faucibus pharetra, urna magna tincidunt tellus, vitae ornare felis felis varius quam. Pellentesque nec mauris at mi pharetra scelerisque. Nunc ut orci vel nulla finibus lobortis id quis risus. Suspendisse a sem in velit commodo sagittis. Sed feugiat convallis nulla, id vulputate ligula. Vestibulum eget arcu egestas, efficitur lectus et, eleifend ante. Ut a pulvinar quam, eu ornare sem. Nulla vel leo dolor. Morbi diam leo, imperdiet eu hendrerit nec, luctus vitae turpis.
Etiam pharetra felis in gravida posuere. In ornare nulla id quam faucibus rutrum. Aenean aliquet massa ut aliquam laoreet. Nulla sit amet dui quis ante vehicula vulputate. In tincidunt congue vulputate. Sed a consequat enim. Vivamus leo augue, interdum ac consectetur eu, consequat quis urna. Morbi ultricies tempor justo, id consequat tellus bibendum vel.
Proin nec lobortis neque. Proin maximus ipsum augue, at consectetur quam gravida sit amet. Suspendisse potenti. Quisque fermentum rutrum mauris, vel commodo est vestibulum non. Proin ut tempus neque. Cras lobortis, purus vitae varius finibus, dolor tellus ullamcorper sapien, at finibus lectus nulla semper elit. Morbi viverra dui urna, ut faucibus quam consectetur quis. Aenean in consequat ex. Duis pharetra vel justo ac scelerisque. Quisque ac felis sed felis molestie rhoncus eget vel velit. Suspendisse velit velit, dictum at augue sed, scelerisque euismod velit. Sed blandit ut est tincidunt eleifend.
Integer dolor nulla, fermentum non nisi nec, semper sollicitudin dolor. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In sed odio eros. Vestibulum dictum egestas sollicitudin. Pellentesque vel magna maximus, accumsan magna in, tempor mi. Mauris sollicitudin porta dapibus. Donec arcu metus, eleifend imperdiet dignissim at, imperdiet id leo. Suspendisse tincidunt elit malesuada fermentum euismod. Mauris lectus nulla, tristique et rutrum sed, bibendum eget urna. Cras commodo purus posuere nulla lobortis, consequat volutpat odio suscipit. Proin in porttitor mauris. Morbi non semper metus. Etiam sit amet vehicula orci. Praesent condimentum tellus quis odio viverra laoreet. Curabitur lacinia aliquet porta.
Sed eget arcu eu lorem interdum posuere sit amet eu leo. Integer pharetra maximus dui ac lobortis. Phasellus tincidunt convallis augue, a iaculis mi. Aliquam pellentesque, tortor lacinia dapibus tempus, nulla diam maximus eros, sit amet varius justo erat ac justo. Aliquam non neque nec neque luctus efficitur nec a enim. Morbi ornare pretium blandit. Donec finibus gravida magna ac vehicula. Pellentesque porta sapien quis arcu egestas blandit in sit amet est. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.""".split('\n')

while True:
  print("🕣 TODO 🕣")
  action = input("What do you want: view, add, remove, do, clear, edit? ")
  if action == "view" or action == "v":
    plist(todos)
    time.sleep(2)
  elif action == "do" or  action == "d":
    prettyPrint(todos)
  elif   action == "edit" or action == "e":
    taskOld = input("What do you want to edit? ")
    taskNew = input("Type new task ")
    if taskOld in todos:
      i = todos.index(taskOld)
      todos[i] = taskNew
  elif action == "clear" or  action == "c": 
    yesOrNo = input("Do you really want to clear? ")
    if yesOrNo == "yes" or yesOrNo == "y":
      todos.clear()  
  elif action == "add" or action == "a":
    task = input("What do you want to add? ")
    todos.append(task)
  elif action ==  "remove" or action == "r":
    taskR = input("What do you want to remove? ")
    yesOrNo = input("Do you really want to remove? ")
    if (yesOrNo == "yes" or yesOrNo == "y") and taskR in todos:
      todos.remove(taskR)
  time.sleep(1) 
  os.system("clear")
