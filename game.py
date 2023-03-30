from src.services.game_services import GameLogic
from src.domain.player import HumanPlayer, ComputerPlayer
from src.domain.field import Field
from src.domain.fleet import Fleet
from src.ui.console_ui import ConsoleUI
from src.observer.observer import UIObserver
from src.data.constants import DEFAULT_BOARD_SIZE


class BattleshipsGame:
    @staticmethod
    def play():
        ROWS_INDEX = 0
        COLUMNS_INDEX = 1

        human_fleet = Fleet()
        computer_fleet = Fleet()

        human_field = Field(DEFAULT_BOARD_SIZE, DEFAULT_BOARD_SIZE, human_fleet)
        computer_field = Field(DEFAULT_BOARD_SIZE, DEFAULT_BOARD_SIZE, computer_fleet)

        human = HumanPlayer(human_field, human_fleet)
        computer = ComputerPlayer(computer_field, computer_fleet)

        game = GameLogic(human, computer)

        ui = ConsoleUI(game)
        ui_observer = UIObserver(ui)
        game.attach_observer(ui_observer)

        # board_size = ui.custom_user_board_size()
        # if board_size is None:
        #     return


        # Ship placement phase
        ui.display_field(human_field)

        while True:
            ship_locations = ui.ask_player_for_ship_locations()
            if ship_locations is None:
                continue
            if game.valid_player_ship_locations(ship_locations):
                game.place_human_ships(ship_locations)
                break
            else:
                ui.display_invalid_locations_message()
        ui.display_field(human_field)
        game.place_computer_ships()
        # Attack phase (main loop of the game)
        game.determine_first_turn(ui.ask_user_if_player1_starts_first())
        while not game.is_won():
            if game.is_human_turn():
                attack_coordinates = ui.ask_user_for_attack_guess()
                if attack_coordinates is None:
                    continue
                game.human_attack_guess(attack_coordinates)
            else:
                ui.display_computer_attack_message()
                game.computer_attack()
            game.next_turn()


if __name__ == "__main__":
    battleships = BattleshipsGame()
    battleships.play()
