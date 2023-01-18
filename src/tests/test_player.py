from unittest import TestCase
from src.domain.player import *


class TestComputerPlayer(TestCase):
    def setUp(self) -> None:
        self.__fleet = Fleet()
        self.__field: Field = Field(10, 10, self.__fleet)
        self.__player = ComputerPlayer(self.__field, self.__fleet)

    def test_randomly_create_ship_locations(self):
        print(self.__player.randomly_create_ship_locations())
