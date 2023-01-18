from src.data.constants import *
from src.exceptions.errors import ConvertStringToCoordinatesError
from src.data.observer_codes import *


class ConsoleUI:
    def __init__(self):
        pass

    @staticmethod
    def display_start_message():
        print("Welcome!")
        print("1. Start game")
        print("0. Exit")

    @staticmethod
    def display_observer_message(code):
        if code == HUMAN_MISSED:
            print("You missed!")
        elif code == HUMAN_GOT_HIT:
            print("You got hit!")
        elif code == HUMAN_SHIP_SUNK:
            print("Your ship has sunk!")
        elif code == COMPUTER_MISSED:
            print("Computer missed!")
        elif code == COMPUTER_GOT_HIT:
            print("Computer got hit!")
        elif code == COMPUTER_SHIP_SUNK:
            print("Computer ship has sunk!")
        else:
            print(code)

    @staticmethod
    def read_user_input():
        return input("input > ")

    def ask_user_for_attack_guess(self):
        print("Your turn to strike! Try and attack an enemy position!")
        user_string_coordinates = self.read_user_input()
        try:
            user_correct_coordinates = self.convert_string_to_coordinates(user_string_coordinates)
        except ConvertStringToCoordinatesError as ConvertError:
            print(ConvertError)
            return
        return user_correct_coordinates

    def custom_user_board_size(self):
        print("board rows: ")
        board_rows = self.read_user_input()
        print("board columns: ")
        board_columns = self.read_user_input()
        try:
            board_rows = int(board_rows)
            board_columns = int(board_columns)
        except ValueError:
            print("Board rows and columns must be integers")
            return

        return board_rows, board_columns

    def ask_user_if_player1_starts_first(self):
        print("who starts the game?")
        print("1. Human")
        print("2. Computer")
        HUMAN = '1'
        COMPUTER = '2'
        user_option = self.read_user_input()
        if user_option == HUMAN:
            return True
        if user_option == COMPUTER:
            return False
        print("Unknown option.")

    def display_invalid_locations_message(self):
        print("Ships do not have valid locations. Ship locations might overlap or are outside the field.")

    @staticmethod
    def convert_string_to_coordinates(coordinates_as_string: str):
        CHARACTER_INDEX = 0
        number_index = None
        for i in range(0, len(coordinates_as_string)):
            if coordinates_as_string[i].isnumeric():
                number_index = i
                break
        if number_index == None:
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

    def ask_user_for_specific_ship_location(self, ship_name, ship_size):
        print(f'place {ship_name} (size is {ship_size} consecutive squares): ')
        user_raw_coordinates = self.read_user_input().strip(" ")
        if len(user_raw_coordinates.split(" ")) != ship_size:
            print("Incorrect number of coordinates!")
            return
        converted_coordinates = []
        for coordinates in user_raw_coordinates.split(" "):
            try:
                correct_coordinate = self.convert_string_to_coordinates(coordinates)
            except ConvertStringToCoordinatesError as ConvertError:
                print(ConvertError)
                return
            converted_coordinates.append(correct_coordinate)
        return converted_coordinates

    def ask_player_for_ship_locations(self):
        """

        :return: a dictionary with each ship name and their assigned coordinates by the user, for further calculation
        this only transforms the coordinates given by the user to usable coordinates, it does not check for game rules,
        it does not check if a ship is overlapping another ship, or if it is in the field, such checks are done
        in game-logic layer.
        e.g:
            On a ship with size 3:
            user input: A1 A2 A3  --> [(0,0), (0,1), (0,2)]
            user input: A1 AA A6 --> "Incorrect coordinate format"
            user input : A1 A2  --> "Incorrect number of coordinates"

        """
        print("Place your ships!")
        print("Coordinate format should be: LETTER_OF_COLUMN NUMBER_OF_ROW\n"
              "for a cruiser example: A4 A5 A6")
        ship_and_player_given_coordinates = {}
        for current_ship_name in SHIP_NAMES_AND_SIZE:
            current_ship_coordinates = self.ask_user_for_specific_ship_location(current_ship_name,
                                                                                SHIP_NAMES_AND_SIZE[current_ship_name])
            if current_ship_coordinates is None:
                return
            ship_and_player_given_coordinates[current_ship_name] = current_ship_coordinates
        return ship_and_player_given_coordinates

    @staticmethod
    def display_computer_attack_message():
        print("Computer's turn!")

    @staticmethod
    def display_field(field_to_display):
        print(field_to_display)
