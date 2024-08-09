import random
from getpass import getpass as inputs

print("guess the number")

x = random.randint(1, 1000000)
# x = int(inputs("Write your secret number "))
c = 0

while True:
  c += 1
  guess = int(input("What is your guess? "))
  if guess < 0:
    exit()
  if guess == x:
    print("Correct! ")
    break
  elif guess < x:
    print("Too low")
  else:
    print("Too high")
print(f"It took you {c} guesses ")

# import random

# for _i in range(10):
#   myNumber = random.randint(1, 100000)
#   print(myNumber)
