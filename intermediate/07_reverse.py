user_entry = input('Ingrese la cadena de texto a invertir: ')

def reverse(word):
  initial_word = []
  reversed_word = []
  index = 1
  for letter in word:
    initial_word.append(letter)
  while index <= len(word):
    reversed_word.append(initial_word.pop())
    index += 1
  print(''.join(reversed_word))

reverse(user_entry)