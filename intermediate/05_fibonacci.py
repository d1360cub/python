def fibonacci():
  fibo = [0, 1]
  for element in range (1, 49):
    fibo.append(fibo[len(fibo) - 1] + fibo[len(fibo) - 2])
  for number in fibo:
    print(number)

fibonacci()