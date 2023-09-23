my_number = 5.3
my_other_number = "a"

try:
    print(my_number + my_other_number)
    print("sale por el primer try")
except:
    print("sale por el except del primer try/except")

try:
    print(my_number + my_other_number)
    print("sale por el segundo try")
except:
    print("sale por el except del segundo try/except")
else:
    print("solo se imprime si el resultado del try fue exitoso")

try:
    print(my_number + my_other_number)
    print("sale por el tercer try")
except:
    print("sale por el except del tercer try/except")
else:
    print("solo se imprime si el resultado del try fue exitoso")
finally:
    print("siempre se imprime este finally")

try:
    print(my_number + my_other_number)
    print("sale por el try")
except TypeError:
    print("solo captura errores del tipo TypeError")

try:
    print(my_number + my_other_number)
    print("sale por el try")
except TypeError as errorcito:
    print(errorcito)
    print("sale por la excepcion TypeError")

print("continua la ejecucion")

try:
    print(my_number + my_other_number)
    print("sale por el try")
except ValueError as errorcito:
    print(errorcito)
    print("sale por la excepcion ValueError")
except Exception as excepcion:
    print(excepcion)
    print(
        "sale por cualquier excepcion diferente a la definida anteriormente que fue ValueError"
    )
