from src.domain.fleet import Fleet
from src.data.constants import *

import texttable


class Field:
    def __init__(self, rows, columns, fleet: Fleet):
        """
        :param fleet: Fleet object which contains the ships that are supposed to be on the board
        visited_positions: list of already visited squares
        """
        self.__rows = rows
        self.__columns = columns
        self.__board = [[EMPTY_SPACE for _ in range(0, columns)] for _ in range(0, rows)]
        self.__fleet = fleet

    def __str__(self):
        text_board = texttable.Texttable()

        letters_header = ['-']
        for i in range(0, self.__columns):
            letters_header.append(chr(ord('A') + i))
        text_board.header(letters_header)

        for i in range(0, self.__rows):
            current_row = [i + 1] + self.__board[i]
            text_board.add_row(current_row)
        return text_board.draw()

    def place_ships(self, ships_and_their_locations: dict):
        for ship_name in ships_and_their_locations:
            ship_locations = ships_and_their_locations[ship_name]
            self.__fleet.assign_ship_positions(ship_name, ship_locations)
            for location in ship_locations:
                self.record_ship_position(ship_name, location)

    def check_if_ship_in_location(self, location_to_check: tuple):
        all_ship_locations = self.__fleet.get_all_ship_locations()
        if location_to_check in all_ship_locations:
            return True
        return False

    def get_position_status(self, position: tuple):
        return self.__board[ROWS_INDEX][COLUMNS_INDEX]

    def update_position_status(self, position: tuple, new_value):
        self.__board[position[HORIZONTAL_AXIS_INDEX]][position[VERTICAL_AXIS_INDEX]] = new_value

    def get_number_of_ships(self):
        return len(self.__fleet)

    def get_size(self):
        return self.__rows, self.__columns

    def record_ship_position(self, ship_name, position: tuple):
        ship_mark_location_symbol = SHIP_NAMES_AND_MARKS[ship_name]
        self.update_position_status(position, ship_mark_location_symbol)

    def check_if_ship_at_location_is_sunk(self, location_to_check: tuple):
        if not self.check_if_ship_in_location(location_to_check):
            return False
        ship_at_location = self.__fleet.get_ship_at_position(location_to_check)
        return ship_at_location.is_sunk()

    def update_board_with_sunk_ship(self, sunk_ship):
        ship_sunken_positions = sunk_ship.positions_occupied
        for position in ship_sunken_positions:
            self.update_position_status(position, SHIP_SUNK)

    def update_position_with_hit(self, hit_position: tuple):
        if not self.check_if_ship_in_location(hit_position):
            return False
        ship_at_hit_position = self.__fleet.get_ship_at_position(hit_position)
        # update ship
        ship_at_hit_position.is_hit(hit_position)
        # update board
        self.update_position_status(hit_position, SHIP_HIT)
        # check if the ship is now sunk and update the board if it is.
        if self.check_if_ship_at_location_is_sunk(hit_position):
            self.update_board_with_sunk_ship(self.__fleet.get_ship_at_position(hit_position))
