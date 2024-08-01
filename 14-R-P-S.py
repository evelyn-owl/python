from getpass import getpass as input

print("E P I C   ✂️ 🧻 🏔️   B A T T L E")
print("Select your move (R, P or S)")

p1 = input("Player 1 > ").lower()
p2 = input("Player 2 > ").lower()

if (p1 == "s" and p2 == "s") or (p1 == "p" and p2 == "p") or (p1 == "r" and p2 == "r"):
  print("Draw 😑")
  
elif (p1 == "s" and p2 == "p") or (p1 == "p" and p2 == "r") or (p1 == "r" and p2 == "s"):
  print("Player 1 WON 😎🏆")
elif (p2 == "s" and p1 == "p") or (p2 == "p" and p1 == "r") or (p2 == "r" and p1 == "s"):
  print("Player 2 WON 😎🏆")
else:
  print(f"Try again. Your moves: {p1}, {p2}")


        
        
        
