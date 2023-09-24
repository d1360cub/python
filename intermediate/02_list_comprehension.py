my_list = [35, 24, 62, 52, 30, 30, 17]

copied_list = [i for i in my_list]

print(copied_list)

my_range_list = [i for i in range(6)]

print(my_range_list)  # [0, 1, 2, 3, 4, 5]

added_list = [i + 2 for i in range(7)]
print(added_list)  # [2, 3, 4, 5, 6, 7, 8]
