def my_function():
    print("esto es una funcion")


my_function()


def add_two_values(first_number, second_number):
    return first_number + second_number


print(add_two_values(3, 5.5))


def greeting(name, lastname):
    print(f"hola {name} {lastname}")


greeting("jhon", "doe")
greeting(lastname="doe", name="jane")


def print_name_with_alias(name, lastname, alias="no a.k.a"):
    print(name, lastname, alias)


print_name_with_alias("jhon", "doe", "big dog")
print_name_with_alias("jane", "doe")


def print_text(*text):
    print(text)


print_text("imprimiendo", "un", "texto", "infinito")


def print_text(*texts):
    for text in texts:
        print(text)


print_text("imprimiendo", "un", "texto", "infinito")
