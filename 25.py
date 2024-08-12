def dice(side):
  import random

  x = random.randint(1, side)
  #print(f"You rolled {x}")
  return x

def hp():
  return dice(6) * dice(8)
  
print("⚔️ Character Stats Generator ⚔️")
hero = input("Name your warrior: ")
health = hp() 
print(f"Their health is: {health} hp")
