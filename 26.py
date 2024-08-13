import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('Boss Battle 1.wav')
sound.play()

def pause():
  pygame.mixer.pause()

pause()

def play(x):
  # Play the sound
  pygame.mixer.pause()
  if x == "1" :
    sound = pygame.mixer.Sound('Boss Battle 1.wav')
    sound.play()
  if x == "2":
    sound = pygame.mixer.Sound('S23-19 ACTION LOOP.wav')
    sound.play()
  
  #pygame.mixer.unpause()
  #while True:
    # Start taking user input and doing something with it
  #  input()

while True:
  # clear the screen 
  os.system("clear")
  # Show the menu
  
  menu = """🎵 MyPOD Music Player

Press 0 to Exit
Press 1 to Play Boss Battle
Press 2 to Play Action Loop

Press anything else to see the menu again.
  """
  print(menu)

  
  # take user's input
  x = input()
  
  # check whether you should call the play() subroutine depending on user's input
  if x == "1" :
    play(x)
  elif x == "0":
    os.system("clear")
    print(menu)
    exit()
  elif x == "2":
    play(x)
  else:
    os.system("clear")
