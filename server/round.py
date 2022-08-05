class Round(object):
    def __init__(self, word, player_drawing) -> None:
        self.word = word
        self.player_drawing = player_drawing
        self.player_guesses = []
        self.skips = 0
        self.player_scores = {player:0 for player in player_drawing}

    def guess(self, player, wrd):
        return wrd == self.word

    

    