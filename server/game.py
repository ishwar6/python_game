

class Game(object):
    def __init__(self, id, players) -> None:
        self.id = id
        self.players = players
        self.words_used  = []


    def player_guess(self, player, guess):
        pass

    def player_disconnected(self, player):
        pass

    def skip(self):
        pass

    def round_ended(self):
        pass

    def update_board(self):
        pass