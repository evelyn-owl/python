bill = float(input("What was the bill?: "))
people = int(input("How many people?: "))
tip = int(input("What tip you want?: "))

tips = bill * tip / 100
tips_x = (tips / people)
bill_x = tips_x + bill / people
answer = round(bill_x, 2)

print(f"You all owe ₴{answer}")
