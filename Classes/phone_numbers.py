import random
from typing import List


class Abonent:
    def __init__(self, name: str, phone_number: str, price: float = 100) -> None:
        self.name = name
        self.phone_number = phone_number
        self.price = price

    def show_number(self) -> None:
        print(f'Number of the abonent {self.phone_number}')

    def add_to_group(self, group_name: str) -> None:
        match group_name:
            case 'usual':
                self.__class__ = UsualAbonent
            case 'student':
                self.price *= 0.5
                self.__class__ = StudentContact
            case 'commercial':
                self.price *= 5.0
                self.__class__ = CommercialAbonent
        print(f'{self.name} added to group {group_name}.')


class UsualAbonent(Abonent):
    def __init__(self, name: str, phone_number: str, price: float) -> None:
        super().__init__(name, phone_number, price * 1.0)


class StudentContact(Abonent):
    def __init__(self, name: str, phone_number: str, price: float) -> None:
        super().__init__(name, phone_number, price * 0.5)


class CommercialAbonent(Abonent):
    def __init__(self, name: str, phone_number: str, price: float) -> None:
        super().__init__(name, phone_number, price * 5.0)


class AbonentGenerator:
    def __init__(self) -> None:
        self.existing_numbers = []
        self.price = 100

    def generate_unique_phone_number(self) -> str:
        number = random.randint(79000000000, 79999999999)
        return f'+{number}'

    def create_contact(self, name: str, contact_type: str) -> object:
        number = self.generate_unique_phone_number()
        self.existing_numbers.append(number)
        match contact_type:
            case 'usual':
                return UsualAbonent(name, number, self.price)
            case 'student':
                return StudentContact(name, number, self.price)
            case 'commercial':
                return CommercialAbonent(name, number, self.price)

    def get_existing_numbers(self) -> List[str]:
        return self.existing_numbers


generator = AbonentGenerator()

contact1 = generator.create_contact("Alice", 'usual')
contact2 = generator.create_contact("Sasha", 'student')
contact4 = generator.create_contact("Alina", 'student')
# Using the methods
contact1.show_number()
contact1.add_to_group("student")

contact3 = generator.create_contact("Jenya", 'commercial')
contact3.show_number()

print(generator.get_existing_numbers())
