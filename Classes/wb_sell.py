from typing import List

# Base class SellProduct
class SellProduct:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price
# Derived classes for different products
class Shirt(SellProduct):
    def __init__(self, name: str, price: float, material: str, color: str) -> None:
        super().__init__(name, price)
        self.material = material
        self.color = color

class Shorts(SellProduct):
    def __init__(self, name: str, price: float, size: str, gender: str) -> None:
        super().__init__(name, price)
        self.size = size
        self.gender = gender


class Sneaker(SellProduct):
    def __init__(self, name: str, price: float, size: str, gender: str) -> None:
        super().__init__(name, price)
        self.size = size
        self.gender = gender


# Marketplace class
class Marketplace:

    data : List[SellProduct] = []

    def __init__(self, name: str) -> None:
        self.name = name

    def add_object(self, obj: SellProduct):
        self.data.append(obj)
        print(f'{obj.name} added to marketplace {self.name}')

    def remove_object(self, obj: SellProduct):
        self.data.remove(obj)
        print(f'{obj.name} removed from marketplace {self.name}')

    def get_objects(self) -> list:
        return self.data

# Testing the implementation
mp = Marketplace("Chernichki")

# Creating products
shirt = Shirt("Casual Shirt", 29.99, "Cotton", "Blue")
shorts = Shorts("Running Shorts", 19.99, "M", "Unisex")
sneaker = Sneaker("Sport Sneaker", 89.99, "42", "Men")

# Adding objects to marketplace
mp.add_object(shirt)
mp.add_object(shorts)
mp.add_object(sneaker)

# Getting all products in the marketplace
objects_for_sale = mp.get_objects()
for obj in objects_for_sale:
    print(f"{obj.name}, Price: {obj.price}")

# Removing an object
mp.remove_object(shorts)

# Displaying remaining products after removal
objects_for_sale_after_removal = mp.get_objects()
for obj in objects_for_sale_after_removal:
    print(f"{obj.name}, Price: {obj.price}")