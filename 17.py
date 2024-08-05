# while True:
#   print("You are in a corridor, do you go left or right?")
#   direction = input("> ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break
from getpass import getpass as input

print("E P I C   ✂️ 🧻 🏔️   B A T T L E")
print("Select your move (R, P or S)")
wins1 =  0
wins2 = 0
while True:
  p1 = input("Player 1 > ").lower()
  p2 = input("Player 2 > ").lower()
  
  if (p1 == "s" and p2 == "s") or (p1 == "p" and p2 == "p") or (p1 == "r" and p2 == "r"):
    print("Draw 😑")
  
  elif (p1 == "s" and p2 == "p") or (p1 == "p" and p2 == "r") or (p1 == "r" and p2 == "s"):
    print("Player 1 WON 😎🏆")
    wins1 += 1   
  elif (p2 == "s" and p1 == "p") or (p2 == "p" and p1 == "r") or (p2 == "r" and p1 == "s"):
    print("Player 2 WON 😎🏆")
    wins2 += 1
  else:
    print(f"Try again. Your moves: {p1}, {p2}")
    #break
  if wins1 == 3:
    print("GAME OVER Player 1 WON 😎🏆")
    break
  if wins2 == 3:
    print("GAME OVER Player 2 WON 😎🏆")
    break


