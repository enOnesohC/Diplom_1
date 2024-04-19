from ingredient import Ingredient


class TestIngredient:
    def test_ing_get_name(self):
        ing = Ingredient("type", "name", 123)
        assert ing.get_name() == "name"

    def test_ing_get_type(self):
        ing = Ingredient("type", "name", 123)
        assert ing.get_type() == "type"

    def test_ing_get_price(self):
        ing = Ingredient("type", "name", 123)

        assert ing.get_price() == 123
