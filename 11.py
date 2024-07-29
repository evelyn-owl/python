year = int(input("What year is now? "))

def is_leap(year):
  if year % 4 == 0 and year % 100 != 0:
    return True
  elif year % 400 == 0:
    return True
  else:
    return False

if is_leap(year):
  sec = 60 * 60 * 24 * 366
  print(sec, "seconds")
else:
  seco = 60 * 60 * 24 * 365
  print(seco, "seconds")
  
