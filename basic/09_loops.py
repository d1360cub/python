count = 0

while count < 10:
    print(f"el valor de count es {count}, incremento de 1")
    count += 1

while count < 20:
    print(f"el valor de count es {count}, incremento de 2")
    count += 2
else:
    print("count es mayor a 20")

while count < 30:
    count += 2
    if count == 28:
        print("count es igual a 28 y sale con el break que está dentro del if")
        break
    print(f"el valor de count es {count}")

my_list = [35, 24, 62, 52, 30, 30, 17]
print("imprimiendo una lista")
for element in my_list:
    print(element)

my_tuple = (34, 1.77, "jhon", "doe", "jhon")
print("imprimiendo una tupla")
for element in my_tuple:
    print(element)

my_set = {"jhon", "doe", 27}
print("imprimiendo un set")
for element in my_set:
    print(element)

my_dict = {"lenguajes": {"python", "js", "c#"}, "pos_2": False, 1: 2.35}
print("imprimiendo un dict (imprime las keys)")
for element in my_dict:
    print(element)
print("imprimiendo un dict.values() para que imprima los valores")
for element in my_dict.values():
    print(element)
