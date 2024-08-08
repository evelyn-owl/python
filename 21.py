print("X Game")
print()
number = int(input("Name your number: "))
score = 0#int((""))
for i in range(1, 11):
  x = int(input(f"{i} * {number} = "))
  if x != i * number:
    print(f"Nope! 😹👎🏼 Answer was {i * number} ")
  else:
    print("Great work!😉✊🏼")
    score += 1

print(f"You scored {score} out of 10.")
if score == 10:
  print("✊🏼💻💅")
