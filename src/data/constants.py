"""
        Important constants used throughout the game

    - header deviation (if we had a header on 2rows the constant would be changed to 2, this affects how coordinates are calculated)
    - SHIP SIZES AND NAMES! (in theory if you change these, all the names of the ships and their size throughout the game
                    should change)
    - number of ships (this should change the ship placement phase to include and ask for more ships)

"""
HORIZONTAL_AXIS_INDEX = 0
VERTICAL_AXIS_INDEX = 1
ROWS_INDEX = 0
COLUMNS_INDEX = 1
HEADER_VERTICAL_FIELD_DEVIATION = 1

EMPTY_SPACE = '_'
TRIED_LOCATION = -1
SHIP_HIT = 1
SHIP_SUNK = 2

NUMBER_OF_DESTROYERS = 1
SIZE_OF_DESTROYER = 2
NUMBER_OF_SUBMARINES = 1
SIZE_OF_SUBMARINE = 3
NUMBER_OF_CRUISERS = 1
SIZE_OF_CRUISER = 3
NUMBER_OF_BATTLESHIPS = 1
SIZE_OF_BATTLESHIP = 4
NUMBER_OF_CARRIERS = 1
SIZE_OF_CARRIER = 5
DEFAULT_BOARD_SIZE = 10

DESTROYER_MARK = 'D'
SUBMARINE_MARK = 'S'
CRUISER_MARK = 'CR'
BATTLESHIP_MARK = 'B'
CARRIER_MARK = 'CA'

NUMBER_OF_SHIPS = NUMBER_OF_DESTROYERS + NUMBER_OF_SUBMARINES + NUMBER_OF_CRUISERS + NUMBER_OF_BATTLESHIPS + NUMBER_OF_CARRIERS
SHIP_NAMES_AND_SIZE = {'destroyer': SIZE_OF_DESTROYER,
                       'submarine': SIZE_OF_SUBMARINE,
                       'cruiser': SIZE_OF_CRUISER,
                       'battleship': SIZE_OF_BATTLESHIP,
                       'carrier': SIZE_OF_CARRIER}

SHIP_NAMES_AND_MARKS = {'destroyer': DESTROYER_MARK,
                        'submarine': SUBMARINE_MARK,
                        'cruiser': CRUISER_MARK,
                        'battleship': BATTLESHIP_MARK,
                        'carrier': CARRIER_MARK}
