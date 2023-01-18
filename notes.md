# **IMPORTANT NOTES**

### Battleships follow the OBSERVER design pattern, where all battleships (subjects) notify the UI (subscriber) their state:

        1. OK
        2. Attacked
        3. Destroyed

## Object analysis

**Objects metioned are:**

**Game, Field, Square, Column, Row, Player, Fleet, Ship, Aircraft carrier, Destroyer, Cruiser, Submarine, Battleship, Size, Shape, Turn, Location, Opponent, Hit, Miss, Winner, Copy**

**Relationships are:**

    Game HASA setof Player
    
    Player HASA Field
    
    Player HASA Fleet
    
    Game HASA Turn
    
    Game HASA Winner
    
    Field HASA setof Square
    
    PlayersField ISA Field
    
    OpponentsField ISA Field
    
    Fleet HASA setof Ship
    
    Carrier ISA Ship
    
    Battleship ISA Ship
    
    Cruiser ISA Ship
    
    Destroyer ISA Ship
    
    Submarine ISA Ship
    
    Ship HASA Location
    
    Location HAS Row
    
    Location HAS Column
    
    Square HASA Location
    
    Square HASA Ship
    
    Square HASA Trial
    
    Hit ISA Trial
    
    Miss ISA Trial

## Reworking this gives:

## Game

    Player one
    Player two
    int winner
    int turn
## Player

    Field field
    Fleet fleet
## Field

    Square[][] squares
## Fleet

    Ship[] ships
## Ship

    int size
    String name
    Location[size] location
## Location

    int row
    int column
## Square

    Location location
    Ship ship
    int hitOrMiss


# Operation Analysis

## Operations mentioned are:

    (the game is) Played
    
    (each player) Places
    
    (ships may not) Overlap
    
    (first turn is ) Determined
    
    (players) Take turns
    
    (players) Guess
    
    (player) Declares
    
    (ship is) Occupying
    
    (all squres for a ship are) Guessed
    
    (players) Announce
    
    (player) Keeps track of
    
    (first player) Sink

# Reworked this is:

## Game

    void play()
    Player determineFirstTurn()
## Player

    void placeShips(Field)
    Location makeGuess()
    void sendGuess(Location)
    Location receiveGuess()
    void record(Location)
    String announceSunk(Ship)
    String announceHitOrMiss(Location)
## Field

    boolean isHitOrMiss(Location)
    Ship isSunk(Location)
    void record(Location)
## Ship

    boolean overlaps(Ship)
    boolean occupies(Location)
    boolean isSunk()