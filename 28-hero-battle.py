import os, time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('Boss Battle 1.wav')
sound.play()

def dice(side):
  import random

  x = random.randint(1, side)
  #print(f"You rolled {x}")
  return x

def strength():
  return (dice(6) * dice(12) / 2) + 12

def health():
  return (dice(6) * dice(12) / 0.5) + 10

def hero():
  hero = input("Name Your hero: ")
  print()
  race = input("Character Type (Human, Witch, Demon) ")
  print()
  hp = round(health())
  sp = round(strength())
  print(f"{hero}\nHEALTH: {hp}\nSTRENGTH: {sp}")
  print("\nMay the Force be with you!")
  time.sleep(2)
  return (hero, hp, sp)

print("⚔️Character Builder⚔️")
(name1, hp1, sp1) = hero() # генерую 1 героя, зберігаю імя у змінній name1, здоровя у hp1 
print("Who are they battling? ")
(name2, hp2, sp2) = hero() # генерую 2 героя
round_ = 1 
while True:
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  c1 = dice(9)
  c2 = dice(9)
  damage = abs(sp2 - sp1) + 1
  if c1 > c2:
    hp2 = hp2 - damage
    print (f"{name1} wins round {round_}")
    print(f"{name2} takes a hit, with {damage} damage\n")
    print(f"{name1}\nHEALTH {hp1}") 
    print(f"{name2}\nHEALTH {hp2}")  
  elif c2 > c1:
    hp1 = hp1 - damage
    print(f"{name2} wins round {round_}")
    print(f"{name1} takes a hit, with {damage} damage\n")
    print(f"{name1}\nHEALTH {hp1}") 
    print(f"{name2}\nHEALTH {hp2}")  
  else:
    print("Draw!\n\n")
    print(f"{name1}\nHEALTH {hp1}") 
    print(f"{name2}\nHEALTH {hp2}")  

  time.sleep(2)  
  if hp1 < 0:
    print(f"Oh no {name1} has died!")
    print(f"{name2} destroyed {name1} in {round_} rounds!")
    break
  elif hp2 < 0:
    print(f"Oh no {name2} has died!")
    print(f"{name1} destroyed {name2} in {round_} rounds!")
    break
  
  round_ += 1
# again = input("Again? ")
  # if again == "no":
  #   break
  # else:
  #   os.system("clear")

