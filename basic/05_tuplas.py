tupla = (34, 1.77, "jhon", "doe", "jhon")
lista = [34, 1.77, "doe", "jhon"]

print(type(tupla))
print(type(lista))
print(tupla[0])
print(tupla[-1])
print(tupla.count("jhon"))
print(tupla.index("jhon"))
print(lista.index("jhon"))

# No se puede escribir un elemento de una tupla
# tupla[1] = 1.85
print(tupla)

# concatenando una tupla
otra_tupla = ("una", "tupla", "nueva")
tupla_concatenada = tupla + otra_tupla
print(tupla_concatenada)

# slice de una tupla
print(tupla_concatenada[3:6])
