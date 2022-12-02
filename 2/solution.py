import argparse
import sys

POINTS_WIN_ = 6
POINTS_DRAW_ = 3

ROCK_1 = 'A'
ROCK_2 = 'X'
OPTION_LOSE = 'X'

PAPER_1 = 'B' 
PAPER_2 = 'Y' 
OPTION_DRAW = 'Y' 

SCISSORS_1 = 'C'
SCISSORS_2 = 'Z'
OPTION_WIN = 'Z'

def get_hand_score(inPlayerHand : str) -> int:
    _mapping = {
        ROCK_1: 1,
        ROCK_2: 1,

        PAPER_1 : 2,
        PAPER_2 : 2,

        SCISSORS_1 : 3,
        SCISSORS_2 : 3
    }
    return _mapping[inPlayerHand]

def get_match_score(inPlayer1Hand : str, inPlayer2Hand: str) -> tuple[int, int]:
    _player1WinsPermuatsions = [[ROCK_1, SCISSORS_2], [PAPER_1, ROCK_2], [SCISSORS_1, PAPER_2]]

    if _player1WinsPermuatsions.count([inPlayer1Hand, inPlayer2Hand]):
        return [POINTS_WIN_, 0]
    return[0, POINTS_WIN_]

def play_game(inPlayer1Hand : str, inPlayer2Hand: str) -> tuple[int, int]:
    _player1Score = get_hand_score(inPlayer1Hand)
    _player2Score = get_hand_score(inPlayer2Hand)
    if _player1Score == _player2Score:
        return [_player1Score + POINTS_DRAW_, _player2Score + POINTS_DRAW_]
    
    _matchScore = get_match_score(inPlayer1Hand, inPlayer2Hand)
    return [_player1Score + _matchScore[0], _player2Score + _matchScore[1]]

def get_hand_to_play(inPlayer1Hand: str, inHowItEnds : str):
    _winMap = {
        ROCK_1: PAPER_2,
        PAPER_1 : SCISSORS_2,
        SCISSORS_1 : ROCK_2
    }
    _loseMap = {
        ROCK_1: SCISSORS_2,
        PAPER_1 : ROCK_2,
        SCISSORS_1 : PAPER_2
    }

    if inHowItEnds == OPTION_WIN :
        return _winMap[inPlayer1Hand]
    return _loseMap[inPlayer1Hand]

def play_game_2(inPlayer1Hand : str, inHowItEnds: str) -> tuple[int, int]:
    _player2Hand = ''
    if inHowItEnds == OPTION_DRAW:
        _player2Hand = inPlayer1Hand
    else:
        _player2Hand = get_hand_to_play(inPlayer1Hand, inHowItEnds)

    _player1Score = get_hand_score(inPlayer1Hand)
    _player2Score = get_hand_score(_player2Hand)
    if _player1Score == _player2Score:
        return [_player1Score + POINTS_DRAW_, _player2Score + POINTS_DRAW_]
    
    _matchScore = get_match_score(inPlayer1Hand, _player2Hand)
    return [_player1Score + _matchScore[0], _player2Score + _matchScore[1]]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    _player1Score = 0
    _player2Score = 0
    with open(args.filename) as f:
        for _line in f:
            _line = _line.rstrip()
            _split = _line.split(' ')
            # _result = play_game(_split[0], _split[1])
            _result = play_game_2(_split[0], _split[1])
            _player1Score += _result[0]
            _player2Score += _result[1]

    print(f"Result: {_player1Score} - {_player2Score}")

    sys.exit(0)

