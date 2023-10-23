
import random

import flask

from src.game_logic import game

app = flask.Flask(__name__)

# Options config -- config defining how the server will randomly generate the options a player can choose
MIN_OPTIONS = 3
MAX_OPTIONS = 10

# Num players config -- config defining how the server will randomly generate the number of players in a game
MIN_PLAYERS = 2
MAX_PLAYERS = 2

# Global variables. At some point get better with flask to not use these.
# Games. Dict of game_id to game object.
games: dict[int, game.Game] = {}
# Initialize game ID at 0 and increment each game
game_id = 0


def random_number(low: int, high: int) -> int:
    rand_range = high - low + 1
    return int(random.random() * rand_range) + low


def make_game() -> game.Game:
    num_options = random_number(MIN_OPTIONS, MAX_OPTIONS)
    num_players = random_number(MIN_PLAYERS, MAX_PLAYERS)
    return game.Game(num_players, num_options)


@app.route('/')
def get_active_game_id() -> str:
    return str(game_id)


@app.route('/get_game/<id>')
def get_game(id: str) -> str:
    id = int(id)
    if id not in games:
        flask.abort(404)
    return games[id].to_string()


@app.route('/submit_game/<id>')
def submit_game(id: str):
    id = int(id)
    if id not in games:
        flask.abort(404)
    args = flask.request.args
    submission = int(args['option'])
    games[id].add_submission(submission)
    if games[id].finished:
        # Start a new game when last one is finished
        global game_id
        game_id = id + 1
        games[game_id] = make_game()
    return 'Ack'


if __name__ == '__main__':
    games = {game_id: make_game()}
    app.run()
