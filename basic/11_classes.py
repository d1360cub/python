class Person:
    def __init__(self, name, lastname) -> None:
        self.name = name
        self.lastname = lastname

    def walk(self):
        print(f"{self.name} {self.lastname} está caminando")


my_person = Person("jhon", "doe")
print(f"{my_person.name} {my_person.lastname}")
my_person.walk()
