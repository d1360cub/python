def add_one(value):
  return value + 1

def add_four(value):
  return value + 4

def add_two_values_plus_one(first_value, second_value):
  return first_value + second_value + 1

def add_two_values_plus_one_using_function(first_value, second_value):
  return add_one(first_value + second_value)

print(add_two_values_plus_one(2, 3))
print(add_two_values_plus_one_using_function(2, 3))

def add_two_values_and_another_value(first_value, second_value, f_sum):
  return f_sum(first_value + second_value)

print(add_two_values_and_another_value(2, 3, add_one))
print(add_two_values_and_another_value(2, 3, add_four))

# Closures

def add_ten():
  def add(value):
    return value + 10
  return add

add_closure = add_ten()
print(add_closure(3))
print(add_ten()(3))

# Built-in Higher Order Functions

numbers = [2, 5, 10, 21]

def multiply_by_two(number):
  return number *2

# map

print(list(map(multiply_by_two, numbers)))
print(list(map(lambda number: number + 3, numbers)))

# filter

print(list(filter(lambda number: number % 2 == 0, numbers)))

# reduce

from functools import reduce

print(reduce(lambda acc, curr: acc + curr, numbers))
