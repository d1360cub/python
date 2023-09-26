# lambdas = anonymous functions

sum = lambda first_value, second_value: first_value + second_value

print(sum(5, 3))

def sum_three_values(third_value):
  return lambda first_value, second_value: first_value + second_value + third_value

print(sum_three_values(5)(2,4))