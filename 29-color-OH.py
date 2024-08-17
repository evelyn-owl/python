def printc(text, color):
  code = "\033[0m"
  if color == "purple":
    code = "\033[35m" 
  elif color == "green":
    code = "\033[32m"  
  elif color == "red":
    code = "\033[31m"
  elif color == "brown":
    code = "\033[33m"
  elif color == "black":
    code = "\033[30m"
  elif color == "grey":
    code = "\033[90m"
  print(f"{code}{text}", end=" ")

printc("With my", "red")
printc("new program", "purple")
printc("I can just call red('and')", "white")
printc("and", "green")
printc("that word will appear in color I set to.", "brown")
printc("Hello", "white")
printc("Hornet E.", "grey")
