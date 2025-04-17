import random


class Ship:
    def __init__(self, size):
        pass

    def place(self, positions):
        pass

    def hit(self) -> bool:
        pass

    def is_sunk(self):
        pass


class Battleship(Ship):
    def __init__(self):
        pass

class Cruiser(Ship):
    def __init__(self):
        pass

class Destroyer(Ship):
    def __init__(self):
        pass

class Submarine(Ship):
    def __init__(self):
        pass


class Board:
    def __init__(self, size=10):
        pass

    def is_valid_position(self, positions):
        pass

    def place_ship(self, ship, start_row, start_col, horizontal=True):
        pass

    def receive_shot(self, row, col):
        pass

    def display(self):
        pass

    def display_hidden(self):
        pass

    def all_ships_sunk(self):
        pass


def place_ships_on_board(ships, board):
    pass


