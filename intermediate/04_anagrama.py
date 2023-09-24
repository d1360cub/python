word_1 = input('ingrese la primer palabra: ')
word_2 = input('ingrese la segunda palabra: ')

def anagrama (word_1, word_2):
  if word_1.lower() == word_2.lower() or len(word_1) != len(word_2):
    print('no son anagramas')
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
    print(result_1, result_2)
    if result_1 == result_2:
      print('son anagramas')
    else:
      print('no son anagramas')

anagrama(word_1, word_2)