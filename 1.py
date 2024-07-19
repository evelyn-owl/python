#print("бнхх тютр, аошч ж сжп рзфал")
#print("ти Клоуторн? Wow")


#a = 5 > 3 ? "hoho" : "hehe"
#name = input("Name ")
#print(name)
alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
message = "бнхх тютр, аошч ж сжп рзфал"
key = 1
result = ""

'''
1.беру першу букву у повідмленні
2.шукаю її номер в алфафіт
3. + key
4. шукаю нову букву в алфафіті
підставляю її в результат

іду наступну букву
'''
for letter in message: #беру першу букву у повідмленні
  x = alphabet.find(letter) #шукаю її номер в алфафіт
  #print(1, x)
  y = x + key # + key
  #print(2, y)
  z = alphabet[y % 33] if x != -1 else letter #шукаю нову букву в алфафіті
  #print(3, z)
  result = result + z #дописую нову букву в рещультат
  #print(4)
  #print(letter, '|', x,'|', y,'|', z,'|', result, '|')
print(message)
print(result)
