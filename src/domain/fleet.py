from src.domain.ship import *
from src.data.constants import *


class Fleet:
    def __init__(self):
        self.__ships = []

    def __len__(self):
        return len(self.__ships)

    def create_ships(self):
        """
        The 5 ships are:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2)
        """
        for ship_name in SHIP_NAMES_AND_SIZE:
            ship_size = SHIP_NAMES_AND_SIZE[ship_name]
            new_ship = Ship(ship_name, ship_size)
            self.__ships.append(new_ship)

    def get_ship_by_name(self, ship_name_to_search):
        for ship in self.__ships:
            if ship.name == ship_name_to_search:
                return ship

    def assign_ship_positions(self, ship_to_assign_position_name, positions_to_assign: list):
        for ship in self.__ships:
            if ship.name == ship_to_assign_position_name:
                ship.positions_occupied = positions_to_assign
                return

    def get_ships(self):
        return self.__ships

    def get_ship_at_position(self, position_to_check: tuple) -> Ship:
        for ship in self.__ships:
            if position_to_check in ship.positions_occupied:
                return ship

    def get_all_ship_locations(self) -> list:
        ship_locations = []
        for ship in self.__ships:
            for position in ship.positions_occupied:
                ship_locations.append(position)
        return ship_locations
