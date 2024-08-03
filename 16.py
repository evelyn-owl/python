# attempt 1
print("""Fill in the blank lyrics!
(Type in the blank lyrics and see if you are as cool as me.)
""")
attempts = 0
while True:
  attempts += 1
  word = input("Almighty crown of _______ ")
  if word != "victory":
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
