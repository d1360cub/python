word_1 = input('ingrese la primer palabra: ')
word_2 = input('ingrese la segunda palabra: ')

def anagrama (word_1, word_2):
  if word_1.lower() == word_2.lower() or len(word_1) != len(word_2):
    print('no son anagramas según función anagrama')
  else:
    word_1 = word_1.lower()
    word_2 = word_2.lower()
    list_1 = []
    list_2 = []
    for letter in word_1:
      list_1.append(letter)
    for letter in word_2:
      list_2.append(letter)
    list_1.sort()
    list_2.sort()
    result_1 = ''.join(list_1)
    result_2 = ''.join(list_2)
    if result_1 == result_2:
      print('son anagramas según función anagrama')
    else:
      print('no son anagramas según función anagrama')

def anagram (word_1, word_2):
  if word_1.lower() == word_2.lower() or len(word_1) != len(word_2):
    print('no son anagramas según función anagram')
  elif (sorted(word_1.lower()) == sorted(word_2.lower())):
    print('son anagramas según función anagram')
  else:
    print('no son anagramas según función anagram')
    

anagrama(word_1, word_2)
anagram(word_1, word_2)