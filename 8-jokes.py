print("😛 Joke Generator 😎")
print("---------------------")

name = input("What is your name? ")
gender = input("Are you girl or boy? ")


if gender == "girl":
  animal = input("Pick your animal: lamb, penguin, cat. ")
  if animal == "cat":
    input(f"{name.title()}, when is it bad luck to see a black cat? ")
    print("When you're a mouse.")
  elif animal == "penguin":
    input(f"{name.title()}, what do you call a penguin in the desert? ")
    print("Lost.")
  elif animal == "lamb":
    input(f"{name.title()}, what do you call a lamb with a machine gun? ")
    print("Lambo.")

else:
  food = input("Pick your food: soup, sausage, corn. ")
  if food == "corn":
    input(f"{name.title()}, what did the baby corn say to the mother corn? ")
    print("Where's pop corn?")
  elif food == "sausage":
    input(f"{name.title()}, how long will my sausage be? ")
    print("Oh, about 3 inches.")
  elif food == "soup":
    input(f"{name.title()}, there's a fly in my soup! ")
    print("Don't worry, sir, the spider in your salad will get it.")


