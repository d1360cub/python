def my_function():
    print("esto es una funcion")


def add_two_values(first_number, second_number):
    return first_number + second_number


def greeting(name, lastname):
    print(f"hola {name} {lastname}")


def print_name_with_alias(name, lastname, alias="no a.k.a"):
    print(name, lastname, alias)


def print_text(*texts):
    for text in texts:
        print(text)
