print("ugly score calculator")

exam = input("Name of exam: ")
score = int(input("Max. Possible Score? "))
your_score =int( input("Your score: "))

p = (your_score/score)*100
p = round(p, 2)

if p >= 90:
  print(f"You got {p} % which is a A+ 👼")
elif p >= 80:
  print(f"You got {p} % which is a A 😕")
elif p >= 70:
  print(f"You got {p} % which is a B 😟")
elif p >= 60:
  print(f"You got {p} % which is a C ☹️")
elif p >= 50:
  print(f"You got {p} % which is a D 😳")
elif p <  50:
  print(f"You got {p} % which is a U 😈")
  
