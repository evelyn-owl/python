# TODO: не питай Камілу про школу та інше 
# пишу у змінні
hero = input("Are you a witch or a human? ")
school = input("Do you study at school? ")
gender = input("Are you a girl or a boy? ")
eyes = input("Do you have 2 eyes? ")
kids = input("Do you have kids? ")

# перевіряю героїв
# Ida, Emity, Bosha, Imperor Belos
# Luz, Camilla
if hero == "witch" and school == "no":
  if gender == "girl":
    print("Hi Ida!")
  else:
    print("Bye-bye Belos!")
elif hero == "witch" and school == "yes":
  if eyes == "yes":
    print("Hi Glove!")
  else:
    print("Hi Ugly!")
elif kids == "yes":
  print("Hi Camilla!")
else:
  print("Go Luz!!!")
