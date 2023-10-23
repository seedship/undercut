"""This class defines the logic behind the undercut game."""
import collections
import json
from typing import DefaultDict


class Game:
    """The game"""
    def __init__(self, num_players: int, num_options: int):
        """Constructs a game.

        Args:
            num_players: the number of players in this game.
            num_options: What options the players can choose.
        """
        print('Game Constructor')
        self._num_players = num_players
        self._num_options = num_options

        # Mapping from submission value to number of submissions
        self._submissions: DefaultDict[int, int] = collections.defaultdict(lambda: 0)
        self._submission_count: int = 0
        self._winning_number: int | None = None

    @property
    def num_players(self) -> int:
        return self._num_players

    @property
    def num_options(self) -> int:
        return self._num_options

    @property
    def finished(self) -> bool:
        return self._submission_count == self._num_players

    @property
    def winning_number(self) -> int:
        assert self.finished
        if self._winning_number is None:
            self._set_winning_number()
        return self._winning_number

    def _set_winning_number(self):
        assert self._winning_number is None
        for idx in reversed(range(2, self._num_options + 1)):
            if self._submissions[idx - 1] == 0:
                self._winning_number = idx
                return
        self._winning_number = 1

    def add_submission(self, submission: int):
        assert not self.finished
        assert submission <= self._num_options
        self._submission_count += 1
        self._submissions[submission] += 1

    def to_string(self) -> str:
        game_dict = {
            'num_players': self._num_players,
            'num_options': self._num_options,
            'finished': self.finished,
            'count': self._submission_count,
        }
        if self.finished:
            game_dict['submissions'] = self._submissions
            game_dict['winning_number'] = self.winning_number
        return json.dumps(game_dict)