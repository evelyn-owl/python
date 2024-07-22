# питають і запамятовують у змінні
whom = input("Name your addressee > ")
me = input("Name yourself > ")
purchase = input("Name your purchase > ")

# записую кольори у змінні
r = "\033[31m"
c = "\033[36m"
p = "\033[35m"
d = "\033[0m"

# пишу лист
print()
print()
print(f"Dear {c}{whom}{d},")
print()
print(f"Buy me a {p}{purchase}{d}, please.")
print()
print(f"Your {r}{me}{d}.")




  
