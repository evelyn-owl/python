import os, time


def dice(side):
  import random

  x = random.randint(1, side)
  #print(f"You rolled {x}")
  return x

def strength ():
  return (dice(6) * dice(12) / 2) + 12

def health():
  return (dice(6) * dice(12) / 2) + 10

while True:
  print("⚔️Character Builder⚔️")
  hero = input("Name Your hero: ")
  print()
  race = input("Character Type (Human, Witch, Demon) ")
  print()
  hp = round(health())
  sp = round(health())
  print(f"{hero}\nHEALTH: {hp}\nSTRENGTH: {sp}")
  print("\nMay the Force be with you!")
  time.sleep(2)
  again = input("Again? ")
  if again == "no":
    break
  else:
    os.system("clear")
    
