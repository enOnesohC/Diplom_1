import pytest
from bun import Bun


class TestBun:
    def test_add_bun(self):
        bun = Bun("name", 123)
        assert "name" == bun.get_name()
        assert 123 == bun.get_price()

    def test_get_name(self):
        bun = Bun("name", 123)
        assert "name" == bun.get_name()

    def test_get_price(self):
        bun = Bun("name", 123)
        assert 123 == bun.get_price()

    def test_bun_name_as_number(self):
        with pytest.raises(ValueError):
            bun = Bun(123, 123)

    def test_bun_price_as_str(self):
        with pytest.raises(ValueError):
            bun = Bun("name", "123")

    def test_bun_none_name(self):
        with pytest.raises(ValueError):
            bun = Bun(None, 123)

    def test_bun_none_price(self):
        with pytest.raises(ValueError):
            bun = Bun("name", None)
