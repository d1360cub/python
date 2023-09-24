def fizzbuzz():
  number = 1
  while(number <= 100):
    if (number % 3 == 0 and number % 5 == 0):
      print('fizzbuzz')
    elif (number % 3 == 0):
      print('fizz')
    elif (number % 5 == 0):
      print('buzz')
    else:
      print(f'{number}\n')
    number += 1


fizzbuzz()