from round import Round

class Game(object):
    def __init__(self, id, players) -> None:
        self.id = id
        self.players = players
        self.words_used  = []
        self.round = None
        self.board = None
        self.player_draw_ind = 0
        self.start_new_round()

    def start_new_round(self):
        """start a new round with a new word
        """

        self.round = Round(self.get_word(), self.players[self.player_draw_ind])
        self.player_draw_ind +=1

        if self.player_draw_ind >= len(self.players):
            self.end_round()
            self.end_game()


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