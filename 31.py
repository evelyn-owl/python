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
  elif color == "blue":
    code = "\033[34m"
  print(f"{code}{text}", end="")

e = "="
title = "=  Music App  ="

printc(f"{e: >20}", "green")
printc(f"{e}", "black")
printc(f"{title}", "red")
printc(f"{e}", "black")
printc(f"{e}", "green")
print()
band = "Evanescense"
print("🎧🔥 Whisper")
printc(f"{band: >16}", "blue")
print()
print()
printc("PREV\n", "white")
printc(f"{'NEXT': >9}\n", "green")
printc(f"{'PAUSE': >15}", "red")
