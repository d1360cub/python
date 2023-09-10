lista = ["jhon", "doe", 28, 1.75]

print(f"name {lista[0]} {lista[1]} high {lista[3]} age {lista[2]}")

# destructurando una lista
name, lastname, age, high = lista
print(age)

# concatenar una lista
print([1, 2, 5] + lista)

# añadir un elemento al final
lista.append("elementoalfinal")
print(lista)

# añadir un elemento en un posicion especifica
lista.insert(2, "elemento insertado en pos 2")
print(lista)

# eliminar un elemento conocido en específico
lista.remove("elemento insertado en pos 2")
print(lista)
# si hay elementos duplicados, elimina el primero que encuentra

# eliminar el último elemento y lo almacena
print(lista.pop())
print(lista)
# elimina elemento en la posicion indicada y lo almacena
print(lista.pop(2))
print(lista)

# elimina elemento en la posicion indicada pero no lo almacena
del lista[2]
print(lista)

# copiar una lista
lista_copiada = lista.copy()
print(lista_copiada)

# darle la vuelta a la lista
lista_copiada.reverse()
print(lista_copiada)

# ordena de manera ascendente
lista.sort()
print(lista)

# resetear una lista
lista.clear()
print(lista)
