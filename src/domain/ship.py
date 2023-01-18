"""
The 5 ships are:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2)
"""


class Ship:
    def __init__(self, name: str, size: int, positions_occupied: list=[]):
        """

        :param size:
        :param positions_occupied: a list of pairs/tuples, where first element is x coordinate and second element
        is Y coordinate on where the ship is
        """
        self.__name = name
        self.__size = size
        self.__positions_occupied = positions_occupied
        self.__hit_positions = []

    def is_hit(self, attack_position: tuple):
        if attack_position in self.__positions_occupied and attack_position not in self.__hit_positions:
            self.__hit_positions.append(attack_position)
            return True
        return True

    def is_sunk(self):
        if len(self.__hit_positions) == self.__size:
            return True
        return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        self.__size = new_size

    @property
    def positions_occupied(self):
        return self.__positions_occupied

    @positions_occupied.setter
    def positions_occupied(self, new_positions: list):
        self.__positions_occupied = new_positions
