from database import Database
from bun import Bun
from ingredient import Ingredient


class TestDataBase:
    def test_available_buns(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_available_ingredients(self):
        database = Database()
        assert len(database.available_ingredients()) == 6
