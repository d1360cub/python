def is_prime():
  for element in range (1, 101):
    if element >= 2:
      not_prime = False
      for index in range(2, element):
        if element % index == 0:
          not_prime = True
          break

      if not not_prime:
        print(element)


is_prime()