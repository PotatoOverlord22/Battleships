from unittest import TestCase
from src.domain.field import *


class TestField(TestCase):
    def setUp(self) -> None:
        fleet = Fleet()
        self.testing_field = Field(10, 10, fleet)

    def test_get_number_of_ships(self):
        pass

    def test_str(self):
        print(self.testing_field)
