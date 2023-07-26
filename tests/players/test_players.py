import pytest

from client.player import Player


@pytest.fixture
def first_name() -> str:
    return "lebron"


@pytest.fixture
def last_name() -> str:
    return "james"


@pytest.fixture
def is_active() -> bool:
    return True


def test_player(first_name, last_name, is_active):
    player = Player(first_name, last_name)
    assert player.first_name, first_name
    assert player.last_name, last_name
    assert player.full_name, f"{first_name} {last_name}"
    assert player.is_active, is_active

