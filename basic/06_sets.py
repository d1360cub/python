set = {"jhon", "doe", 27}  # si el set se define vacio, lo define como un diccionario

set.add("nuevo elemento")
print(set)  # un set no es una estructura ordenada

set.add("nuevo elemento")
print(set)  # un set no puede tener elementos repetidos

print("jhon" in set)
print("element" in set)  # false

# print(set[2]) # nose puede acceder porque esta almacenado de manera desordenada

set.remove("nuevo elemento")
print(set)

# set.clear()
print(len(set))

otro_set = {"nuevo", "set", "para", "unir"}

set_unido = set.union(otro_set)
print(set_unido)

print(set_unido.difference(set))
