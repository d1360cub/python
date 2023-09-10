salto_de_linea = "salto de linea\ndebe ser todo pegado para que\nno ponga espacios"
print(salto_de_linea)

tabulacion = "\ttexto con tabulacion"
print(tabulacion)

name, lastname, age = "jhon", "doe", 35

# dandole formato a las variables al imprimir en pantalla
# %s es para formatear a string y %d a entero

print("his name is %s %s and he is %s" % (name, lastname, age))
print(type(age))  # age sigue siendo entero porque formateamos fue en pantalla
print("his name is {} {} and he is {}".format(name, lastname, age))

print(f"his name is {name} {lastname} and he is {age}".format(name, lastname, age))

# desempaquetar caracteres
ejemplo = "12345"
a, b, c, d, e = ejemplo
print(a, c)

# slice de una cadena
print(ejemplo[2])  # 3
print(ejemplo[2:4])  # 34
print(ejemplo[2:])  # 345

# reverse
print(ejemplo[::-1])  # 54321

# funciones
print("capitalizar".capitalize())
print("capitalizar".upper())
print("capitalizar".count("a"))
print(ejemplo.isnumeric())
print("capitalizar".capitalize().isupper())
