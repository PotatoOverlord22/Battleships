from src.domain.field import Field
from src.domain.fleet import Fleet
from src.data.constants import *
from src.exceptions.errors import AttackError

import random
from abc import abstractmethod


class Player:
    @abstractmethod
    def place_ships(self, ships_and_their_locations):
        pass

    @abstractmethod
    def attack(self, enemy):
        pass

    @abstractmethod
    def check_if_got_hit(self, position):
        pass

    def update_own_hit(self, position_hit):
        pass

    @abstractmethod
    def get_field(self):
        pass


class HumanPlayer(Player):
    def __init__(self, field: Field, fleet: Fleet):
        self.__field = field
        self.__fleet = fleet

    def place_ships(self, ships_and_their_locations):
        self.__fleet.create_ships()
        self.__field.place_ships(ships_and_their_locations)

    def attack(self, enemy: Player):
        # Implemented in service for now
        pass

    def get_field(self):
        return self.__field

    def check_if_got_hit(self, position_being_attacked):
        return self.__field.check_if_ship_in_location(position_being_attacked)

    def update_own_hit(self, position_hit):
        self.__field.update_position_with_hit(position_hit)

    def check_if_ship_at_position_is_sunk(self, position_to_check):
        self.__field.check_if_ship_at_location_is_sunk(position_to_check)


class ComputerPlayer(Player):
    def __init__(self, field: Field, fleet: Fleet):
        self.__field = field
        self.__fleet = fleet

    def place_ships(self):
        self.__fleet.create_ships()
        ships_and_correct_random_positions = self.randomly_create_ship_locations()
        self.__field.place_ships(ships_and_correct_random_positions)

    def attack(self, enemy: HumanPlayer):
        # Implemented in service for now
        pass

    def get_field(self):
        return self.__field

    def update_own_hit(self, position_hit):
        self.__field.update_position_with_hit(position_hit)

    def check_if_got_hit(self, position_being_attacked):
        return self.__field.check_if_ship_in_location(position_being_attacked)

    def check_if_ship_at_position_is_sunk(self, position_to_check):
        self.__field.check_if_ship_at_location_is_sunk(position_to_check)

    def create_random_position(self):
        field_size = self.__field.get_size()
        vertical_coordinate = random.randint(0, field_size[ROWS_INDEX])
        horizontal_coordinate = random.randint(0, field_size[COLUMNS_INDEX])
        return vertical_coordinate, horizontal_coordinate

    def randomly_create_ship_locations(self):
        field_size = self.__field.get_size()
        ships_and_their_locations = {}
        available_positions = []
        for i in range(0, field_size[ROWS_INDEX]):
            for j in range(0, field_size[COLUMNS_INDEX]):
                available_positions.append((i, j))
        i = 0
        while i < NUMBER_OF_SHIPS:
            current_ship_name = list(SHIP_NAMES_AND_SIZE.keys())[i]
            current_ship_size = SHIP_NAMES_AND_SIZE[current_ship_name]
            ship_random_start_position = random.choice(available_positions)
            generated_possible_ship_positions = self.create_possible_ship_locations_from_a_position(
                ship_random_start_position, current_ship_size, available_positions)
            if generated_possible_ship_positions is None:
                continue
            for position in generated_possible_ship_positions:
                available_positions.remove(position)
            ships_and_their_locations[current_ship_name] = generated_possible_ship_positions
            i += 1
        return ships_and_their_locations

    @staticmethod
    def create_possible_ship_locations_from_a_position(start_position, ship_size, available_positions):
        # Generate up
        generated_ship_locations = [start_position]
        for i in range(1, ship_size):
            current_position = (start_position[HORIZONTAL_AXIS_INDEX], start_position[VERTICAL_AXIS_INDEX] + i)
            if current_position not in available_positions:
                break
            generated_ship_locations.append(current_position)
        generated_ship_locations = [start_position]
        if len(generated_ship_locations) == ship_size:
            return generated_ship_locations
        # Generate down
        generated_ship_locations = [start_position]
        for i in range(1, ship_size):
            current_position = (start_position[HORIZONTAL_AXIS_INDEX], start_position[VERTICAL_AXIS_INDEX] - i)
            if current_position not in available_positions:
                break
            generated_ship_locations.append(current_position)
        # Generate right
        generated_ship_locations = [start_position]
        for i in range(1, ship_size):
            current_position = (start_position[HORIZONTAL_AXIS_INDEX] + i, start_position[VERTICAL_AXIS_INDEX])
            if current_position not in available_positions:
                break
            generated_ship_locations.append(current_position)
        if len(generated_ship_locations) == ship_size:
            return generated_ship_locations
        # Generate left
        generated_ship_locations = [start_position]
        for i in range(1, ship_size):
            current_position = (start_position[HORIZONTAL_AXIS_INDEX] - i, start_position[VERTICAL_AXIS_INDEX])
            if current_position not in available_positions:
                break
            generated_ship_locations.append(current_position)
        if len(generated_ship_locations) == ship_size:
            return generated_ship_locations
