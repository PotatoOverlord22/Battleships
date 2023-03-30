from src.domain.player import HumanPlayer, ComputerPlayer
from src.observer.subject import GameSubject
from src.data.constants import *
from src.data.observer_codes import *
from src.exceptions.errors import ConvertStringToCoordinatesError


class GameLogic(GameSubject):
    def __init__(self, player1: HumanPlayer, player2: ComputerPlayer):
        super().__init__()
        self.__human = player1
        self.__computer = player2
        self.__human_attack = True
        self.__is_won = False

    def determine_first_turn(self, does_human_start: bool):
        self.__human_attack = does_human_start

    def get_human_player_field(self):
        return self.__human.get_field()

    def get_computer_player_field(self):
        return self.__computer.get_field()

    def place_human_ships(self, ships_and_their_locations: dict):
        self.__human.place_ships(ships_and_their_locations)

    def place_computer_ships(self):
        self.__computer.place_ships()

    def is_human_turn(self):
        return self.__human_attack

    def update_game_state(self):
        pass

    def human_attack_guess(self, attack_coordinates):
        if self.__computer.check_if_got_hit(attack_coordinates):
            self.notify_observers(COMPUTER_GOT_HIT)
            self.__computer.update_own_hit(attack_coordinates)
            if self.__computer.check_if_ship_at_position_is_sunk(attack_coordinates):
                self.notify_observers(COMPUTER_SHIP_SUNK)
        else:
            self.notify_observers(HUMAN_MISSED)

    def computer_attack(self):
        computer_attack_position = self.__computer.create_random_position()
        if self.__human.check_if_got_hit(computer_attack_position):
            self.notify_observers(HUMAN_GOT_HIT)
            self.__human.update_own_hit(computer_attack_position)
            if self.__human.check_if_ship_at_position_is_sunk(computer_attack_position):
                self.notify_observers(HUMAN_SHIP_SUNK)
        else:
            self.notify_observers(COMPUTER_MISSED)

    def valid_player_ship_locations(self, ships_and_their_locations: dict):
        """

        :param ships_and_their_locations: should be a dictionary where the key is the name of the ship and
                                the value a list of coordinates which the ship occupies
        :return: True if the ship locations are valid on the field that is being played on
                False if the ship locations break the game rules
        """
        player_field = self.get_human_player_field()

        for ship_name in ships_and_their_locations:
            current_ship_coordinates: list = ships_and_their_locations[ship_name]
            for ship_coordinate in current_ship_coordinates:
                if not self.check_if_coordinate_in_field(player_field, ship_coordinate):
                    return False
            # get the size of the current ship from the program's data
            if not self.check_ship_coordinates_to_be_consecutive(SHIP_NAMES_AND_SIZE[ship_name],
                                                                 current_ship_coordinates):
                return False

        all_occupied_ship_locations = []
        for locations_of_a_ship in ships_and_their_locations.values():
            for location in locations_of_a_ship:
                all_occupied_ship_locations.append(location)
        if self.check_if_overlapping_ships_locations(all_occupied_ship_locations):
            return False
        return True

    @staticmethod
    def check_if_overlapping_ships_locations(ship_locations: list):
        """

        :param ship_locations: list of tuples, each tuple represents a location occupied by one of the ships
        :return: True -> if a location is occupied twice by ships
                False -> if all locations are occupied only once
        """
        for i in range(0, len(ship_locations) - 1):
            for j in range(i + 1, len(ship_locations)):
                if ship_locations[i][HORIZONTAL_AXIS_INDEX] == ship_locations[j][HORIZONTAL_AXIS_INDEX] and \
                        ship_locations[i][VERTICAL_AXIS_INDEX] == ship_locations[j][VERTICAL_AXIS_INDEX]:
                    return True
        return False

    @staticmethod
    def check_ship_coordinates_to_be_consecutive(ship_size, ship_locations: list):
        """
            A ship has consecutive locations if all its occupied locations are on the same axis (horizontal or vertical)
        and the distance between the head and the tail of the ship is equal to its size (biggest coordinate on opposite
        axis - smallest coordinate on opposite axis + 1 should be the size of the ship)
        :param ship_size: the size of the ship
        :param ship_locations: a list of tuples, each tuple representing the coordinates occupied by the ship
        :return: True
        """
        FIRST_LOCATION = 0
        HORIZONTAL_COORDINATE = 0
        VERTICAL_COORDINATE = 1
        # Check if the given locations are on the same vertical or horizontal axis
        horizontal_axis = ship_locations[FIRST_LOCATION][HORIZONTAL_COORDINATE]
        vertical_axis = ship_locations[FIRST_LOCATION][VERTICAL_COORDINATE]
        coordinates_on_same_horizontal_axis = 1
        coordinates_on_same_vertical_axis = 1

        biggest_horizontal_coordinate = ship_locations[FIRST_LOCATION][HORIZONTAL_COORDINATE]
        smallest_horizontal_coordinate = ship_locations[FIRST_LOCATION][HORIZONTAL_COORDINATE]

        biggest_vertical_coordinate = ship_locations[FIRST_LOCATION][VERTICAL_COORDINATE]
        smallest_vertical_coordinate = ship_locations[FIRST_LOCATION][VERTICAL_COORDINATE]

        for i in range(1, len(ship_locations)):
            current_horizontal_coordinate = ship_locations[i][HORIZONTAL_COORDINATE]
            current_vertical_coordinate = ship_locations[i][VERTICAL_COORDINATE]

            if current_vertical_coordinate > biggest_vertical_coordinate:
                biggest_vertical_coordinate = current_vertical_coordinate
            elif current_vertical_coordinate < smallest_vertical_coordinate:
                smallest_vertical_coordinate = current_vertical_coordinate
            if current_horizontal_coordinate > biggest_horizontal_coordinate:
                biggest_horizontal_coordinate = current_horizontal_coordinate
            elif current_horizontal_coordinate < smallest_horizontal_coordinate:
                smallest_horizontal_coordinate = current_horizontal_coordinate

            if current_horizontal_coordinate == horizontal_axis:
                coordinates_on_same_horizontal_axis += 1
            if current_vertical_coordinate == vertical_axis:
                coordinates_on_same_vertical_axis += 1

        if coordinates_on_same_horizontal_axis == ship_size:
            if biggest_vertical_coordinate - smallest_vertical_coordinate + 1 == ship_size:
                return True
        if coordinates_on_same_vertical_axis == ship_size:
            if biggest_horizontal_coordinate - smallest_horizontal_coordinate + 1 == ship_size:
                return True
        return False

    @staticmethod
    def check_if_coordinate_in_field(field, coordinate: tuple):
        field_size = field.get_size()

        if coordinate[HORIZONTAL_AXIS_INDEX] not in range(0, field_size[ROWS_INDEX]):
            return False
        if coordinate[VERTICAL_AXIS_INDEX] not in range(0, field_size[COLUMNS_INDEX]):
            return False
        return True

    def next_turn(self):
        self.__human_attack = not self.__human_attack
        self.update_game_state()

    def is_won(self):
        pass

    def ship_placement_phase(self):
        pass

    def attack_phase(self):
        if self.__human_attack:
            pass
        else:
            pass

        self.__human_attack = not self.__human_attack

    @staticmethod
    def convert_string_to_coordinates(coordinates_as_string: str):
        CHARACTER_INDEX = 0
        number_index = None
        for i in range(0, len(coordinates_as_string)):
            if coordinates_as_string[i].isnumeric():
                number_index = i
                break
        if number_index is None:
            raise ConvertStringToCoordinatesError("Incorrect coordinate format.")

        if len(coordinates_as_string) < 2:
            raise ConvertStringToCoordinatesError("Incorrect coordinate format.")
        if not coordinates_as_string[CHARACTER_INDEX].isalpha():
            raise ConvertStringToCoordinatesError("Incorrect coordinate format.")
        number_part = coordinates_as_string[number_index:]
        for number_as_character in number_part:
            if not number_as_character.isnumeric():
                raise ConvertStringToCoordinatesError("Incorrect coordinate format.")
        vertical_coordinate = ord(coordinates_as_string[CHARACTER_INDEX].upper()) - ord('A')
        horizontal_coordinate = int(number_part) - HEADER_VERTICAL_FIELD_DEVIATION
        return horizontal_coordinate, vertical_coordinate
