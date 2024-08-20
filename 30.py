print("""30 Days Down
""")

for i in range(1, 30):
  thought = input(f"Day {i}: ")
  line = f"You thought Day {i} was"
  print(f"{line: ^90}\n{thought: ^90}")
