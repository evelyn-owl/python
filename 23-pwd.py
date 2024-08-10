# import uuid;

## genarate random password
# for i in range(15):
#   x = uuid.uuid4().hex.upper()[0:6]
#   print(x)

def login():
  users = {
    "Ida": "Clowtorni",
    "Emira": "123m",
    "Edric": "123d",
    "Stringbean": "123t",
    "Willow": "plants",
    "Collector": "123o",
    "Vee": "123e",
    "Gus": "illusions",
    "Luz": "witch",
    "Camila": "123a",
    "Amity": "slime",
    "Hunter": "123u",
    "King": "titan",
    "Lilith": "123i",
    "Flapjack": "123l",
  }
  
  while True:
    print()
    name = input("What is your username?: ")
    password = input("What is your password? ")
    if users.get(name) == password: #(password == "123" and name == "Ida"):
      print("Welcome to Boiling Isles!!!!!!!")
      break
    elif name == "Belos" or name == "belos":
      print("Eat dirt, Belos!!!!!!😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡")
      break
    else:
      print("Do you look like a Belos? 😡😡😡😡😡😡😡😡😡😡😡😡😡")  
  
login()


#Eat dirt, Belos!!!!!!😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡
#Emira, Edric, Stringbean, Willow, Collector, Vee, Gus, Luz, Camila, Amity, Hunter King, Lilith, Flapjack.
# users = {
#   "Ida": "123"
# }

# print(users.get("Ida"))
# print(users.get("opos"))
