import pytest
from bun import Bun


class TestBun:
    def test_get_name(self):
        bun = Bun("name", 123)
        assert "name" == bun.get_name()

    def test_get_price(self):
        bun = Bun("name", 123)
        assert 123 == bun.get_price()
