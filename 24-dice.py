print("🎲 Infinity Dice 🎲 ")
def dice(side):
  import random

  x = random.randint(1, side)
  print(f"You rolled {x}")


sides = int(input("How many sides?: "))
while True:
  dice(sides)  
  again = input("Roll again? ")
  if again == "no":
    exit()
  else:
    print()
    