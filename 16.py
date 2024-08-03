# attempt 1
print("""Fill in the blank lyrics!
(Type in the blank lyrics and see if you are as cool as me.)
""")

attempts = 0
line = "Almighty crown of _______ "
key = "victory"

while True:
  if attempts == 4:
    key = "crown"
    line = "Almighty _____ of victory"
  if attempts == 7:
    key = "ground"
    line = "Crash into the ______ but at least the nightmare ends"

  attempts += 1
  
  word = input(line)
  if word != key:
    print("Nope, try again.")
    print()
  else:
    print(f"Well done! It only took you {attempts} attempts.")
    break
    
# while True:
#   color = input("Enter a color: ")
#   if color == "red":
#     break
#   else:
#     print(f"I don't like {color}")
# print("I like red!")
