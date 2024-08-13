import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('hollow.wav')
sound.play()

def pause():
  pygame.mixer.pause()

pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  #while True:
    # Start taking user input and doing something with it
  #  input()

while True:
  # clear the screen 
  os.system("clear")
  # Show the menu
  
  menu = """🎵 MyPOD Music Player

Press 1 to Play
Press 2 to Exit

Press anything else to see the menu again.
  """
  print(menu)

  
  # take user's input
  x = input()
  
  # check whether you should call the play() subroutine depending on user's input
  if x == "1" :
    play()
  elif x == "2":
    os.system("clear")
    print(menu)
    exit()
  else:
    os.system("clear")
