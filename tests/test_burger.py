from bun import Bun
from ingredient import Ingredient
from burger import Burger
from unittest.mock import Mock
from unittest.mock import patch


class TestBurger:
    @patch('bun.Bun.get_price', return_value=200)
    def test_get_price_only_bun(self, mock_bun_get_price):
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 100
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.get_price() == 200

    @patch('ingredient.Ingredient.get_price', return_value=100)
    @patch('bun.Bun.get_price', return_value=200)
    def test_get_price_only_ingredient(self, mock_ing_get_price, mock_bun_get_price):
        mock_ing = Mock(spec=Ingredient)
        mock_ing.get_price.return_value = 100

        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 0

        burger = Burger()
        burger.set_buns(mock_bun)

        burger.add_ingredient(mock_ing)
        assert burger.get_price() == 100

    @patch('ingredient.Ingredient.get_price', return_value=100)
    @patch('bun.Bun.get_price', return_value=200)
    @patch('ingredient.Ingredient.get_name', return_value="name_ing")
    @patch('bun.Bun.get_name', return_value="name_bun")
    @patch('ingredient.Ingredient.get_type', return_value="type_ing")
    def test_get_receipt(self, mock_ing_get_price, mock_bun_get_price, mock_ing_get_name, mock_bun_get_name, mock_ing_get_type):
        mock_bun = Mock(spec=Bun)
        mock_ing = Mock(spec=Ingredient)

        mock_ing.get_price.return_value = 100
        mock_ing.get_name.return_value = "name_ing"
        mock_ing.get_type.return_value = "type_ing"

        mock_bun.get_price.return_value = 100
        mock_bun.get_name.return_value = "name_bun"


        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing)

        assert str(burger.get_receipt()) == ('(==== name_bun ====)\n'
 '= type_ing name_ing =\n'
 '(==== name_bun ====)\n'
 '\n'
 'Price: 300')