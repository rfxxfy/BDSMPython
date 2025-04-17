from typing import List

class StringValue:
    def __init__(self, min_length: int, max_length: int):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name: str):
        self.public_name = name
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            return
        length = len(value)
        if length < self.min_length or length > self.max_length:
            return
        instance.__dict__[self.private_name] = value


class PriceValue:
    def __init__(self, max_value: float):
        self.max_value = max_value

    def __set_name__(self, owner, name: str):
        self.public_name = name
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            return
        if value < 0 or value > self.max_value:
            return
        instance.__dict__[self.private_name] = value


class Car:
    name = StringValue(min_length=2, max_length=50)
    price = PriceValue(max_value=1_000_000)

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Car(name={self.name!r}, price={self.price!r})"


class AutoSalon:
    name = StringValue(min_length=3, max_length=100)
    cars: List[Car] = []

    def __init__(self, name: str):
        self.name = name

    def add_car(self, car: Car):
        self.cars.append(car)

    def remove_car(self, car: Car):
        self.cars.remove(car)
