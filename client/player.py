from nba_api.stats.static import players

from models.player_model import PlayerModel


class Player:
    _data = None

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def _info(self) -> PlayerModel:
        if self._data is None:
            self._data = self._get_player_by_name(self.first_name, self.last_name)
        return self._data

    @property
    def is_active(self) -> bool:
        return self._info.is_active

    @property
    def full_name(self) -> str:
        return self._info.full_name

    @classmethod
    def _get_player_by_name(cls, first_name: str, last_name: str):
        players_found = players.find_players_by_full_name(f'{first_name} {last_name}')
        assert players_found, f"No player found: {first_name} {last_name}"
        assert len(
            players_found) == 1, f"More players found for {first_name} {last_name}: {', '.join([p['full_name'] for p in players_found])}"
        return PlayerModel(**players_found[0])


