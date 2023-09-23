dictionary = {"name": "jhon", "lastname": "doe", "age": 28}
print(type(dictionary))
print(dictionary["name"])

other_dict = {"lenguajes": {"python", "js", "c#"}, "pos_2": False, 1: 2.35}
print(other_dict["lenguajes"])
print(type(other_dict["lenguajes"]))
print(other_dict[1])
print(type(other_dict["pos_2"]))

other_dict["pos_2"] = True
print(other_dict)

dictionary["nueva_key"] = "elemento nuevo"
print(dictionary)

del dictionary["nueva_key"]
print(dictionary)

print("jhon" in dictionary)  # false, porque busca en las keys
print("name" in dictionary)  # true

print(dictionary.items())  # lista con keys y values
print(dictionary.keys())  # lista con las keys
print(dictionary.values())  # lista con los values

copied_dict = dict.fromkeys(
    dictionary
)  # crea un nuevo diccionario con las keys del otro pero sin values
print(copied_dict)

copied_dict = dict.fromkeys(
    dictionary, "same value for all keys"
)  # crea un nuevo diccionario y le asigna el mismo value a todas las keys
print(copied_dict)

print(dictionary.values())
