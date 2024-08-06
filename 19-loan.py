print("Loan Calculator")

money = int(input("How much money you want to borrow? "))
years = int(input("How many years? "))
interest = int(input("What interest? "))

total = money 
for year in range(years):
  interest_year = total * interest / 100
  total += interest_year 
  print(f"Year {year + 1} is {round(total, 2)}")
print(f"You paid ${round(total - money, 2)} in interest!!!")  
  
# total = 0
# for counter in range(10):
#   print("BEFORE", counter, total)
#   total += counter
#   print("AFTER", counter, total)
