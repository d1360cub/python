cond1 = False

if cond1:
    print("el valor de la condicion es True")
else:
    print("el valor de la condicion es False")

cond1 = 5 * 2

if cond1:
    print(f"el valor de la condicion es {cond1}")
else:
    print("el valor de cond es diferente")

if cond1 > 10:
    print("cond es mayor a 10")
elif cond1 < 10:
    print("cond es menor a 10")
else:
    print("cond es igual a 10")


my_string = ""

if my_string == "cadena de texto":
    print("las cadenas de texto son iguales")

if not my_string:
    print("la cadena de texto está vacía")
